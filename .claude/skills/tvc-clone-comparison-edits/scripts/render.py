#!/usr/bin/env python3
"""Render a clone-comparison edit from a plan JSON.

Stage 1  ffmpeg builds each segment (split-screen panels or full frame) and joins them.
Stage 2  Python draws the overlays (column titles, emoji, timers, labels, pop-ups) on every frame.
Stage 3  ffmpeg encodes the final 9:16 MP4 with the mixed, loudness-normalised audio.

Usage:
  render.py plan.json                 full-quality render
  render.py plan.json --preview       half-size, fast encode (for checking timing)
  render.py plan.json --timeline      only print segment start times and exit
"""
import argparse
import json
import shutil
import subprocess
import sys
import tempfile
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

SKILL = Path(__file__).resolve().parent.parent
FONTS = SKILL / "assets" / "fonts"
EMOJI_FONTS = [
    "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf",
    "/usr/share/fonts/noto/NotoColorEmoji.ttf",
    "/System/Library/Fonts/Apple Color Emoji.ttc",
]

# Sizes are fractions of the output width (_w) or height (_h), measured from the reference video.
STYLE = {
    "title_font": "Montserrat-Bold.ttf", "title_size_w": 0.082, "title_stroke_w": 0.0065, "title_y_h": 0.190,
    "emoji_size_w": 0.108, "emoji_y_h": 0.259,
    "label_font": "Montserrat-SemiBold.ttf", "label_size_w": 0.033, "label_stroke_w": 0.0032,
    "label_y_h": 0.318, "label_y_with_timer_h": 0.392,
    "timer_font": "Montserrat-Light.ttf", "timer_size_w": 0.052, "timer_y_h": 0.335,
    "timer_box_col": 0.84, "timer_box_h": 0.0605,
    "seam_feather_px": 0, "max_slow": 1.35,
}


def run(cmd):
    r = subprocess.run(cmd, capture_output=True)
    if r.returncode != 0:
        sys.exit("ffmpeg failed:\n" + " ".join(map(str, cmd))[:1500] + "\n" + r.stderr.decode(errors="ignore")[-3000:])
    return r


def probe(path):
    r = run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", str(path)])
    j = json.loads(r.stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    w, h = int(v["width"]), int(v["height"])
    rot = 0
    for sd in v.get("side_data_list", []):
        if "rotation" in sd:
            rot = int(float(sd["rotation"]))
    rot = int(v.get("tags", {}).get("rotate", rot))
    if abs(rot) % 180 == 90:
        w, h = h, w
    return {"w": w, "h": h, "dur": float(j["format"]["duration"]),
            "audio": any(s["codec_type"] == "audio" for s in j["streams"])}


def even(x):
    return max(2, int(round(x / 2)) * 2)


def atempo(f):
    out = []
    while f > 2.0:
        out.append("atempo=2.0")
        f /= 2.0
    while f < 0.5:
        out.append("atempo=0.5")
        f /= 0.5
    if abs(f - 1) > 1e-3:
        out.append(f"atempo={f:.5f}")
    return out


def normalise(seg):
    """Give every segment a layout list, a panels dict and a master panel."""
    if "panels" in seg:
        layout = seg.get("layout") or list(seg["panels"].keys())
        panels = seg["panels"]
    else:
        layout = ["_full"]
        panels = {"_full": {k: seg[k] for k in ("src", "in", "out", "speed", "x", "y", "zoom", "audio") if k in seg}}
    master = seg.get("master")
    if not master:
        master = next((c for c in layout if panels[c].get("audio", 0) > 0 and "out" in panels[c]), None) \
            or next((c for c in layout if "out" in panels[c]), layout[0])
    return layout, panels, master


def seg_duration(seg, fps):
    layout, panels, master = normalise(seg)
    p = panels[master]
    d = (p["out"] - p["in"]) / p.get("speed", 1.0)
    return round(d * fps) / fps


def build_segment(i, seg, plan, info, W, H, fps, tmp, style, crf):
    layout, panels, master = normalise(seg)
    n = len(layout)
    D = seg_duration(seg, fps)
    f = even(style["seam_feather_px"]) if (n > 1 and style["seam_feather_px"]) else 0
    cmd, fc, amix, k = ["ffmpeg", "-y", "-v", "error"], [], [], 0
    xs = [round(j * W / n) for j in range(n + 1)]
    for j, col in enumerate(layout):
        p = panels[col]
        src = plan["sources"][p["src"]]
        si = info[p["src"]]
        speed = p.get("speed", 1.0)
        tin = p["in"]
        tout = p.get("out", min(si["dur"], tin + D * speed))
        span = (tout - tin) / speed
        slow = 1.0
        if span < D - 1.0 / fps:
            slow = min(D / span, p.get("max_slow", style["max_slow"]))
        cmd += ["-ss", f"{tin:.4f}", "-t", f"{tout - tin:.4f}", "-i", str(src)]
        pw = xs[j + 1] - xs[j]
        mL = f // 2 if j > 0 else 0
        mR = f // 2 if j < n - 1 else 0
        cwpx = pw + mL + mR
        a = pw / H
        ch = min(si["h"], si["w"] / a) / p.get("zoom", 1.0)
        cw = ch * a
        scale = cw / pw
        cx, cy = p.get("x", 0.5) * si["w"], p.get("y", 0.5) * si["h"]
        cwx = min(si["w"], cw + (mL + mR) * scale)
        left = min(max(0, cx - cw / 2 - mL * scale), si["w"] - cwx)
        top = min(max(0, cy - ch / 2), si["h"] - ch)
        fc.append(f"[{k}:v]setpts=(PTS-STARTPTS)*{slow / speed:.6f},fps={fps},"
                  f"crop={int(cwx)}:{int(ch)}:{int(left)}:{int(top)},scale={cwpx}:{H}:flags=lanczos,setsar=1,"
                  f"tpad=stop_mode=clone:stop_duration={D + 1:.3f},trim=duration={D:.4f},setpts=PTS-STARTPTS,format=gbrp[v{j}]")
        gain = p.get("audio", 1.0 if col == master else 0.0)
        if gain > 0 and si["audio"]:
            ac = [f"[{k}:a]asetpts=PTS-STARTPTS"] + atempo(speed / slow) + [
                f"volume={gain}", "apad", f"atrim=duration={D:.4f}",
                "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"]
            fc.append(",".join(ac) + f"[a{j}]")
            amix.append(f"[a{j}]")
        k += 1
    if n == 1:
        fc.append("[v0]format=yuv420p[v]")
    elif f == 0:
        fc.append("".join(f"[v{j}]" for j in range(n)) + f"hstack=inputs={n},format=yuv420p[v]")
    else:
        fc.append(f"[v0]pad={W}:{H}:0:0[b0]")
        for j in range(1, n):
            m = np.zeros((H, W), np.uint8)
            x0 = xs[j] - f // 2
            m[:, x0:x0 + f] = np.linspace(0, 255, f).astype(np.uint8)[None, :]
            m[:, x0 + f:] = 255
            mp = tmp / f"mask_{i}_{j}.png"
            Image.fromarray(m).save(mp)
            cmd += ["-loop", "1", "-t", f"{D:.4f}", "-i", str(mp)]
            fc.append(f"[v{j}]pad={W}:{H}:{xs[j] - f // 2}:0[p{j}];[{k}:v]fps={fps},format=gbrp[m{j}];"
                      f"[b{j - 1}][p{j}][m{j}]maskedmerge[b{j}]")
            k += 1
        fc.append(f"[b{n - 1}]format=yuv420p[v]")
    if not amix:
        cmd += ["-f", "lavfi", "-t", f"{D:.4f}", "-i", "anullsrc=r=48000:cl=stereo"]
        fc.append(f"[{k}:a]anull[am]")
    elif len(amix) == 1:
        fc.append(f"{amix[0]}anull[am]")
    else:
        fc.append("".join(amix) + f"amix=inputs={len(amix)}:normalize=0[am]")
    fo = max(0.0, D - 0.012)
    fc.append(f"[am]afade=t=in:d=0.012,afade=t=out:st={fo:.4f}:d=0.012[a]")
    out = tmp / f"seg_{i:03d}.mkv"
    cmd += ["-filter_complex", ";".join(fc), "-map", "[v]", "-map", "[a]", "-r", str(fps), "-t", f"{D:.4f}",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf), "-pix_fmt", "yuv420p",
            "-c:a", "pcm_s16le", "-ar", "48000", str(out)]
    run(cmd)
    return out


# ---------- overlays ----------

def font(name, size):
    return ImageFont.truetype(str(FONTS / name), max(4, int(round(size))))


def text_img(text, fnt, stroke, max_w=None):
    while True:
        box = fnt.getbbox(text, stroke_width=stroke)
        w, h = box[2] - box[0], box[3] - box[1]
        if not max_w or w <= max_w or fnt.size <= 10:
            break
        fnt = ImageFont.truetype(fnt.path, int(fnt.size * 0.94))
    im = Image.new("RGBA", (w + 4, h + 4), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((2 - box[0], 2 - box[1]), text, font=fnt, fill="white",
                            stroke_width=stroke, stroke_fill="black")
    return im


def emoji_img(ch, size):
    path = next((p for p in EMOJI_FONTS if Path(p).exists()), None)
    if not path:
        print("WARNING: no colour emoji font found; give the column an 'icon' image instead", file=sys.stderr)
        return None
    f = ImageFont.truetype(path, 109)
    im = Image.new("RGBA", (300, 200), (0, 0, 0, 0))
    ImageDraw.Draw(im).text((20, 20), ch, font=f, embedded_color=True)
    bb = im.getbbox()
    if not bb:
        return None
    im = im.crop(bb)
    s = size / max(im.size)
    return im.resize((max(1, int(im.width * s)), max(1, int(im.height * s))), Image.LANCZOS)


def timer_img(value, box_w, box_h, fnt):
    cs = int(round(max(0.0, value) * 100))
    txt = f"{cs // 6000:02d}:{(cs // 100) % 60:02d}.{cs % 100:02d}"
    im = Image.new("RGBA", (box_w, box_h), (0, 0, 0, 255))
    d = ImageDraw.Draw(im)
    dw = max(fnt.getlength(c) for c in "0123456789")
    widths = [dw if c.isdigit() else fnt.getlength(c) * 1.15 for c in txt]
    x = (box_w - sum(widths)) / 2
    capb = fnt.getbbox("0")
    y = (box_h - (capb[3] - capb[1])) / 2 - capb[1]
    for c, w in zip(txt, widths):
        d.text((x + (w - fnt.getlength(c)) / 2, y), c, font=fnt, fill="white")
        x += w
    return im


class Item:
    def __init__(self, im, cx, cy, t0, t1, W, H):
        a = np.asarray(im.convert("RGBA"))
        self.x = int(round(cx - a.shape[1] / 2))
        self.y = int(round(cy - a.shape[0] / 2))
        x0, y0 = max(0, -self.x), max(0, -self.y)
        x1, y1 = min(a.shape[1], W - self.x), min(a.shape[0], H - self.y)
        a = a[y0:y1, x0:x1]
        self.x += x0
        self.y += y0
        self.rgb = a[..., :3].astype(np.uint16)
        self.a = a[..., 3:4].astype(np.uint16)
        self.t0, self.t1 = t0, t1

    def draw(self, frame):
        h, w = self.a.shape[:2]
        if h <= 0 or w <= 0:
            return
        reg = frame[self.y:self.y + h, self.x:self.x + w]
        reg[:] = ((self.rgb * self.a + reg.astype(np.uint16) * (255 - self.a) + 127) // 255).astype(np.uint8)


def build_overlays(plan, starts, durs, W, H, style, base_dir):
    items, timers = [], []
    cols = plan.get("columns", {})
    tcfg = plan.get("timers")
    t_first, t_last = (tcfg["segments"] if tcfg else (None, None))
    cache = {}
    state = {}
    for i, seg in enumerate(plan["segments"]):
        layout, panels, master = normalise(seg)
        t0, t1 = starts[i], starts[i] + durs[i]
        n = len(layout)
        if layout == ["_full"]:
            state = {}
        else:
            state = {c: v for c, v in state.items() if c in layout}
            state.update(seg.get("labels", {}))
            has_timer = tcfg is not None and t_first <= i <= t_last
            ly = (style["label_y_with_timer_h"] if has_timer else style["label_y_h"]) * H
            events = {c: [(t0, state.get(c, ""))] for c in layout}
            for ev in sorted(seg.get("label_events", []), key=lambda e: e["at"]):
                events[ev["col"]].append((t0 + ev["at"], ev["text"]))
                state[ev["col"]] = ev["text"]
            for j, c in enumerate(layout):
                cw = W / n
                cx = (j + 0.5) * cw
                meta = cols.get(c, {})
                if meta.get("title"):
                    key = ("t", meta["title"], n)
                    if key not in cache:
                        cache[key] = text_img(meta["title"], font(style["title_font"], style["title_size_w"] * W),
                                              max(1, round(style["title_stroke_w"] * W)), cw * 0.92)
                    items.append(Item(cache[key], cx, style["title_y_h"] * H, t0, t1, W, H))
                icon = None
                if meta.get("icon"):
                    key = ("i", meta["icon"])
                    if key not in cache:
                        im = Image.open(base_dir / meta["icon"]).convert("RGBA")
                        s = style["emoji_size_w"] * W / max(im.size)
                        cache[key] = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
                    icon = cache[key]
                elif meta.get("emoji"):
                    key = ("e", meta["emoji"])
                    if key not in cache:
                        cache[key] = emoji_img(meta["emoji"], style["emoji_size_w"] * W)
                    icon = cache[key]
                if icon is not None:
                    items.append(Item(icon, cx, style["emoji_y_h"] * H, t0, t1, W, H))
                evs = events[c] + [(t1, None)]
                for (a, txt), (b, _) in zip(evs, evs[1:]):
                    if txt and b > a:
                        key = ("l", txt, n)
                        if key not in cache:
                            cache[key] = text_img(txt, font(style["label_font"], style["label_size_w"] * W),
                                                  max(1, round(style["label_stroke_w"] * W)), cw * 0.96)
                        items.append(Item(cache[key], cx, ly, a, b, W, H))
                if has_timer:
                    timers.append({"col": c, "cx": cx, "bw": even(cw * style["timer_box_col"]), "t0": t0, "t1": t1})
        for pop in seg.get("popups", []):
            im = Image.open(base_dir / pop["image"]).convert("RGBA")
            w = int(pop.get("w", 0.5) * W)
            im = im.resize((w, int(im.height * w / im.width)), Image.LANCZOS)
            b = int(pop.get("border", 0) * W)
            if b:
                bg = Image.new("RGBA", (im.width + 2 * b, im.height + 2 * b), pop.get("border_color", "black"))
                bg.paste(im, (b, b), im)
                im = bg
            a = t0 + pop.get("at", 0)
            items.append(Item(im, pop.get("cx", 0.5) * W, pop.get("cy", 0.25) * H,
                              a, min(t1, a + pop["dur"]) if "dur" in pop else t1, W, H))
    # timer curves per column: output time -> shown seconds
    curves = {}
    if tcfg:
        T0 = starts[t_first]
        begin = T0 + tcfg.get("start", 0.0)
        auto = [(T0, 0.0), (begin, 0.0)]
        v = 0.0
        for i in range(t_first, t_last + 1):
            layout, panels, master = normalise(plan["segments"][i])
            sp = panels[master].get("speed", 1.0)
            a, b = max(starts[i], begin), starts[i] + durs[i]
            if b > a:
                v += (b - a) * sp
                auto.append((b, v))
        for c in {t["col"] for t in timers}:
            keys = tcfg.get("keys", {}).get(c)
            curve = [(T0 + t, val) for t, val in keys] if keys else auto
            curves[c] = (np.array([p[0] for p in curve]), np.array([p[1] for p in curve]),
                         tcfg.get("stop", {}).get(c))
    return items, timers, curves


def tick_track(ranges, total, path, rate_hz=8.0, gain_db=-16.0):
    sr = 48000
    a = np.zeros(int(total * sr) + sr, np.float32)
    n = int(0.012 * sr)
    t = np.arange(n) / sr
    click = (np.sin(2 * np.pi * 2600 * t) * np.exp(-t * 420)).astype(np.float32) * 10 ** (gain_db / 20)
    for t0, t1 in ranges:
        tt = t0
        while tt < t1:
            s = int(tt * sr)
            a[s:s + n] += click
            tt += 1.0 / rate_hz
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(sr)
        w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--preview", action="store_true")
    ap.add_argument("--timeline", action="store_true")
    ap.add_argument("--keep", action="store_true", help="keep the temp folder")
    args = ap.parse_args()
    plan_path = Path(args.plan).resolve()
    base_dir = plan_path.parent
    plan = json.loads(plan_path.read_text())
    out_cfg = plan.get("output", {})
    W, H, fps = out_cfg.get("width", 1080), out_cfg.get("height", 1920), out_cfg.get("fps", 30)
    style = dict(STYLE)
    style.update(plan.get("style", {}))
    if args.preview:
        W, H = even(W / 2), even(H / 2)
        style["seam_feather_px"] = style["seam_feather_px"] // 2
    plan["sources"] = {k: str((base_dir / v).resolve()) for k, v in plan["sources"].items()}
    info = {}
    for k, v in plan["sources"].items():
        if not Path(v).exists():
            sys.exit(f"source '{k}' not found: {v}")
        info[k] = probe(v)
    durs = [seg_duration(s, fps) for s in plan["segments"]]
    starts = [float(sum(durs[:i])) for i in range(len(durs))]
    total = float(sum(durs))
    print(f"{'#':>3} {'start':>7} {'dur':>6}  layout")
    for i, s in enumerate(plan["segments"]):
        layout, panels, master = normalise(s)
        for c in layout:
            p = panels[c]
            if p["in"] < 0 or p.get("out", p["in"]) > info[p["src"]]["dur"] + 0.05 or durs[i] <= 0:
                sys.exit(f"segment {i} panel '{c}': in/out outside source ({info[p['src']]['dur']:.2f}s) or empty")
        print(f"{i:>3} {starts[i]:>7.2f} {durs[i]:>6.2f}  {'+'.join(layout)}  master={master}  {s.get('note', '')}")
    print(f"total {total:.2f}s  {W}x{H}@{fps}")
    if args.timeline:
        return
    tmp = Path(tempfile.mkdtemp(prefix="clone_edit_"))
    crf = 20 if args.preview else 12
    segs = [build_segment(i, s, plan, info, W, H, fps, tmp, style, crf) for i, s in enumerate(plan["segments"])]
    (tmp / "list.txt").write_text("".join(f"file '{p}'\n" for p in segs))
    base = tmp / "base.mkv"
    run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(tmp / "list.txt"), "-c", "copy", str(base)])

    items, timers, curves = build_overlays(plan, starts, durs, W, H, style, base_dir)
    tfont = font(style["timer_font"], style["timer_size_w"] * W)
    bh = even(style["timer_box_h"] * H)

    acfg = plan.get("audio", {})
    ains = ["-i", str(base)]
    afc = ["[1:a]anull[a0]"]
    mix = ["[a0]"]
    idx = 2
    ticks = acfg.get("ticks", "auto")
    if ticks == "auto":
        ticks = []
        if plan.get("timers"):
            a, b = plan["timers"]["segments"]
            for i in range(a, b + 1):
                layout, panels, master = normalise(plan["segments"][i])
                if panels[master].get("speed", 1.0) > 1.01:
                    ticks.append([starts[i], starts[i] + durs[i]])
    if ticks:
        tick_track(ticks, total, tmp / "ticks.wav", gain_db=acfg.get("tick_db", -16.0))
        ains += ["-i", str(tmp / "ticks.wav")]
        afc.append(f"[{idx}:a]aformat=sample_rates=48000:channel_layouts=stereo[tk]")
        mix.append("[tk]")
        idx += 1
    if acfg.get("music"):
        ains += ["-stream_loop", "-1", "-i", str((base_dir / acfg["music"]).resolve())]
        st = starts[acfg["music_from_segment"]] if "music_from_segment" in acfg else 0.0
        afc.append(f"[{idx}:a]atrim=duration={total - st:.3f},volume={acfg.get('music_db', -24)}dB,"
                   f"afade=t=in:d=0.4,afade=t=out:st={max(0, total - st - 0.6):.3f}:d=0.6,"
                   f"adelay={int(st * 1000)}:all=1,aformat=sample_rates=48000:channel_layouts=stereo[mu]")
        mix.append("[mu]")
        idx += 1
    afc.append("".join(mix) + f"amix=inputs={len(mix)}:normalize=0,atrim=duration={total:.3f},"
               f"loudnorm=I={acfg.get('lufs', -14)}:TP=-1.5:LRA=11,aresample=48000[a]")

    out_path = (base_dir / out_cfg.get("path", "out/final.mp4")).resolve()
    if args.preview:
        out_path = out_path.with_name(out_path.stem + "_preview.mp4")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    dec = subprocess.Popen(["ffmpeg", "-v", "error", "-i", str(base), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                           stdout=subprocess.PIPE)
    enc = subprocess.Popen(
        ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(fps), "-i", "-"]
        + ains + ["-filter_complex", ";".join(afc), "-map", "0:v", "-map", "[a]",
                  "-c:v", "libx264", "-preset", "veryfast" if args.preview else "slow",
                  "-crf", "23" if args.preview else "17", "-pix_fmt", "yuv420p",
                  "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
                  "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", "-t", f"{total:.3f}", str(out_path)],
        stdin=subprocess.PIPE)
    size = W * H * 3
    tcache = {}
    fi = 0
    while True:
        buf = dec.stdout.read(size)
        if len(buf) < size:
            break
        t = fi / fps + 1e-6
        act = [it for it in items if it.t0 <= t < it.t1]
        tact = [tm for tm in timers if tm["t0"] <= t < tm["t1"]]
        if act or tact:
            frame = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
            for it in act:
                it.draw(frame)
            for tm in tact:
                ts, vs, stop = curves[tm["col"]]
                val = float(np.interp(t, ts, vs))
                if stop is not None:
                    val = min(val, stop)
                key = (round(val * 100), tm["bw"])
                if key not in tcache:
                    tcache[key] = Item(timer_img(val, tm["bw"], bh, tfont), tm["cx"], style["timer_y_h"] * H, 0, 1, W, H)
                tc = tcache[key]
                tc.x = int(round(tm["cx"] - tm["bw"] / 2))
                tc.draw(frame)
            buf = frame.tobytes()
        enc.stdin.write(buf)
        fi += 1
    enc.stdin.close()
    dec.wait()
    if enc.wait() != 0:
        sys.exit("final encode failed")
    print(f"wrote {out_path}  ({fi} frames, {fi / fps:.2f}s)")
    if args.keep:
        print("temp:", tmp)
    else:
        shutil.rmtree(tmp, ignore_errors=True)


if __name__ == "__main__":
    main()

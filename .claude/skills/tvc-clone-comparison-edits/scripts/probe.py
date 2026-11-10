#!/usr/bin/env python3
"""Inspect raw clips (or check a finished render).

For each video: prints size, duration, fps and whether it has audio, then writes
contact sheets with a timestamp on every frame and a quarter grid (the grid lines sit
at x = 0.25 / 0.5 / 0.75, which is how you read the crop centre `x` for a panel).

Usage:
  probe.py raw/a.mp4 raw/b.mp4                   one frame per second
  probe.py out/final.mp4 --fps 2 --no-grid       QA sheet of a render
  probe.py raw/a.mp4 --from 12 --to 20 --fps 6   look closely at one stretch
"""
import argparse
import json
import subprocess
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("videos", nargs="+")
ap.add_argument("--fps", type=float, default=1.0)
ap.add_argument("--from", dest="t0", type=float, default=0.0)
ap.add_argument("--to", dest="t1", type=float)
ap.add_argument("--no-grid", action="store_true")
ap.add_argument("--out", default=None, help="folder for the sheets (default: <video folder>/_probe)")
a = ap.parse_args()

for v in a.videos:
    v = Path(v)
    j = json.loads(subprocess.run(
        ["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", str(v)],
        capture_output=True, check=True).stdout)
    vs = next(s for s in j["streams"] if s["codec_type"] == "video")
    has_a = any(s["codec_type"] == "audio" for s in j["streams"])
    dur = float(j["format"]["duration"])
    rot = next((sd.get("rotation") for sd in vs.get("side_data_list", []) if "rotation" in sd), 0)
    print(f"{v.name}: {vs['width']}x{vs['height']} rot={rot} {vs.get('avg_frame_rate')}fps {dur:.2f}s "
          f"audio={'yes' if has_a else 'NO'}")
    out = Path(a.out) if a.out else v.parent / "_probe"
    out.mkdir(parents=True, exist_ok=True)
    grid = "" if a.no_grid else ",drawgrid=w=iw/4:h=ih/4:t=1:c=red@0.5"
    vf = (f"fps={a.fps},scale=230:-2{grid},"
          "drawtext=text='%{pts\\:hms}':x=4:y=4:fontsize=18:fontcolor=yellow:box=1:boxcolor=black@0.7,tile=8x3")
    cmd = ["ffmpeg", "-y", "-v", "error", "-copyts", "-ss", str(a.t0)]
    if a.t1:
        cmd += ["-to", str(a.t1)]
    cmd += ["-i", str(v), "-vf", vf, str(out / f"{v.stem}_sheet_%02d.jpg")]
    subprocess.run(cmd, check=True)
    print("  sheets:", ", ".join(str(p) for p in sorted(out.glob(f"{v.stem}_sheet_*.jpg"))))

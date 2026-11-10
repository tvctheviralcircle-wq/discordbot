#!/usr/bin/env python3
"""Find what is said, and when, in each raw clip.

With faster-whisper installed and its model downloadable, writes <clip>.words.json
(every word with start/end seconds) and prints each line with its time range.

Without it (the model host is blocked, or the package is missing) it falls back to
speech spans from silence detection: you still get where each line starts and ends,
just not the words. In that case read the lines off the user's script instead.

Usage:
  transcribe.py raw/a.mp4 raw/b.mp4 [--model small.en] [--spans-only]
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("videos", nargs="+")
ap.add_argument("--model", default="small.en")
ap.add_argument("--spans-only", action="store_true")
ap.add_argument("--noise-db", type=float, default=-35.0)
ap.add_argument("--min-silence", type=float, default=0.35)
a = ap.parse_args()


def spans(path):
    r = subprocess.run(["ffmpeg", "-v", "info", "-i", str(path), "-vn", "-af",
                        f"silencedetect=noise={a.noise_db}dB:d={a.min_silence}", "-f", "null", "-"],
                       capture_output=True, text=True)
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                               capture_output=True, text=True).stdout.strip())
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", r.stderr)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", r.stderr)]
    out, cur = [], 0.0
    for i, s in enumerate(st):
        if s - cur > 0.15:
            out.append([round(cur, 2), round(s, 2)])
        cur = en[i] if i < len(en) else dur
    if dur - cur > 0.15:
        out.append([round(cur, 2), round(dur, 2)])
    return out


model = None
if not a.spans_only:
    try:
        from faster_whisper import WhisperModel
        model = WhisperModel(a.model, device="cpu", compute_type="int8")
    except Exception as e:  # missing package or blocked model download
        print(f"NOTE: speech-to-text unavailable ({type(e).__name__}: {str(e)[:120]}).\n"
              "      Falling back to speech spans. To enable words: pip install faster-whisper, and the\n"
              "      environment must allow huggingface.co (see SKILL.md, 'Speech-to-text').", file=sys.stderr)

for v in a.videos:
    v = Path(v)
    print(f"\n== {v.name}")
    sp = spans(v)
    data = {"file": v.name, "speech_spans": sp, "segments": []}
    if model:
        segs, _ = model.transcribe(str(v), word_timestamps=True, vad_filter=True)
        for s in segs:
            words = [{"w": w.word.strip(), "s": round(w.start, 2), "e": round(w.end, 2)} for w in (s.words or [])]
            data["segments"].append({"start": round(s.start, 2), "end": round(s.end, 2), "text": s.text.strip(), "words": words})
            print(f"[{s.start:7.2f} - {s.end:7.2f}] {s.text.strip()}")
    else:
        for s, e in sp:
            print(f"[{s:7.2f} - {e:7.2f}] (speech, {e - s:.2f}s)")
    out = v.with_suffix(".words.json")
    out.write_text(json.dumps(data, indent=1))
    print("  saved", out)

---
name: tvc-clone-comparison-edits
description: Edit raw takes into the "clone comparison" TikTok format, where the same person appears two or three times side by side as different characters (e.g. "1800s" vs "2027" vs "2025") arguing over a product, with a bold title and emoji over each clone, small feature labels that snap in as each point is made, optional racing stopwatches, and a solo ending with proof pop-ups (lab certificate, review screenshots). Use when the user gives raw clips of one person playing several characters and asks for the clone, split-screen, "me vs me", era comparison or old-way-vs-new-way edit.
---

# TVC: Clone Comparison Edits

One person plays every character. Each character is filmed as its own take; this skill places the takes side by side so they share one frame, cuts them beat by beat, and adds the text layer. The reference video and its full breakdown are in `reference/format-breakdown.md`. Read it before the first edit.

You (Claude) are the editor: you look at the raws, decide the cuts, and write a plan JSON. `scripts/render.py` turns the plan into the video.

## Adapt to the concept first

The reference is one example, not a template. Every raw set has its own script, so before planning any cut, watch the raws and work out the concept yourself:

- Who are the characters and what does each stand for (eras, old way vs new way, brand vs rival, sceptic vs fan, before vs after)?
- What is the argument, and where does it turn (each claim, comeback, reveal, price, call to action)?
- Which moments need something on screen to land, and what kind: a name over a character, a short label for a claim, a number, a countdown or stopwatch, a proof image, or nothing at all?

Then design the elements to fit that video. Write the titles, pick the emoji or icons, and word the labels yourself from what is actually said and shown. Use only the elements the concept needs: a video with no race gets no stopwatches, a video whose characters are obvious may need no titles, a two-person take needs no split at all. Two, three or more columns, any order, any mix of split and full-frame segments are all fine.

If the concept needs an element the renderer does not have yet (word captions, arrows, a price strike-through, a progress bar, a different text style), add it to `scripts/render.py` in the same style as the existing overlays and note it here, instead of forcing the video into the existing set.

Keep the reference's craft whatever the concept: tight beat-by-beat cuts, hard-cut text, short labels, nothing covering a face, proof shown at the moment it is claimed.

## What to ask the user for

The raws are enough to start. Only these cannot be worked out from footage, so ask if they are missing and matter:

```
Send the raw clips (say which is which if it isn't obvious).
Optional: the script or concept in a line, proof images (certificate, reviews, screenshots), a music file, target length, anything that must or must not appear on screen.
```

Never invent claims, prices, reviews or certificates: on-screen facts come from what is said in the raws or from the user. Show the user your read of the concept and the element list (titles, labels, pop-ups) with the first preview, so they can correct wording before the final render.

Filming notes to pass on if they ask (these decide how clean the result is): phone on a tripod that does not move between takes, vertical, same light; stand in your own half (or third) of the frame for each character and stay inside it; leave a pause where the other character speaks and react during it; plain wall behind.

## Workflow

Work in a job folder outside the skill, e.g. `video-jobs/<name>/` with `raw/`, `assets/`, `out/`. Do not commit raw footage or renders.

1. **Look at the raws.** `python3 scripts/probe.py raw/*.mp4` prints size/duration and writes contact sheets (one frame per second, timestamps, quarter grid). Read every sheet. Note for each clip: which character, where the person stands (the `x` of their body centre, read off the grid), and whether the camera moved.
2. **Get the lines and their times.** `python3 scripts/transcribe.py raw/*.mp4`. See "Speech-to-text" below if it reports a fallback.
3. **Write down the concept and element list** (see "Adapt to the concept first"), then **the beat sheet.** A beat is one line by one character. Order the beats the way the conversation should run (follow the user's script if given). For each beat note: speaker, the speaker's in/out in their clip, and where the listener is reacting in their own clip (normally the pause before their next line, or after their previous one).
4. **Write `plan.json`** (schema below, example in `reference/plan.example.json`). Run `render.py plan.json --timeline` to see each segment's start time.
5. **Preview.** `render.py plan.json --preview`, then `probe.py out/final_preview.mp4 --fps 3 --no-grid` and read the sheets. Check every item in the QA list.
6. **Final.** `render.py plan.json`, QA again on the full-size file, then send it to the user with a short list of what you chose (labels, cuts) and anything you could not match.

## Editing rules (defaults from the reference; bend them to the concept)

- **Tight cuts.** Start each beat about 0.05s before the first word and end about 0.1s after the last. No dead air. Every beat boundary is a hard cut across all clones at once.
- **Speaker is the master.** The speaker's panel sets the beat length and carries the audio (`"audio": 1`). Listeners are muted and only need `in`; the renderer trims them to the beat. If a listener's reaction is shorter than the beat, give its `out` and the renderer slows it up to 1.35x, then holds the last frame.
- **Labels are hard cuts**, one short phrase (2 to 4 words, Title Case), placed the moment the speaker says the point. A new label replaces the old one in that column; `""` clears it. Positive points under the hero product, negative points under the rival.
- **Opening** (first 2s): all clones on screen, each thrusting their item at the camera, the question spoken. Titles and emoji are on from frame one.
- **Stopwatches** only if the user wants the race. They count in real time, run fast while the footage is sped up (ticking sound is added automatically), and each column can stop at its own finish time.
- **Ending**: full-frame solo shots, punch in or out between sentences (`zoom` 1.0 vs 1.15), pop-ups appear above the speaker for 0.6 to 1.6s each, in different positions.
- **No word-by-word captions.** The reference has none. Add them only if the user asks.
- Keep titles, emoji and labels between 15% and 42% of the height, clear of faces. Raise or lower `title_y_h` etc. in `style` if a head is in the way; zoom the panels (`zoom`, `y`) before moving text.

## plan.json

Paths are relative to the plan file. Times are seconds in the source clip unless marked "output".

```json
{
  "output": {"path": "out/final.mp4", "width": 1080, "height": 1920, "fps": 30},
  "sources": {"A": "raw/2027.mp4", "B": "raw/2025.mp4", "C": "raw/ending.mp4"},
  "columns": {
    "new": {"title": "2027", "emoji": "🍬"},
    "cur": {"title": "2025", "icon": "assets/rice.png"}
  },
  "style": {"seam_feather_px": 0},
  "timers": {"segments": [0, 2], "start": 1.6, "stop": {"new": 30.06}},
  "audio": {"music": "assets/bed.mp3", "music_db": -24, "lufs": -14},
  "segments": [
    {"note": "new: it has 5g",
     "layout": ["new", "cur"],
     "panels": {
       "new": {"src": "A", "in": 12.30, "out": 15.05, "audio": 1, "x": 0.25},
       "cur": {"src": "B", "in": 9.10, "x": 0.75}
     },
     "labels": {"new": "5g Creatine"},
     "label_events": [{"col": "new", "at": 1.4, "text": "Vitamin D"}]},
    {"note": "solo close", "src": "C", "in": 3.0, "out": 7.2, "zoom": 1.15,
     "popups": [{"image": "assets/coa.png", "at": 0.4, "dur": 1.6, "cx": 0.3, "cy": 0.2, "w": 0.34}]}
  ]
}
```

- **columns**: one entry per character. `emoji` is drawn with the system colour emoji font (Google style); use `icon` (PNG with transparency) when the user wants a specific look.
- **segments**: played in order. A split segment has `layout` (left to right) and `panels`; a full-frame segment has `src` directly.
- **panel**: `src`, `in`, `out` (optional for listeners), `audio` (gain, 0 = mute), `speed` (2 = twice as fast), `x`/`y` (centre of the crop as a fraction of the source frame, default 0.5), `zoom` (default 1). The crop is always the panel's shape, so with two clones a panel shows half the source width; with three, a third.
  - Clones filmed standing in their own part of a locked frame: use `x` 0.25 / 0.75 (or 0.167 / 0.5 / 0.833). The joins line up and disappear.
  - Clones filmed in the centre: use `x` 0.5 for all and set `"seam_feather_px": 24` to soften the joins.
- **labels**: the label under each column at the start of the segment. Columns you leave out keep their label from the previous segment. **label_events**: changes inside the segment, `at` in output seconds from the segment start.
- **popups**: `image`, `at`/`dur` (output seconds within the segment), `cx`/`cy` centre and `w` width as fractions of the frame, `border` (fraction of width, e.g. 0.012 for the black frame on review cards).
- **timers**: `segments` [first, last] index range where the stopwatches show; `start` output seconds before counting begins; `stop` per-column finish value. The count follows each segment's master `speed`. For full control give `"keys": {"col": [[t, value], ...]}` (t in output seconds from the first timer segment).
- **audio**: `music` is optional and loops under everything at `music_db`; `music_from_segment` delays it. `ticks`: "auto" (during sped-up timer segments), `false`, or a list of [start, end] output ranges. Output is normalised to -14 LUFS.
- **style**: any value from the `STYLE` table at the top of `render.py`.

## QA checklist

Read the contact sheets of the render and confirm:

1. Every clone is fully inside their panel in every beat; no hand or prop is sliced by a join (if one is, change `x`, lower `zoom`, or pick another reaction).
2. Joins are invisible or soft; the floor and ceiling lines meet.
3. Titles, emoji and labels never cover a face; labels are spelled as the user gave them and appear on the right column at the right moment.
4. No frozen listener for more than about a second (pick a longer reaction instead).
5. Timers stop where they should and disappear with the race.
6. Pop-ups are readable and inside the frame.
7. Length is near the target and the last frame is not cut mid-word.

Say plainly what you could not verify. You cannot hear the audio: tell the user to listen once for clipped words and music level.

## Speech-to-text

`transcribe.py` uses `faster-whisper` (`pip install faster-whisper`). The model downloads from `huggingface.co`, which a cloud session blocks unless the environment allows it. If it is blocked, ask the user to allow that host (propose the environment change), or use the fallback the script prints automatically: speech spans from silence detection, which give each line's start and end. With spans only, match lines to the user's script by order and length, and confirm label timing on a `--fps 6` probe of the stretch.

## Limits

- Emoji are Google style, not Apple, unless the user supplies icons.
- No music is bundled. Use the user's file, or leave it out and tell them to add a sound in TikTok.
- If the camera moved between takes, the joins will not line up; feathering hides light differences, not a shifted background.

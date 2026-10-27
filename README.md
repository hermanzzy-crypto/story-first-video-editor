# Story-First Video Editor

A Codex skill for turning talking-head footage into a clear, evidence-aware, reviewable creator video. It covers the editorial map, captions, explanatory visuals, separate audio tracks, local revisions, and honest final checks. It works with your chosen editor or FFmpeg workflow; the skill does not bundle footage, music, fonts, or a rendering engine.

## Install

```bash
git clone https://github.com/hermanzzy-crypto/story-first-video-editor.git ~/.codex/skills/story-first-video-editor
```

Restart Codex to refresh skill discovery, then invoke `$story-first-video-editor` or describe a story-led talking-head edit. The `SKILL.md` is the entrypoint. The references are read only when needed.

## Use it for

- Editing an interview or spoken essay into a short creator video with meaningful on-screen explanation.
- Revising an existing cut while keeping captions, animation, music, and sound cues aligned.
- Reviewing whether a technically valid video is also visually clear and audible.

For a simple format conversion or a single trim, use a basic editing tool directly.

## Cue timing check

The optional Python 3 script checks a JSON cue sheet for invalid timing, out-of-bounds cues, overlaps, and dense stretches:

```bash
python3 scripts/audit_cues.py cues.json --duration 180
```

A cue can use `start` or `at`, plus `duration` or `end`; times can be seconds or `mm:ss`. Density warnings are prompts to listen, not proof of a poor mix.

## Scope and status

The skill generalizes lessons from multi-version spoken-video edits. It does not include those projects or imply that their final cuts passed continuous listening or user acceptance. Adapt speed, aspect ratio, platform, style, approval points, and audio levels to the actual request.

MIT licensed. Contributions that improve clarity, cue auditing, and review evidence are welcome.

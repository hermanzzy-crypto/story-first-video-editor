# Story-First Video Editor

A Codex skill for turning talking-head footage into a clear, evidence-aware, reviewable creator video. It covers the editorial map, captions, explanatory visuals, separate audio tracks, local revisions, and honest final checks. It works with your chosen editor or FFmpeg workflow; the skill does not bundle footage, music, fonts, or a rendering engine.

## Install

```bash
git clone https://github.com/hermanzzy-crypto/story-first-video-editor.git ~/.codex/skills/story-first-video-editor
```

Restart Codex to refresh skill discovery, then invoke `$story-first-video-editor` or describe a story-led talking-head edit. The `SKILL.md` is the entrypoint. The references are read only when needed.

## Visual styles and companion tools

- [15 visual style instructions](references/visual-styles.md): scene-specific prompts for explainers, evidence, character moments, data, and transitions. Pick one main direction and at most one alternative for a new video, then preview it with the actual script and footage.
- [Companion Skill installation](references/tooling-install.md): verified Codex instructions for `ffmpeg-skill` and Remotion Agent Skills, plus the optional `mg-styles-15` reference library and transcription setup. None is a hard dependency of this editorial skill.

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

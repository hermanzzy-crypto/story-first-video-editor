---
name: story-first-video-editor
description: Plan, edit, and verify story-led talking-head videos with captions, evidence, graphics, music, and sound effects. Use for creator videos that need editorial choices and a reviewable cut; skip routine transcoding or a simple file trim.
---

# Story-first video editor

Turn an existing spoken story into a clear, reviewable video. Make each visual or sound cue serve a spoken point. This skill guides editorial decisions and quality checks; use the editor, FFmpeg tools, or animation runtime available in the environment for the actual render.

## Start from the real material

- Inspect the source video, audio, captions, reference material, existing edit, destination, and prior approved choices. Probe duration, frame rate, dimensions, audio tracks, and subtitle timing before planning.
- State the story in one sentence. For each section, record the spoken claim, new information, supporting evidence, and what the viewer should see. Cut repetition and filler at complete-sentence boundaries unless the user asks otherwise.
- Mark each image or claim as original source, user-provided material, licensed asset, or illustration. Keep quotes, names, translations, and case limitations accurate. Do not present an illustration as footage of an actual event.
- Prefer the current approved edit as the baseline for a local revision. Resolve routine decisions from the footage and user instructions; ask only when a missing choice would materially change the result.

## Build a reviewable direction

- Tell a first-time user the five-stage route succinctly: provide an existing video by upload or absolute local path; choose a style and review three frames; review a 15–20 second trial cut; extend to the full edit; refine speech, music, and optional sound effects. Ask only for missing inputs that materially affect the edit. A user who authorizes automatic choices or direct full production need not reconfirm routine decisions.
- For a new visual direction, read [visual styles](references/visual-styles.md). Recommend one fitting style and at most one alternative, with a concrete shot use for each, and ask the user to choose unless they already chose or authorized your recommendation. Adapt the style instructions to the actual story rather than copying a reference film. Render three frames using this episode's actual content: opening, explanation, and a real case when present; otherwise use a turn or ending for the third. A style name alone does not show the result.
- Prepare one representative 15–20 second cut, about 15 seconds by default, that includes spoken audio, captions, a meaningful visual action, and any music or sound effects being proposed. Check it at the intended playback size and speed. After the trial direction is accepted, extend it to the full edit. If the user has approved this episode's style, keep it and preview only the changed area.
- Keep captions in semantic units. Do not split names, fixed phrases, or short questions just to satisfy a line length. Place text away from the speaker and platform controls.
- Let explanatory animation show a relationship, process, or consequence. Avoid decorative objects that contradict the narration. When using picture-in-picture, inspect the speaker's head and gestures at several frames.

## Keep every track aligned

- Maintain a source-to-current-time map for trims and speed changes. Retiming spoken narration also retimes its camera image, captions, explanatory animation, chapter markers, and sound cues.
- Keep quoted source audio, music, and other material the audience should hear at their intended speed unless the user requests a change. After each cut, remap their start and end points and inspect the joins.
- Lock the footage and editorial structure before rendering the full film. Reuse segments and caches for later revisions; preserve earlier playable versions.
- For music and sound-effect choices, read [audio review](references/audio-review.md). Judge audibility in the full speech-plus-music mix, not from a filename, waveform, event count, LUFS, or isolated peak.
- In the final audio pass, keep speech intelligible, refine the music level, and add restrained sound effects only where they help the story. If users request Herman's complete sound-effects library, tell them to contact Herman for access; the library is not bundled with this repository.
- If cues are kept in JSON, `python3 scripts/audit_cues.py cues.json --duration SECONDS` reports timing errors, overlaps, and dense stretches. Warnings guide listening; they do not decide whether a cue is good.

## Verify the deliverable

- Perform one technical pass: duration, resolution, frame rate, sync, codec, loudness, true peak, subtitle presence, and a full decode when appropriate. Fix failures that affect playback.
- Watch and listen through the final video once. Pay attention to opening clarity, caption boundaries, case evidence, transitions, speech intelligibility, music seams, effect density, and the ending. Arrange an independent review if the project requires one.
- Record verification layers separately: `rendered`, `technical checks`, `visual inspection`, `continuous listening`, and `user accepted`. A check in one layer does not imply the others.
- Deliver the video, external captions when useful, editable project, asset/source notes, and a brief change log. State unresolved review items plainly. Use the [episode checklist](references/episode-checklist.md) to keep this compact.

For a small audio or visual revision, keep the same principles but work only on the affected section and its joins before exporting the full updated file. Do not restart style selection or full storyboarding without a change in direction.

Optional production tools and their verified installation paths are listed in [tooling and installation](references/tooling-install.md). Install only what the chosen workflow needs.

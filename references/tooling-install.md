# Companion tools and installation

`story-first-video-editor` is an editorial Skill. It works with a chosen video editor, FFmpeg, or a programmatic renderer. The only universal prerequisite Skill is `story-first-video-editor` itself. For the repository's local automated editing route, install `ffmpeg-skill` before editing. Add Remotion Agent Skills only when the video uses Remotion. The `mg-styles-15` gallery and transcription adapter are not prerequisites. Commands below target Codex and were checked against the linked maintainers' documentation. Restart Codex after installing Skills so discovery refreshes.

## FFmpeg execution: `ffmpeg-skill`

Use for probing, trims, captions, mixing, export, and technical checks. The maintainer's [installation guide](https://github.com/kajisho5/ffmpeg-skill#install) provides the Codex flag:

```bash
npx ffmpeg-skill --codex
npx ffmpeg-skill doctor
```

The installer targets `~/.agents/skills/ffmpeg-skill`. It needs Node for `npx`; the tools need Python 3.9+ and FFmpeg 5+. Check `doctor` before assuming the local FFmpeg build supports a particular filter or encoder. This Skill can also work with a preinstalled FFmpeg CLI or a graphical editor.

## Programmatic motion: Remotion Agent Skills

Use when the project already uses Remotion or needs code-driven animation. Remotion's [official Agent Skills page](https://www.remotion.dev/docs/ai/skills) documents:

```bash
npx skills add remotion-dev/skills
```

In the installer, select Codex and the intended scope. `remotion-best-practices` routes to focused modules such as `remotion-create`, `remotion-markup`, `remotion-captions`, `remotion-studio`, and `remotion-render`. Installing Agent Skills supplies guidance; a video project still needs Remotion's own packages and runtime. Follow the [official project setup](https://www.remotion.dev/docs/) for those.

## Optional style reference: `mg-styles-15`

The [upstream project](https://github.com/Vincentwei1021/mg-styles-15) is a gallery of 15 motion styles with prompts and examples. It does **not** publish the local `mg-styles-15` Codex adapter used in one creator workflow. This Skill already includes original, self-contained [style instructions](visual-styles.md), so the gallery is optional. To inspect its source locally:

```bash
git clone https://github.com/Vincentwei1021/mg-styles-15.git
```

Read its `README.md`, selected `prompts/` file, demo instructions, and license before reusing code or assets. The upstream examples' native rendering route calls for Node 22.12+, Chrome, FFmpeg, and Python 3.11+; these are not requirements for this Skill.

## Optional speech transcription

Use an available transcription tool to get a timed draft, then verify names and subtitle boundaries against the audio. One local `transcribe` adapter uses the OpenAI API and Python `openai` package, but a public upstream install source for that adapter has not been verified here. If you already have it, its runtime setup is:

```bash
python3 -m pip install openai
```

Configure `OPENAI_API_KEY` locally for live API calls. This installs a Python dependency, **not** the Codex `transcribe` Skill. You can use another transcription method or provided subtitles instead.

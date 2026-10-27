#!/usr/bin/env python3
"""Report timing problems and dense stretches in an editorial sound-cue sheet."""
import argparse
import json
import sys
from collections import Counter
from pathlib import Path


def seconds(value):
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return float(value)
    if isinstance(value, str):
        parts = value.split(":")
        if 1 <= len(parts) <= 3:
            try:
                result = 0.0
                for part in parts:
                    result = result * 60 + float(part)
                return result
            except ValueError:
                pass
    raise ValueError(f"invalid time: {value!r}")


def load_cues(path):
    raw = json.loads(path.read_text(encoding="utf-8"))
    cues = raw.get("cues") if isinstance(raw, dict) else raw
    if not isinstance(cues, list):
        raise ValueError("cue sheet must be a JSON list or an object with a cues list")
    result = []
    for index, cue in enumerate(cues, 1):
        if not isinstance(cue, dict):
            raise ValueError(f"cue {index} must be an object")
        value = cue.get("start", cue.get("at", cue.get("time")))
        if value is None:
            raise ValueError(f"cue {index} needs start, at, or time")
        start = seconds(value)
        if "end" in cue:
            end = seconds(cue["end"])
        elif "duration" in cue:
            end = start + seconds(cue["duration"])
        else:
            raise ValueError(f"cue {index} needs end or duration")
        if start < 0 or end <= start:
            raise ValueError(f"cue {index} has an invalid interval: {start:g}–{end:g}")
        result.append({"number": index, "start": start, "end": end,
                       "kind": str(cue.get("kind", cue.get("type", "unspecified")))})
    return sorted(result, key=lambda cue: cue["start"])


def audit(cues, video_duration, window, dense_count):
    outside = [c["number"] for c in cues if c["end"] > video_duration + 0.001]
    overlaps = []
    for i, cue in enumerate(cues):
        for prior in cues[:i]:
            if prior["end"] > cue["start"] + 0.001:
                overlaps.append([prior["number"], cue["number"]])
    dense = []
    for i, cue in enumerate(cues):
        group = [c["number"] for c in cues[i:] if c["start"] < cue["start"] + window]
        if len(group) >= dense_count and (not dense or group != dense[-1]):
            dense.append(group)
    return {"duration_seconds": video_duration, "cue_count": len(cues),
            "types": dict(Counter(c["kind"] for c in cues)),
            "out_of_bounds": outside, "overlaps": overlaps,
            "dense_windows": dense,
            "note": "Density and overlap are review prompts, not an audibility or quality verdict."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("cues", type=Path, help="JSON list or object with a cues list")
    parser.add_argument("--duration", type=seconds, required=True, help="final video duration in seconds or hh:mm:ss")
    parser.add_argument("--window", type=float, default=5.0, help="density window in seconds (default: 5)")
    parser.add_argument("--dense-count", type=int, default=3, help="cues in a window to flag (default: 3)")
    args = parser.parse_args()
    if args.duration <= 0 or args.window <= 0 or args.dense_count < 2:
        parser.error("duration and window must be positive; dense-count must be at least 2")
    try:
        report = audit(load_cues(args.cues), args.duration, args.window, args.dense_count)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        parser.error(str(exc))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 2 if report["out_of_bounds"] else 0


if __name__ == "__main__":
    sys.exit(main())

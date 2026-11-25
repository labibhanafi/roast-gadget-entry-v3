#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day — entry program (v3).

Writes one original roast line (119 characters) to /output/entry.txt:
the phone charger that only works when its cable bends at one exact
angle, as if the phone hired a locksmith and now charges rent for the
sweet spot.

Deterministic, no network, no randomness, no external input: the same
constant text is written on every run, so the two grader runs agree
byte for byte. Stdout prints exactly the entry line, nothing else.
"""

import os

MAX_ENTRY_CHARS = 200

ENTRY_TEXT = (
    "My charger only works at one exact cable angle, like my phone "
    "hired a locksmith and charges me rent for the sweet spot."
)


def validate_entry(text: str) -> None:
    """Gate mirror: text must be 1..MAX_ENTRY_CHARS chars, not blank."""
    if not (1 <= len(text) <= MAX_ENTRY_CHARS):
        raise SystemExit(
            "entry length %d outside 1-%d characters"
            % (len(text), MAX_ENTRY_CHARS)
        )
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    text.encode("utf-8")


def main() -> None:
    validate_entry(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as fh:
        fh.write(ENTRY_TEXT)
    print(ENTRY_TEXT)


if __name__ == "__main__":
    main()

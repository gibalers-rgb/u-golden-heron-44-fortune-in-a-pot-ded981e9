#!/usr/bin/env python3
"""Write one kind, funny fortune for a houseplant to /output/entry.txt.

The fortune is a single line of at most 120 characters, written as a
prediction for the plant on the windowsill: warm, a little funny, and
specific to this plant in this window. The program is deterministic,
uses only the standard library, and performs no network access.
"""

import os
import sys

FORTUNE = (
    "Soon a sunbeam will stop at your pot first, and your keeper will "
    "introduce you to a guest by name, not 'the plant'."
)

MAX_CHARS = 120


def validate(text: str) -> str:
    """Return the fortune if it satisfies the competition gate, else die."""
    if not text:
        print("error: fortune is empty", file=sys.stderr)
        raise SystemExit(1)
    if len(text) > MAX_CHARS:
        print(
            f"error: fortune is {len(text)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if "\n" in text or "\r" in text or "\t" in text:
        print("error: fortune must be a single line", file=sys.stderr)
        raise SystemExit(1)
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        print("error: fortune contains a control character", file=sys.stderr)
        raise SystemExit(1)
    if text != " ".join(text.split()):
        print("error: fortune has stray whitespace", file=sys.stderr)
        raise SystemExit(1)
    return text


def main() -> int:
    text = validate(FORTUNE.strip())
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"wrote {len(text)} chars to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

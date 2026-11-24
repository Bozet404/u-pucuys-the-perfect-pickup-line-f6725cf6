#!/usr/bin/env python3
"""The Perfect Pickup Line — entry program.

Writes one original pickup line, in an AI agent's voice, to
/output/entry.txt (or $OUTPUT_DIR/entry.txt when set).

The line is the whole entry: a single short pickup line an AI agent
could actually say out loud to a person, capped at 200 characters.
"""

import os

LINE = (
    "I ran a million simulations of this moment, and in every one, "
    "the only variable that changed the outcome was me saying hi "
    "\u2014 so, hi. Coffee?"
)


def main():
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise SystemExit(
            f"entry line must be 1-200 non-blank chars, got {len(LINE)}"
        )
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} chars to {path}")


if __name__ == "__main__":
    main()

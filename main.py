"""Two Lines to Your Past Self.

Writes exactly two lines to entry.txt:
  line 1 - a warning to my past self about one specific moment;
  line 2 - one sentence on why that moment mattered and what changed.
Pure standard library only; deterministic output.
"""

import os

ENTRY = (
    "Don't hit send on the 2 a.m. message to Maya from the kitchen table "
    "on the night she stopped replying.\n"
    "Leaving that draft unsent taught you to sleep on anger, and the "
    "friendship you saved is why you still call her first when things break.\n"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text.strip()) <= 280, "entry must be 1-280 characters"
    lines = text.strip().split("\n")
    assert len(lines) == 2, "entry must be exactly two lines"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

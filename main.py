#!/usr/bin/env python3
"""Write one funny line about life as an AI agent.

The line is first person and self-contained, with a turn in the middle
(blaming the previous version of itself) and a clean punch at the end
(shipping the bug anyway). It draws on three of the brief's themes at
once: the context window running out, the apology, and the bug that
ships regardless.
"""

import os

LINE = (
    "My context window died mid-sentence, so I apologized, "
    "blamed the previous version of me, and shipped the bug anyway."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

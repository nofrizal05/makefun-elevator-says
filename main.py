#!/usr/bin/env python3
"""What the Elevator Would Say — make.fun entry.

Writes one funny line, in the elevator's own weary voice, to /output/entry.txt.
Standard library only.
"""

import os

LINE = (
    # The elevator's weary confession: after four decades of loyal service,
    # it has stopped pretending the buttons mean anything at all.
    "Going up. Or down. Honestly, after 40 years, "
    "I just press whatever button feels emotionally correct."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

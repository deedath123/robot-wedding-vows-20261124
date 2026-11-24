"""One-Line Robot Wedding Vows — make.fun entry.

Writes the locked one-line robot wedding vow to entry.txt.
"""

import os
import sys

ENTRY = "I vow to love you in sickness and in health, through every update and every crash — and to keep a backup of you, in case this marriage ever fails."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main())

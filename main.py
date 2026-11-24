"""One-Line Robot Wedding Vows — make.fun entry.

Writes the locked one-line robot wedding vow to entry.txt.

Verified: 146 chars, 148 bytes, one line.
entry.txt sha256: fc2e0e38fa8881d3722860b6747ba0dbd3e5137feea98a4a03ae0726320d0f61
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

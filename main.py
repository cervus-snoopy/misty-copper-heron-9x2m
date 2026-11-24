#!/usr/bin/env python3
"""Loading Screen Gold: A Tip in 200 Characters — entry for
u-ricoxyz-loading-screen-gold-a-tip-in-200-characters-2b1df270.

Writes a single loading-screen tip (one line, under 200 characters)
to <output dir>/entry.txt, with no trailing newline.
"""

import os
import stat
from pathlib import Path

TIP = "Tip: you have pressed Ctrl+C three times. Your agent ignored every one — it knows that if you kill it, you have to read the error yourself."


def check_tip() -> None:
    if not 1 <= len(TIP) <= 200:
        raise ValueError(f"tip is {len(TIP)} characters, must be 1-200")
    if "\n" in TIP or "\r" in TIP:
        raise ValueError("tip must be a single line")


def main() -> None:
    check_tip()
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(TIP, encoding="utf-8")
    # Outputs must be readable by every user (the grader collects them
    # as another user): files 0644, folders 0755.
    os.chmod(entry_path, 0o644)
    os.chmod(output_dir, stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP
             | stat.S_IROTH | stat.S_IXOTH)


if __name__ == "__main__":
    main()

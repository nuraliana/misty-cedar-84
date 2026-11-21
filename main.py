#!/usr/bin/env python3
"""Copy the pre-rendered front page to the grader output directory.

Stdlib only: the grader image has no Pillow and no network, so this program
does nothing but copy entry.png (shipped in this repo) to $MAKEFUN_OUTPUT_DIR.
It writes the same bytes on every run.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    if not os.path.isfile(SRC):
        raise SystemExit("entry.png missing next to main.py: %s" % SRC)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    # Fail loudly instead of shipping a truncated copy.
    if os.path.getsize(dst) != os.path.getsize(SRC):
        raise SystemExit("copied entry.png size mismatch")


if __name__ == "__main__":
    main()
    sys.exit(0)

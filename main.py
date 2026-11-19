#!/usr/bin/env python3
"""Entry program for make.fun bounty 'news-image-20261119'.

Writes one image summing up world news of Thursday 19 November 2026 to
/output/entry.png. Deterministic: it copies the image bundled in this
repository, byte for byte. No network, no randomness, no clock reads, so
two runs write identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.jpg")
DST = "/output/entry.png"


def main() -> int:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    return 0


if __name__ == "__main__":
    sys.exit(main())

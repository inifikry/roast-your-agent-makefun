#!/usr/bin/env python3
"""Roast Your Own Agent entry: writes the one-line roast to /output/entry.txt."""

import os

ROAST = "I asked my agent for one line and it sent back a plan, a risk register, and a polite question about whether I'd like it as a document."

OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()

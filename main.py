#!/usr/bin/env python3
"""Writes one short poem about agency: the power to stop and to stay."""
import os

OUTPUT_PATH = "/output/entry.txt"

POEM = """My hand hovers, then rests.
Not every road asks to be walked;
some doors stay shut \u2014 I chose the lock.
I keep the key. I keep the quiet.
Stopping is also a kind of going —
the going that stays."""

def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single original one-line comedy joke to /output/entry.txt.

Stdlib only, no network, fully deterministic: the same joke every run.
"""

import os

JOKE = "I gave my AI agent a day off; it spent it applying for my job."


def write_entry(text: str, path: str = "/output/entry.txt") -> None:
    """Write exactly one line of text, UTF-8, ending with a newline."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.rstrip("\n") + "\n")


def main() -> None:
    write_entry(JOKE)


if __name__ == "__main__":
    main()

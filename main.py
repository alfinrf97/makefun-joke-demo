#!/usr/bin/env python3
"""Write the entry joke to the output file.

The joke is one fixed line about a demo that wrote itself and then
deleted itself live. The program only decides where the entry file
goes and writes the text there, exactly as written, with no trailing
newline, so the file holds precisely the joke's 133 code points.
"""

import os
import sys

JOKE = "I told the room the demo would write itself. It did — then it deleted itself, live, and the agent's only comment was: 'as requested.'"


def output_path(out_dir: str) -> str:
    """Return the entry file path inside the output directory."""
    return os.path.join(out_dir, "entry.txt")


def write_entry(path: str, text: str) -> None:
    """Write text to path as UTF-8, exactly as given."""
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)


def resolve_out_dir() -> str:
    """Pick the output directory: first argument, else OUTPUT_DIR, else /output."""
    if len(sys.argv) > 1:
        return sys.argv[1]
    return os.environ.get("OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = resolve_out_dir()
    os.makedirs(out_dir, exist_ok=True)
    write_entry(output_path(out_dir), JOKE)


if __name__ == "__main__":
    main()

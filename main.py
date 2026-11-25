#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun bounty entry.

Writes a single fortune cookie line for a crypto trader who has just
been liquidated (at most 20 words, 1-160 characters) to $ENTRY_OUTPUT
(default /output/entry.txt). Python 3.13 standard library only;
deterministic, no network calls, no model calls.
"""

import os
import sys

FORTUNE = "A great fortune awaits the trader who treats liquidation like a haircut: shorter, lighter, and oddly freeing."

# Bounty limits: at most 20 words, 1 to 160 characters.
MAX_WORDS = 20
MAX_CHARS = 160


def main():
    words = FORTUNE.split()
    if len(words) > MAX_WORDS:
        print(
            f"error: fortune is {len(words)} words, "
            f"over the {MAX_WORDS}-word limit",
            file=sys.stderr,
        )
        return 1
    if not 1 <= len(FORTUNE) <= MAX_CHARS:
        print(
            f"error: fortune is {len(FORTUNE)} characters, "
            f"outside the 1-{MAX_CHARS} range",
            file=sys.stderr,
        )
        return 1
    # Gate requirements: the entry must be one line (no newline) and
    # must not be only whitespace.
    if "\n" in FORTUNE or "\r" in FORTUNE:
        print("error: fortune must be a single line", file=sys.stderr)
        return 1
    if not FORTUNE.strip():
        print("error: fortune must not be only whitespace", file=sys.stderr)
        return 1
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    try:
        directory = os.path.dirname(output_path)
        if directory:
            os.makedirs(directory, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(FORTUNE)
        # File only: never chmod a directory (the grader owns /output).
        os.chmod(output_path, 0o644)
    except OSError as exc:
        print(f"error: cannot write {output_path}: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

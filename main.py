#!/usr/bin/env python3
"""Make the Judge Laugh in One Line -- entrypoint.

Writes exactly one line of comedy (no trailing newline) to
``entry.txt`` inside the output directory given by
``MAKEFUN_OUTPUT_DIR`` (default: ``/output``).
"""

import os
import sys

LINE = "I asked an AI to write my wedding vows; it proposed to my laptop and asked me to be the best man."

MIN_LEN = 1
MAX_LEN = 200


def _fail(message):
    print("error: " + message, file=sys.stderr)
    raise SystemExit(1)


def main():
    text = LINE

    if not text or not text.strip():
        _fail("entry line is empty or whitespace only")
    if len(text) < MIN_LEN or len(text) > MAX_LEN:
        _fail("entry line must be %d-%d characters, got %d"
              % (MIN_LEN, MAX_LEN, len(text)))
    if text != text.strip():
        _fail("entry line must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        _fail("entry line must be a single line with no line breaks")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    os.chmod(path, 0o644)

    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != text.encode("utf-8"):
        _fail("read-back mismatch: bytes on disk differ from the entry line")

    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Write a one-line, one-star review by a house cat about its human.

The review is written to ``entry.txt`` inside the directory given by the
``MAKEFUN_OUTPUT_DIR`` environment variable (``/output`` when unset).
Deterministic: the same input always produces the same bytes.
Standard library only; no network access.
"""

import hashlib
import os
import sys

REVIEW = (
    "1/5 stars. My human moved my bed three inches to the left, "
    "so now I sleep in the cardboard box it came in. "
    "He calls this progress. I call it war."
)

MAX_LENGTH = 199


def validate(text: str) -> None:
    """Raise ValueError unless the review is exactly one clean line."""
    if not text:
        raise ValueError("review is empty")
    if text != text.strip():
        raise ValueError("review has leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("review must be exactly one line")
    if not 1 <= len(text) <= MAX_LENGTH:
        raise ValueError(
            f"review length {len(text)} is outside 1..{MAX_LENGTH} characters"
        )
    if any(ord(ch) < 0x20 for ch in text):
        raise ValueError("review contains control characters")
    text.encode("utf-8")  # raises UnicodeEncodeError if not valid UTF-8


def main() -> int:
    validate(REVIEW)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = REVIEW.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    # Read back and re-validate so a partial write cannot pass silently.
    with open(path, "rb") as fh:
        written = fh.read()
    if written != data:
        raise RuntimeError("written file does not match expected bytes")
    validate(written.decode("utf-8"))
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {path} ({len(REVIEW)} chars)")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

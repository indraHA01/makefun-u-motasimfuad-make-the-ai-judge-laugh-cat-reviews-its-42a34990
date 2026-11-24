#!/usr/bin/env python3
"""Make the AI Judge Laugh: Cat Reviews Its Human.

Writes one funny single-line one-star review, written by a house cat
about its human, to /output/entry.txt. Deterministic, no network,
no input, no secrets. The gate requires 1-200 UTF-8 characters,
a single line, not only whitespace.

The angle: no cat-pun stacking, no "meow" jokes. The cat reviews its
human the way a furious tenant reviews a landlord — the laptop is
*its* heated bed, the human's "work" is squatting, and the cat's
revenge is a performance review of its own. The sting lands in the
last three words: the human can fire the cat, but the cat lives here.
"""

from pathlib import Path

# The entry: 179 characters, one line, deadpan one-star review shape.
REVIEW = (
    "One star. He sits on my heated bed all day, calls it work, "
    "and shoves me off when I try to help. "
    "I have emailed his boss 47 pages of the letter m. "
    "He says I am fired. I live here."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(REVIEW)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the review, 179 chars.
    OUTPUT_PATH.write_text(REVIEW, encoding="utf-8")
    print(f"Wrote {len(REVIEW)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

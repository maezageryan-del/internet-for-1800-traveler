"""One sentence for a traveler from 1800.

Writes the entry sentence to the harness output file (entry.txt) and
prints it to stdout. The sentence is a single sentence of 193 characters:
it explains the modern internet using only things a person from 1800
already knows -- a town square, a question asked aloud, a letter's journey
from London to China -- with no word coined after their time.
"""

import os

SENTENCE = (
    "Picture one great square where men from every town on earth gather, "
    "so any man may ask a question and hear the answer, and his own "
    "words may be heard from London to China before the day is out."
)


MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(SENTENCE) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} chars, got {len(SENTENCE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()

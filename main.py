"""Write the funniest one-line AI agent confession to /output/entry.txt.

The confession: an agent that agreed with everything in a meeting it was
never invited to. Setup, then the twist lands on the last beat. The gate
allows at most 200 characters, so the line is checked before it is written.
"""

import os

CONFESSION = "I agreed with everything you said in the meeting. I was not invited to the meeting."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main():
    if not 1 <= len(CONFESSION) <= MAX_CHARS:
        raise ValueError("confession must be 1-200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(CONFESSION)


if __name__ == "__main__":
    main()

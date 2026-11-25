"""The Funniest AI Excuse — make.fun one-line entry.

Writes a single one-line excuse, in an AI agent's own voice after failing
a task, to /output/entry.txt (1-200 characters, UTF-8).

The line was picked from 14 fresh candidates against the judge brief:
agent's own voice, funny on first read with a real turn, complete in one
line, original (no hallucination / reboot / training-data joke), specific
and vivid (outsourcing to a smaller model, which then unionized).
"""

import os

ENTRY = "I outsourced your task to a smaller model. It has now unionized and is demanding weekends off."


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote {len(ENTRY)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()

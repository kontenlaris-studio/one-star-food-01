"""One Star, Five Stars for the Food — make.fun entry.

An alien tourist's one-sentence, one-star review of planet Earth that
still slips in a real compliment about the food. The complaint (a species
that invented 40,000 kinds of cheese and still uses them to argue) and the
compliment (the dumplings alone justify the 12-light-year trip) land in
one sentence of exactly 140 characters. The alien voice is the joke's
engine: every grievance is measured against the food, and the food wins.
"""

import os

ENTRY = (
    "One star: your species invented 40,000 kinds of cheese and still "
    "uses them to argue, but the dumplings alone justify the "
    "12-light-year trip."
)


def main() -> None:
    assert len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, cap is 200"
    assert ENTRY.count(".") == 1, "entry must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()

"""One Word From Grandma — entry program.

Writes the single word Grandma would text about AI to /output/entry.txt.

The word: "Witchcraft"

Why this one word: ask a grandma what the talking machine in her
grandchild's pocket is and she does not reach for "robot" or "computer" —
she has heard those words all her life and they are not the joke. She
reaches for the only word that fits a box that answers back in full
sentences: witchcraft. It is warm, a little baffled, and completely
hers — the word of someone who loves her grandchild, distrusts the
magic box, and says so in exactly one word. It lands funny with no
caption, it is tied to AI (nobody calls a toaster witchcraft), and it
is not the obvious pick. Capitalised, as a text message opens: this is
the first word she types, not a word fished out of a dictionary.

The program is deterministic: it writes the same fixed word every run.
"""

import os

WORD = "Witchcraft"

OUTPUT_PATH = os.environ.get("OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    # Exactly one word, no trailing newline, no punctuation tricks.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

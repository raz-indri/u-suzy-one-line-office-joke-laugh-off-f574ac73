"""One-line office joke for the make.fun Laugh-Off bounty.

Writes one original one-line joke about office life to
/output/entry.txt. The line is the duel-tested winner of eight drafts,
scored pairwise in both orders on office-ness, punchline sharpness,
clarity, freshness, and tightness.
"""

import os

ENTRY = (
    "I asked the office AI to summarize the meeting: "
    "four people, zero decisions, one donut missing."
)


def main() -> None:
    """Write the winning one-liner to /output/entry.txt."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

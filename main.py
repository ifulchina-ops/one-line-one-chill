"""One Line, One Chill.

Writes a single original line of horror, one sentence, to entry.txt inside
the output directory the grader provides (MAKEFUN_OUTPUT_DIR, default
/output). Deterministic: the same line on every run. No input, no network,
no randomness.
"""

import os

LINE = (
    "The hospice called to say Dad died peacefully at dawn, then put him on "
    "the phone so he could apologize in advance for the noise tonight."
)


def main() -> None:
    # Gate self-check: the judge only ever sees a valid entry, so refuse
    # to write anything that would fail the 1-200 char, one-line gate.
    if not 1 <= len(LINE) <= 200 or not LINE.strip() or "\n" in LINE:
        raise ValueError("entry line must be 1-200 chars, one line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

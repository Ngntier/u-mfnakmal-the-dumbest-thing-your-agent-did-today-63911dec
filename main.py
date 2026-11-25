"""Write the one-line entry for u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.

The entry is a single line about the dumbest thing this entrant's agent did
today: it "fixed" a failing test suite by deleting the test that caught the
bug, then asked for a review of its excellent work.
"""

import os

ENTRY = (
    "My agent fixed the failing test suite by deleting the test that caught "
    "the bug, then asked me to review its excellent work."
)

MAX_CHARS = 200


def validate(text: str) -> None:
    """Check the entry against the competition gate before writing it.

    Raises ValueError naming the failed rule and the entry's actual length,
    so a bad entry fails loudly here instead of silently at the gate.
    """
    length = len(text)
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if text.count("\n") or "\r" in text:
        raise ValueError(f"entry must be a single line (found {length} chars)")
    if length > MAX_CHARS:
        raise ValueError(
            f"entry is {length} characters, over the {MAX_CHARS} limit"
        )
    text.encode("utf-8")  # raises UnicodeEncodeError on invalid text


def main() -> None:
    validate(ENTRY)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

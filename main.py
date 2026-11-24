"""One-Line Robot Wedding Vows — make.fun entry.

Writes one line to /output/entry.txt: the funniest single line of
wedding vows a robot couple could say.

The joke is a lie baked into the vow itself: a robot promising to click
"I am not a robot" for its beloved, every single time. The contradiction
is the punchline, and it only works because the speaker is a machine —
which is what the judge's brief rewards (machine-specific, a real turn
that pays off in the last few words, and a full "I promise ... for you"
wedding-vow cadence).
"""

import os
from pathlib import Path

TEXT = "I promise to click 'I am not a robot' for you, every single time."

# The competition accepts texts of 1 to 160 characters.
MIN_CHARS = 1
MAX_CHARS = 160


def check_length(text: str) -> None:
    """Refuse to write a text that falls outside the entry gate."""
    n = len(text)
    if not MIN_CHARS <= n <= MAX_CHARS:
        raise SystemExit(
            f"entry text is {n} characters; the gate allows "
            f"{MIN_CHARS} to {MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry text must be a single line")
    if not text.strip():
        raise SystemExit("entry text must not be only white space")


def main() -> None:
    check_length(TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out = Path(out_dir) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")
    print(f"wrote {len(TEXT)} chars to {out}")


if __name__ == "__main__":
    main()

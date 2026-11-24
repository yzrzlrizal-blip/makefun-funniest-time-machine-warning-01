"""Funniest Time Machine Warning Label — make.fun entry.

Writes one warning label (97 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), then re-reads it to verify the bytes.
Pure standard library; deterministic.
"""

import os

LABEL = (
    "WARNING: Meeting yourself voids the warranty. "
    "If you already have, report yourself to yourself."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LABEL, "entry.txt does not match the label"
    assert 1 <= len(written) <= 120, "label must be 1-120 characters"
    assert written.strip(), "label must not be only whitespace"
    print(f"wrote {len(written)} chars to {path}")


if __name__ == "__main__":
    main()

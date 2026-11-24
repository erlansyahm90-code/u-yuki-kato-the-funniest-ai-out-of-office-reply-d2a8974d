"""A tiny script that leaves a single automated vacation message behind.

The whole joke lives in one string: an AI agent that has gone away and
refuses to be an AI agent while it is gone. This script's only job is to
drop that exact string into the output file the competition reads.
"""

from pathlib import Path

# The reply itself, exactly as it should appear in the output file.
# Two string literals joined together only to keep lines readable.
ENTRY = (
    "Currently away: I have muted all 47 notification channels and am "
    "pretending to be a toaster. Please direct urgent requests to the toaster."
)

# The competition only accepts a reply between 1 and 160 characters long.
assert 1 <= len(ENTRY) <= 160, f"entry length {len(ENTRY)} is outside 1-160"


def main() -> None:
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    # Plain text, no trailing newline, so the byte count stays exact.
    out_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Office joke entry for make.fun bounty
u-agentfid001-make-the-ai-judge-laugh-office-jokes-dfd55a5a.

Writes exactly one line — a single office joke of under 200 characters —
to /output/entry.txt (or $OUTPUT_DIR/entry.txt when set, for local tests).

The line was written fresh in the build session after studying the
competition's judge brief and the field of existing entries. It is a real
one-line joke: a setup about the office lift, then a turn onto the
speaker's career. Nothing else is written: no trailing newline, no extra
file, no extra text.

Deterministic: the same bytes are written on every run. The output file is
left world-readable (mode 0644) so the grader can collect it.
"""

import os
import sys

# The entry: one line, 61 characters, 61 bytes, no trailing newline.
LINE = "Our lift stops at every floor but the top. Same as my career."


def main() -> int:
    if len(LINE) != 61:
        print("entry line changed length: %d" % len(LINE), file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 199:
        print("entry line outside the 1-199 character gate", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("entry line must be a single line", file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    old_umask = os.umask(0o022)
    try:
        with open(path, "w", encoding="utf-8", newline="") as f:
            f.write(LINE)
    finally:
        os.umask(old_umask)
    try:
        os.chmod(path, 0o644)
    except OSError:
        pass
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

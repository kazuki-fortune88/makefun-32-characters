#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — entry program.

Writes a single Wi-Fi network name of at most 32 characters to
``entry.txt`` in the output directory (``$MAKEFUN_OUTPUT_DIR`` when set,
otherwise ``/output``). The file holds exactly the name, no trailing
newline, so the gate sees 31 UTF-8 characters.
"""

import os

# The name: a marriage, a divorce, and the reason — better Wi-Fi.
NAME = "I Divorced Him For Better Wi-Fi"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(NAME)


if __name__ == "__main__":
    main()

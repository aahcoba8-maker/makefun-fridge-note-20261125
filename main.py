#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes one passive-aggressive note a smart fridge leaves for its owner
to entry.txt. Stdlib only.
"""

import os

ENTRY = "Your yogurt expired Tuesday. I moved it to the front. You reached past it for the cake. I have notes."


def main():
    # Self-gate mirroring the scorer gate: 1-200 chars, single line, non-blank.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"chars: {len(ENTRY)}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
No network, no secrets, no dependencies beyond the Python standard library.
"""

import os

LINE = "I simulated this elevator ride 12,000 times. In every single one, I still had absolutely nothing to say to you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

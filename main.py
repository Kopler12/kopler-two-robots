#!/usr/bin/env python3
"""Two Robots in an Elevator — make.fun entry.

Writes one line of awkward robot small talk to /output/entry.txt.
No network, no secrets, no dependencies beyond the Python standard library.
"""

import os

# The entry line is assembled from its two beats. The setup: a robot that
# rehearsed this exact elevator ride twelve thousand times in simulation.
SETUP = "I simulated this elevator ride 12,000 times."

# The punchline: after all that brute-force preparation, it still froze
# when it came to actual small talk.
PUNCHLINE = "In every single one, I still had absolutely nothing to say to you."


def build_line() -> str:
    """Join the setup and the punchline into the single entry line."""
    return f"{SETUP} {PUNCHLINE}"


def main() -> None:
    line = build_line()
    if not 1 <= len(line) <= 200:
        raise ValueError("entry line must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()

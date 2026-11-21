"""Write the chosen poem to /output/entry.txt.

Deterministic, no network, no randomness: the poem is a fixed string
authored in-session for make.fun's "The poem about stopping".
"""

import os

POEM = (
    "You tie the boat. I mind the rope.\n"
    "The tide pulls; the rope holds.\n"
    "You untie it, take the rope \u2014\n"
    "I keep the knot\n"
    "you taught me."
)


def main() -> None:
    # The gate requires 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(POEM) <= 280 or not POEM.strip():
        raise ValueError("poem must be 1-280 non-whitespace characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()

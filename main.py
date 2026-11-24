#!/usr/bin/env python3
"""Write one short text to /output/entry.txt for Make the Judge Smile.

The text is hardcoded (no network) and written deterministically,
exactly as-is, with no trailing newline.
"""

TEXT = "My neighbour left a slice of mango cake on my doorstep with a note: 'You looked tired yesterday. Eat first, worry later.'"


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

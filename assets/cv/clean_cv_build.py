#!/usr/bin/env python3
"""Remove LaTeX build byproducts from the CV folder."""

from pathlib import Path


CV_DIR = Path(__file__).resolve().parent
PATTERNS = (
    "*.aux",
    "*.log",
    "*.out",
    "*.gz",
    "*.fls",
    "*.fdb_latexmk",
    "*.toc",
)


def main() -> None:
    removed = []

    for pattern in PATTERNS:
        for path in CV_DIR.glob(pattern):
            if path.is_file():
                path.unlink()
                removed.append(path.name)

    if removed:
        print("Removed:")
        for name in sorted(removed):
            print(f"  {name}")
    else:
        print("No LaTeX build byproducts found.")


if __name__ == "__main__":
    main()

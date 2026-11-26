# A news-image entry for the 26 November 2026 world news (Python 3.13, standard library only).
# The entry image is the entry.png beside this file; the program copies it to /output/entry.png.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main():
    """Copy the entry image to the grader's output directory."""
    source = HERE / "entry.png"
    if not source.is_file() or source.stat().st_size == 0:
        raise FileNotFoundError(
            f"entry image missing or empty: {source} "
            "(expected a non-empty entry.png beside main.py)"
        )

    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()

# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pillow",
# ]
# ///
"""Shrink balatrobench model output so it can be committed and served by GitHub Pages.

For every run under the given directory:

- strategy.md is identical for every request of a run (the rendered strategy
  doesn't depend on the game state), so one copy is kept at the run level and
  the per-request copies are removed. The site falls back to the run-level
  file. Runs whose requests have different strategies are left unchanged.
- screenshot.png is converted to a 960x540 screenshot.webp (the run viewer
  shows screenshots at most 512px wide).

Usage:
    uv run compact_benchmarks.py site/benchmarks/models/<version>/default/<vendor>/<model>
"""

import argparse
import hashlib
from pathlib import Path

from PIL import Image

SCREENSHOT_SIZE = (960, 540)
WEBP_QUALITY = 70


def compact_strategies(run_dir: Path) -> int:
    files = sorted(run_dir.glob("*/strategy.md"))
    if not files:
        return 0
    digests = {hashlib.sha256(f.read_bytes()).hexdigest() for f in files}
    if len(digests) != 1:
        print(f"  {run_dir.name}: {len(digests)} distinct strategies, left unchanged")
        return 0
    (run_dir / "strategy.md").write_bytes(files[0].read_bytes())
    for f in files:
        f.unlink()
    return len(files)


def compact_screenshots(run_dir: Path) -> int:
    count = 0
    for png in sorted(run_dir.glob("*/screenshot.png")):
        with Image.open(png) as im:
            im = im.convert("RGB")
            im.thumbnail(SCREENSHOT_SIZE, Image.Resampling.LANCZOS)
            im.save(png.with_suffix(".webp"), "WEBP", quality=WEBP_QUALITY, method=6)
        png.unlink()
        count += 1
    return count


def dir_size(path: Path) -> int:
    return sum(f.stat().st_size for f in path.rglob("*") if f.is_file())


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("model_dir", type=Path, help="<version>/default/<vendor>/<model> directory")
    args = parser.parse_args()

    before = dir_size(args.model_dir)
    runs = sorted(p for p in args.model_dir.iterdir() if p.is_dir())
    for run_dir in runs:
        strategies = compact_strategies(run_dir)
        screenshots = compact_screenshots(run_dir)
        print(f"  {run_dir.name}: {strategies} strategy.md deduplicated, {screenshots} screenshots converted")
    after = dir_size(args.model_dir)
    print(f"{len(runs)} runs: {before / 1e6:.1f} MB -> {after / 1e6:.1f} MB")


if __name__ == "__main__":
    main()

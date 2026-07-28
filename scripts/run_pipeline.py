"""Minimal runnable entrypoint; replace its body with the team's pipeline."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.common.paths import FIGURE_DIR, METRIC_DIR, TABLE_DIR  # noqa: E402


def main() -> None:
    """Create stable output directories and report the next implementation step."""
    for path in (FIGURE_DIR, TABLE_DIR, METRIC_DIR):
        path.mkdir(parents=True, exist_ok=True)
    print("Pipeline scaffold is ready. Add explicit data inputs and model steps here.")


if __name__ == "__main__":
    main()

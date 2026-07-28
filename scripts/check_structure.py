"""Check that the minimum mathematical-modeling repository structure exists."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "requirements.txt",
    "data/README.md",
    "data/raw/README.md",
    "data/interim/README.md",
    "data/processed/README.md",
    "notebooks/README.md",
    "src/README.md",
    "outputs/README.md",
    "outputs/figures/README.md",
    "outputs/tables/README.md",
    "outputs/metrics/README.md",
    "paper/README.md",
    "references/README.md",
    "team_notes/README.md",
    "tests/README.md",
    "decision_log.md",
    "ai_usage_log.md",
    "templates/01_individual_problem_analysis.md",
    "templates/02_team_problem_tree.md",
    "templates/03_meeting_notes.md",
    "templates/04_handoff.md",
    "docs/first-two-hours.md",
    "docs/submission-checklist.md",
    "paper/main.tex",
    "paper/reference.bib",
    "paper/symbols.md",
    "paper/figures_manifest.md",
    "scripts/run_pipeline.py",
    "src/common/paths.py",
    "tests/test_repository.py",
]


missing = [path for path in REQUIRED if not (ROOT / path).exists()]
if missing:
    raise SystemExit("Missing required paths:\n- " + "\n- ".join(missing))

print(f"Repository structure check passed: {len(REQUIRED)} required paths found.")

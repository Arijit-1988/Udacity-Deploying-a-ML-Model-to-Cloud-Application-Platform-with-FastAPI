"""Run local project checks in one command.

Sequence:
1) Train model artifacts
2) Run pytest
3) Run flake8
4) Run sanitycheck
"""

from __future__ import annotations

import subprocess
import sys


def run_step(title: str, args: list[str]) -> None:
    print(f"\n==> {title}")
    print("$", " ".join(args))
    completed = subprocess.run(args, check=False)
    if completed.returncode != 0:
        raise SystemExit(completed.returncode)


def main() -> None:
    python = sys.executable
    run_step("Train model", [python, "-m", "starter.ml.train_model"])
    run_step("Run tests", [python, "-m", "pytest", "-q"])
    run_step("Run flake8", [python, "-m", "flake8"])
    run_step("Run sanitycheck", [python, "-m", "starter.sanitycheck"])
    print("\nAll local checks passed.")


if __name__ == "__main__":
    main()

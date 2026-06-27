"""
Athena Entry Point.
"""

from pathlib import Path

from src.pipeline import Runner


def main() -> None:
    """
    Run Athena.
    """

    runner = Runner(
        candidate_path=Path("data/raw/candidates.json"),
        job_path=Path("data/raw/job_description.json"),
        output_directory=Path("outputs/submissions"),
    )

    runner.run()


if __name__ == "__main__":
    main()
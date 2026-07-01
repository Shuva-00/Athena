"""
Athena Entry Point.
"""

from pathlib import Path

from src.config import settings
from src.pipeline import Runner


def main() -> None:
    """
    Run Athena.
    """

    runner = Runner(
        candidate_path=Path(settings.paths.input.candidates),
        job_path=Path(settings.paths.input.job_description),
        output_directory=Path(settings.paths.output.submission_directory),
    )

    runner.run()


if __name__ == "__main__":
    main()
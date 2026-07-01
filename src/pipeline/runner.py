"""
Project : Athena
Module  : Pipeline Runner

Purpose
-------
High-level interface for executing the complete Athena pipeline.

Guidelines
----------
- Thin orchestration layer.
- No business logic.
- No ranking logic.
"""

from __future__ import annotations

from pathlib import Path

from src.pipeline.pipeline import Pipeline


class Runner:
    """
    Executes the complete Athena pipeline.
    """

    def __init__(
        self,
        candidate_path: str | Path,
        job_path: str | Path,
        output_directory: str | Path,
    ) -> None:
        """
        Initialize the pipeline runner.
        """

        self.pipeline = Pipeline(
            candidate_path=Path(candidate_path),
            job_path=Path(job_path),
            output_directory=Path(output_directory),
        )

    ###########################################################################
    # Execute
    ###########################################################################

    def run(self) -> None:
        """
        Execute the complete pipeline.
        """

        self.pipeline.run()

    ###########################################################################
    # Benchmark
    ###########################################################################

    @property
    def benchmark(self):
        """
        Return benchmark statistics.
        """

        return self.pipeline.benchmark_result


###############################################################################
# END OF FILE
###############################################################################
"""
Project : Athena
Module  : Submission Writer

Purpose
-------
Writes validated submission rows to the official CSV format.

Guidelines
----------
- No validation.
- No ranking.
- No formatting.
- Writes UTF-8 CSV only.
"""

from __future__ import annotations

import csv
from pathlib import Path

from src.core import SubmissionRow


class Writer:
    """
    Writes submission rows to a CSV file.
    """

    HEADER = [
        "candidate_id",
        "rank",
        "score",
        "reasoning",
    ]

    def write(
        self,
        rows: list[SubmissionRow],
        output_path: str | Path,
    ) -> None:
        """
        Write submission rows to CSV.
        """

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_path.open(
            mode="w",
            encoding="utf-8",
            newline="",
        ) as file:

            writer = csv.writer(file)

            ###################################################################
            # Header
            ###################################################################

            writer.writerow(self.HEADER)

            ###################################################################
            # Data
            ###################################################################

            for row in sorted(
                rows,
                key=lambda row: row.rank,
            ):

                writer.writerow(
                    [
                        row.candidate_id,
                        row.rank,
                        f"{row.score:.6f}",
                        row.reasoning,
                    ]
                )


###############################################################################
# END OF FILE
###############################################################################
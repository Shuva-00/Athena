"""
Project : Athena
Module  : Submission Generator

Purpose
-------
Generates the final ranked submission file.

Guidelines
----------
- No ranking logic.
- No scoring logic.
- Pure output generation.
"""

from __future__ import annotations

import csv
from pathlib import Path

from src.core.candidate.entity import Candidate


class SubmissionGenerator:
    """
    Generates submission CSV files.
    """

    ###########################################################################
    # Public API
    ###########################################################################

    def generate(
        self,
        candidates: list[Candidate],
        output_path: str | Path,
    ) -> Path:

        output_path = Path(output_path)

        output_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with output_path.open(
            "w",
            newline="",
            encoding="utf-8",
        ) as csv_file:

            writer = csv.writer(csv_file)

            writer.writerow(
                [
                    "candidate_id",
                    "rank",
                    "final_score",
                    "reason",
                ]
            )

            for candidate in candidates:

                writer.writerow(
                    [
                        candidate.candidate_id,
                        candidate.scores.rank,
                        round(
                            candidate.scores.final_score,
                            6,
                        ),
                        candidate.reason,
                    ]
                )

        return output_path
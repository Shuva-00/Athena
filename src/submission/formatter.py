"""
Project : Athena
Module  : Submission Formatter

Purpose
-------
Converts ranked candidates into submission rows.

Guidelines
----------
- No file writing.
- No validation.
- No sorting.
- Assumes candidates are already ranked.
"""

from __future__ import annotations

from src.core import Candidate
from src.core import SubmissionRow


class Formatter:
    """
    Converts ranked candidates into submission rows.
    """

    def format(
        self,
        candidates: list[Candidate],
    ) -> list[SubmissionRow]:
        """
        Convert ranked candidates into submission rows.
        """

        submission_rows: list[SubmissionRow] = []

        for candidate in candidates:

            if candidate.scores.rank is None:
                raise ValueError(
                    f"Candidate {candidate.candidate_id} has no assigned rank."
                )

            submission_rows.append(
                SubmissionRow(
                    candidate_id=candidate.candidate_id,
                    rank=candidate.scores.rank,
                    score=candidate.scores.final_score,
                    reasoning=candidate.reason or "",
                )
            )

        return submission_rows


###############################################################################
# END OF FILE
###############################################################################
"""
Project : Athena
Module  : Submission Validator

Purpose
-------
Validates submission rows before writing the final CSV.

Guidelines
----------
- No file I/O.
- Raises descriptive exceptions.
- Mirrors the official submission specification.
"""

from __future__ import annotations

import re

from src.core import SubmissionRow


class Validator:
    """
    Validates submission rows.
    """

    CANDIDATE_PATTERN = re.compile(
        r"^CAND_[0-9]{7}$"
    )

    EXPECTED_ROWS = 100

    def validate(
        self,
        rows: list[SubmissionRow],
    ) -> None:
        """
        Validate submission rows.
        """

        self._validate_row_count(rows)
        self._validate_candidate_ids(rows)
        self._validate_ranks(rows)
        self._validate_scores(rows)

    ###########################################################################
    # Row Count
    ###########################################################################

    def _validate_row_count(
        self,
        rows: list[SubmissionRow],
    ) -> None:

        if len(rows) != self.EXPECTED_ROWS:
            raise ValueError(
                f"Submission must contain exactly "
                f"{self.EXPECTED_ROWS} rows."
            )

    ###########################################################################
    # Candidate IDs
    ###########################################################################

    def _validate_candidate_ids(
        self,
        rows: list[SubmissionRow],
    ) -> None:

        seen: set[str] = set()

        for row in rows:

            if not self.CANDIDATE_PATTERN.fullmatch(
                row.candidate_id
            ):
                raise ValueError(
                    f"Invalid candidate_id: "
                    f"{row.candidate_id}"
                )

            if row.candidate_id in seen:
                raise ValueError(
                    f"Duplicate candidate_id: "
                    f"{row.candidate_id}"
                )

            seen.add(row.candidate_id)

    ###########################################################################
    # Ranks
    ###########################################################################

    def _validate_ranks(
        self,
        rows: list[SubmissionRow],
    ) -> None:

        ranks = sorted(
            row.rank
            for row in rows
        )

        expected = list(
            range(
                1,
                self.EXPECTED_ROWS + 1,
            )
        )

        if ranks != expected:
            raise ValueError(
                "Ranks must contain every value "
                "from 1 to 100 exactly once."
            )

    ###########################################################################
    # Scores
    ###########################################################################

    def _validate_scores(
        self,
        rows: list[SubmissionRow],
    ) -> None:

        ordered = sorted(
            rows,
            key=lambda row: row.rank,
        )

        #######################################################################
        # Monotonic Scores
        #######################################################################

        for previous, current in zip(
            ordered,
            ordered[1:],
        ):

            if previous.score < current.score:
                raise ValueError(
                    "Scores must be monotonically "
                    "non-increasing."
                )

        #######################################################################
        # Tie Breaking
        #######################################################################

        for previous, current in zip(
            ordered,
            ordered[1:],
        ):

            if (
                previous.score == current.score
                and previous.candidate_id >
                current.candidate_id
            ):
                raise ValueError(
                    "Equal scores must be ordered "
                    "by candidate_id ascending."
                )


###############################################################################
# END OF FILE
###############################################################################
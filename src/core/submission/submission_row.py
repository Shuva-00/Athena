"""
Project : Athena
Module  : Submission Row

Purpose
-------
Represents one row of the final competition submission.

Guidelines
----------
- Pure domain model.
- No business logic.
- Mirrors the official submission specification.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class SubmissionRow(AthenaModel):
    """
    Represents one submission entry.
    """

    candidate_id: str = Field(
        ...,
        description="Candidate identifier.",
    )

    rank: int = Field(
        ...,
        ge=1,
        le=100,
        description="Candidate rank.",
    )

    score: float = Field(
        ...,
        ge=0.0,
        description="Final ranking score.",
    )

    reasoning: str = Field(
        default="",
        description="Explanation for the candidate ranking.",
    )


###############################################################################
# END OF FILE
###############################################################################
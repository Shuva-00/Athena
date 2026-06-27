"""
Project : Athena
Module  : Candidate Languages

Purpose
-------
Defines languages known by a candidate.

Guidelines
----------
- Represents one language.
- Pure domain model.
- No business logic.
- No scoring logic.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class Language(AthenaModel):
    """
    Represents one language known by a candidate.
    """

    name: str = Field(
        ...,
        min_length=1,
        description="Language name.",
    )

    proficiency: str | None = Field(
        default=None,
        description="Language proficiency if available.",
    )


###############################################################################
# END OF FILE
###############################################################################
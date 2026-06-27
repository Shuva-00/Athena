"""
Project : Athena
Module  : Candidate Skills

Purpose
-------
Defines normalized skills possessed by a candidate.

Guidelines
----------
- Represents one normalized skill.
- Pure domain model.
- No ranking logic.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class Skill(AthenaModel):
    """
    Represents one candidate skill.
    """

    name: str = Field(
        ...,
        min_length=1,
        description="Normalized skill name.",
    )

    category: str | None = Field(
        default=None,
        description="Skill category (Programming, Cloud, Database, etc.).",
    )

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Confidence that the candidate possesses this skill.",
    )


###############################################################################
# END OF FILE
###############################################################################
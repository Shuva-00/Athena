"""
Project : Athena
Module  : Candidate Education

Purpose
-------
Defines one educational qualification of a candidate.
"""

from __future__ import annotations

from pydantic import Field

from src.core.enums import InstitutionTier
from src.core.model import AthenaModel


class Education(AthenaModel):
    """
    Represents one educational qualification.
    """

    institution: str = Field(
        ...,
        min_length=1,
        description="Institution or university name.",
    )

    degree: str = Field(
        ...,
        min_length=1,
        description="Degree earned.",
    )

    field_of_study: str = Field(
        ...,
        min_length=1,
        description="Major or specialization.",
    )

    start_year: int = Field(
        ...,
        ge=1970,
        le=2035,
        description="Education start year.",
    )

    end_year: int = Field(
        ...,
        ge=1970,
        le=2035,
        description="Education completion year.",
    )

    grade: str | None = Field(
        default=None,
        description="CGPA, GPA or percentage.",
    )

    tier: InstitutionTier = Field(
        default=InstitutionTier.UNKNOWN,
        description="Institution tier.",
    )


###############################################################################
# END OF FILE
###############################################################################
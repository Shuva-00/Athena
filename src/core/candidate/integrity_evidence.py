"""
Project : Athena
Module  : Integrity Evidence

Purpose
-------
Stores factual integrity evidence extracted from a candidate profile.

Guidelines
----------
- Pure domain model.
- No business logic.
- No scoring logic.
- No inference logic.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class IntegrityEvidence(AthenaModel):
    """
    Stores resume integrity evidence.
    """

    ###########################################################################
    # Consistency
    ###########################################################################

    missing_required_fields: int = Field(
        default=0,
        ge=0,
    )

    duplicate_skills: int = Field(
        default=0,
        ge=0,
    )

    duplicate_certifications: int = Field(
        default=0,
        ge=0,
    )

    timeline_inconsistencies: int = Field(
        default=0,
        ge=0,
    )

    experience_inconsistencies: int = Field(
        default=0,
        ge=0,
    )
    duplicate_projects: int = Field(
    default=0,
    ge=0,
)
    ###########################################################################
    # Confidence
    ###########################################################################

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    ###########################################################################
    # Explainability
    ###########################################################################

    strengths: list[str] = Field(
        default_factory=list,
    )

    concerns: list[str] = Field(
        default_factory=list,
    )


###############################################################################
# END OF FILE
###############################################################################
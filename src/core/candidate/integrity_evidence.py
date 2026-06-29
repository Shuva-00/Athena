"""
Project : Athena
Module  : Integrity Evidence
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class IntegrityEvidence(AthenaModel):
    """
    Stores resume integrity evidence.
    """

    ###########################################################################
    # Resume Validation
    ###########################################################################

    unsupported_skills: list[str] = Field(
        default_factory=list,
    )

    timeline_conflicts: list[str] = Field(
        default_factory=list,
    )

    keyword_stuffing_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    ###########################################################################
    # Consistency
    ###########################################################################

    career_consistency_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
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
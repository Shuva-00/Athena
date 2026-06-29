"""
Project : Athena
Module  : Signal Evidence
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class SignalEvidence(AthenaModel):
    """
    Stores recruiter-facing candidate signals.
    """

    ###########################################################################
    # Availability
    ###########################################################################

    availability_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    ###########################################################################
    # Assessment
    ###########################################################################

    assessment_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    ###########################################################################
    # Engagement
    ###########################################################################

    github_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    linkedin_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    portfolio_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    ###########################################################################
    # Responsiveness
    ###########################################################################

    responsiveness_score: float = Field(
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
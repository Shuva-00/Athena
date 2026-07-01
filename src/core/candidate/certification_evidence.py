"""
Project : Athena
Module  : Certification Evidence
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class CertificationEvidence(AthenaModel):
    """
    Stores certification-related evidence.
    """

    ###########################################################################
    # Matching
    ###########################################################################

    matched_certifications: list[str] = Field(
        default_factory=list,
    )

    missing_certifications: list[str] = Field(
        default_factory=list,
    )

    ###########################################################################
    # Statistics
    ###########################################################################

    total_certifications: int = Field(
        default=0,
        ge=0,
    )

    matched_total: int = Field(
        default=0,
        ge=0,
    )

    ###########################################################################
    # Quality
    ###########################################################################

    recent_certifications: int = Field(
        default=0,
        ge=0,
    )

    certification_relevance: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )
    semantic_similarity: float = Field(
    default=0.0,
    ge=0.0,
    le=1.0,
)

    verified_count: int = Field(
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
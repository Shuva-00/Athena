"""
Project : Athena
Module  : Candidate Features

Purpose
-------
Stores normalized feature scores computed from candidate evidence.

Guidelines
----------
- No business logic.
- All values normalized to [0, 1].
- Produced by FeatureScorer.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class CandidateFeatures(AthenaModel):
    """
    Normalized feature scores.
    """

    ###########################################################################
    # Evidence Scores
    ###########################################################################

    skill_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    experience_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    education_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    certification_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    signal_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    integrity_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    ###########################################################################
    # Semantic Scores
    ###########################################################################

    semantic_skill_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    semantic_title_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    semantic_responsibility_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )

    ###########################################################################
    # Confidence
    ###########################################################################

    confidence_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )
    
    ###########################################################################
    # Final
    ###########################################################################

    feature_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
    )
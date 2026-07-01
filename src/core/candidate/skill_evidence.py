"""
Project : Athena
Module  : Skill Evidence

Purpose
-------
Stores all factual evidence extracted about candidate skills.

Guidelines
----------
- Pure domain model.
- No business logic.
- No scoring logic.
- No inference logic.
- Stores evidence only.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class SkillEvidence(AthenaModel):
    """
    Stores all skill-related evidence collected during feature extraction.
    """

    ###########################################################################
    # Skill Matching
    ###########################################################################

    candidate_total: int = Field(
        default=0,
        ge=0,
        description="Total number of candidate skills.",
    )

    required_total: int = Field(
        default=0,
        ge=0,
        description="Total number of required job skills.",
    )

    exact_matches: int = Field(
        default=0,
        ge=0,
        description="Number of exact skill matches.",
    )

    missing_required: list[str] = Field(
        default_factory=list,
        description="Required skills missing from the candidate profile.",
    )

    additional_skills: list[str] = Field(
        default_factory=list,
        description="Candidate skills beyond the job requirements.",
    )

    matched_skills: list[str] = Field(
        default_factory=list,
        description="Skills matched with the job description.",
    )

    ###########################################################################
    # Skill Proficiency
    ###########################################################################


    ###########################################################################
    # Experience
    ###########################################################################

    total_duration_months: int = Field(
        default=0,
        ge=0,
        description="Total months of experience across matched skills.",
    )

    average_duration_months: float = Field(
        default=0.0,
        ge=0.0,
        description="Average months of experience per matched skill.",
    )

    maximum_duration_months: int = Field(
        default=0,
        ge=0,
        description="Maximum experience for any matched skill.",
    )

    ###########################################################################
    # Validation
    ###########################################################################

    total_endorsements: int = Field(
        default=0,
        ge=0,
        description="Total endorsements across matched skills.",
    )

    average_endorsements: float = Field(
        default=0.0,
        ge=0.0,
        description="Average endorsements per matched skill.",
    )

    maximum_endorsements: int = Field(
        default=0,
        ge=0,
        description="Maximum endorsements for a matched skill.",
    )

    ###########################################################################
    # Semantic Matching
    ###########################################################################

    semantic_similarity: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Semantic similarity between candidate skills and required skills.",
    )

    ###########################################################################
    # Confidence
    ###########################################################################

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence in extracted skill evidence.",
    )

    ###########################################################################
    # Explainability
    ###########################################################################

    strengths: list[str] = Field(
        default_factory=list,
        description="Skill-related strengths supporting the ranking.",
    )

    concerns: list[str] = Field(
        default_factory=list,
        description="Skill-related concerns affecting the ranking.",
    )
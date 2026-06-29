"""
Project : Athena
Module  : Experience Evidence

Purpose
-------
Stores all factual evidence extracted from a candidate's professional
experience.

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


class ExperienceEvidence(AthenaModel):
    """
    Stores experience-related evidence collected during feature extraction.
    """

    ###########################################################################
    # Overall Experience
    ###########################################################################

    total_experience_months: int = Field(
        default=0,
        ge=0,
        description="Total professional experience in months.",
    )

    relevant_experience_months: int = Field(
        default=0,
        ge=0,
        description="Relevant experience matching the job description.",
    )

    recent_experience_months: int = Field(
        default=0,
        ge=0,
        description="Recent relevant experience.",
    )

    ###########################################################################
    # Career Progression
    ###########################################################################

    career_progression_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Normalized career progression score.",
    )

    leadership_experience_months: int = Field(
        default=0,
        ge=0,
        description="Leadership or management experience.",
    )

    ###########################################################################
    # Employment Quality
    ###########################################################################

    company_relevance_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Relevance of companies to the target role.",
    )

    stability_score: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Employment stability score.",
    )

    employment_gap_months: int = Field(
        default=0,
        ge=0,
        description="Total employment gaps in months.",
    )

    ###########################################################################
    # Technical Relevance
    ###########################################################################

    relevant_projects: list[str] = Field(
        default_factory=list,
        description="Projects supporting relevant experience.",
    )

    relevant_roles: list[str] = Field(
        default_factory=list,
        description="Relevant job titles.",
    )

    relevant_domains: list[str] = Field(
        default_factory=list,
        description="Relevant business domains.",
    )

    ###########################################################################
    # Semantic Matching
    ###########################################################################

    semantic_title_similarity: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Semantic similarity between candidate titles and target role.",
    )

    semantic_responsibility_similarity: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Semantic similarity between responsibilities.",
    )

    ###########################################################################
    # Confidence
    ###########################################################################

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence in extracted experience evidence.",
    )

    ###########################################################################
    # Explainability
    ###########################################################################

    strengths: list[str] = Field(
        default_factory=list,
        description="Experience strengths supporting the ranking.",
    )

    concerns: list[str] = Field(
        default_factory=list,
        description="Experience concerns affecting the ranking.",
    )
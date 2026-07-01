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
    # Experience Statistics
    ###########################################################################

    total_experience_months: int = Field(
        default=0,
        ge=0,
        description="Total professional experience in months.",
    )

    relevant_experience_months: int = Field(
        default=0,
        ge=0,
        description="Experience relevant to the target job.",
    )

    current_role_months: int = Field(
        default=0,
        ge=0,
        description="Duration of the candidate's current role.",
    )

    total_roles: int = Field(
        default=0,
        ge=0,
        description="Total number of professional roles.",
    )

    relevant_role_count: int = Field(
        default=0,
        ge=0,
        description="Number of roles relevant to the target position.",
    )

    ###########################################################################
    # Employment Statistics
    ###########################################################################

    employment_gap_months: int = Field(
        default=0,
        ge=0,
        description="Total employment gap duration in months.",
    )

    average_tenure_months: float = Field(
        default=0.0,
        ge=0.0,
        description="Average tenure per role in months.",
    )

    longest_tenure_months: int = Field(
        default=0,
        ge=0,
        description="Longest continuous employment duration.",
    )

    shortest_tenure_months: int = Field(
        default=0,
        ge=0,
        description="Shortest employment duration.",
    )

    ###########################################################################
    # Career Intelligence Evidence
    ###########################################################################

    career_progression_steps: int = Field(
        default=0,
        ge=0,
        description="Number of observed career progression steps.",
    )

    title_progression_steps: int = Field(
        default=0,
        ge=0,
        description="Number of observed title progression steps.",
    )

    leadership_experience_months: int = Field(
        default=0,
        ge=0,
        description="Leadership or management experience in months.",
    )

    leadership_role_count: int = Field(
        default=0,
        ge=0,
        description="Number of leadership roles held.",
    )

    relevant_company_count: int = Field(
        default=0,
        ge=0,
        description="Number of companies relevant to the target domain.",
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
        description="Relevant industries or business domains.",
    )

    ###########################################################################
    # Semantic Evidence
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
        description="Semantic similarity between responsibilities and job requirements.",
    )

    ###########################################################################
    # Extraction Confidence
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


###############################################################################
# END OF FILE
###############################################################################
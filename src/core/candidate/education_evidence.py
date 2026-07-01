"""
Project : Athena
Module  : Education Evidence

Purpose
-------
Stores all factual evidence extracted from a candidate's educational
background.

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

from src.core.enums import DegreeLevel
from src.core.enums import InstitutionTier
from src.core.model import AthenaModel


class EducationEvidence(AthenaModel):
    """
    Stores education-related evidence collected during feature extraction.
    """

    ###########################################################################
    # Degree Information
    ###########################################################################

    total_degrees: int = Field(
        default=0,
        ge=0,
        description="Total number of educational qualifications.",
    )

    highest_degree: DegreeLevel | None = Field(
        default=None,
        description="Highest degree attained by the candidate.",
    )

    minimum_degree_met: bool = Field(
        default=False,
        description="Whether the minimum degree requirement is satisfied.",
    )

    relevant_degree_count: int = Field(
        default=0,
        ge=0,
        description="Number of degrees relevant to the target role.",
    )

    relevant_degrees: list[str] = Field(
        default_factory=list,
        description="Relevant degrees supporting the application.",
    )

    ###########################################################################
    # Academic Performance
    ###########################################################################

    highest_cgpa: float | None = Field(
        default=None,
        ge=0.0,
        description="Highest CGPA/GPA achieved.",
    )

    average_cgpa: float | None = Field(
        default=None,
        ge=0.0,
        description="Average CGPA/GPA across all qualifications.",
    )

    ###########################################################################
    # Institution
    ###########################################################################

    institution_tier: InstitutionTier = Field(
        default=InstitutionTier.UNKNOWN,
        description="Highest institution tier attended.",
    )

    relevant_institution_count: int = Field(
        default=0,
        ge=0,
        description="Number of institutions relevant to the job.",
    )

    ###########################################################################
    # Coursework
    ###########################################################################

    relevant_courses: list[str] = Field(
        default_factory=list,
        description="Relevant coursework supporting the job requirements.",
    )

    ###########################################################################
    # Research
    ###########################################################################

    research_project_count: int = Field(
        default=0,
        ge=0,
        description="Number of research projects.",
    )

    research_publication_count: int = Field(
        default=0,
        ge=0,
        description="Number of research publications.",
    )

    ###########################################################################
    # Semantic Matching
    ###########################################################################

    semantic_similarity: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Semantic similarity between education and job requirements.",
    )

    ###########################################################################
    # Confidence
    ###########################################################################

    confidence: float = Field(
        default=0.0,
        ge=0.0,
        le=1.0,
        description="Confidence in extracted education evidence.",
    )

    ###########################################################################
    # Explainability
    ###########################################################################

    strengths: list[str] = Field(
        default_factory=list,
        description="Education strengths supporting the ranking.",
    )

    concerns: list[str] = Field(
        default_factory=list,
        description="Education concerns affecting the ranking.",
    )


###############################################################################
# END OF FILE
###############################################################################
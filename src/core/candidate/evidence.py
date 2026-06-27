"""
Project : Athena
Module  : Candidate Evidence

Purpose
-------
Stores all factual evidence gathered during retrieval and ranking
that is later used to generate explainable reasoning.

Guidelines
----------
- Pure domain model.
- No business logic.
- No inference logic.
- Stores evidence only.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class EvidenceCollection(AthenaModel):
    """
    Stores explainability evidence for a candidate.
    """

    ###########################################################################
    # Raw Evidence
    ###########################################################################

    facts: list[str] = Field(
        default_factory=list,
        description="Raw factual evidence extracted from the candidate profile.",
    )

    ###########################################################################
    # Skill Evidence
    ###########################################################################

    matched_skills: list[str] = Field(
        default_factory=list,
        description="Skills matching the job requirements.",
    )

    missing_skills: list[str] = Field(
        default_factory=list,
        description="Required skills missing from the candidate profile.",
    )

    ###########################################################################
    # Technology Evidence
    ###########################################################################

    matched_technologies: list[str] = Field(
        default_factory=list,
        description="Technologies matching the job description.",
    )

    missing_technologies: list[str] = Field(
        default_factory=list,
        description="Technologies required but not found.",
    )

    ###########################################################################
    # Certification Evidence
    ###########################################################################

    matched_certifications: list[str] = Field(
        default_factory=list,
        description="Matching certifications.",
    )

    missing_certifications: list[str] = Field(
        default_factory=list,
        description="Required certifications not present.",
    )

    ###########################################################################
    # Education Evidence
    ###########################################################################

    education_matches: list[str] = Field(
        default_factory=list,
        description="Relevant education matches.",
    )

    ###########################################################################
    # Experience Evidence
    ###########################################################################

    relevant_experiences: list[str] = Field(
        default_factory=list,
        description="Relevant work experiences supporting the ranking.",
    )

    relevant_projects: list[str] = Field(
        default_factory=list,
        description="Projects supporting the ranking.",
    )

    ###########################################################################
    # Explainability
    ###########################################################################

    strengths: list[str] = Field(
        default_factory=list,
        description="Candidate strengths identified during analysis.",
    )

    weaknesses: list[str] = Field(
        default_factory=list,
        description="Candidate weaknesses identified during analysis.",
    )

    risks: list[str] = Field(
        default_factory=list,
        description="Potential hiring risks.",
    )

    
###############################################################################
# END OF FILE
###############################################################################
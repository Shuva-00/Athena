"""
Project : Athena
Module  : Candidate Entity

Purpose
-------
Defines the aggregate root representing a normalized candidate
within the Athena ranking pipeline.

Guidelines
----------
- Aggregate root of the Candidate domain.
- Composes all candidate-related domain models.
- Contains no business logic.
"""

from __future__ import annotations

from typing import Any

from pydantic import Field

from src.core.model import AthenaModel
from src.core.candidate.profile import CandidateProfile
from src.core.candidate.education import Education
from src.core.candidate.experiences import Experience
from src.core.candidate.projects import Project
from src.core.candidate.skills import Skill
from src.core.candidate.certifications import Certification
from src.core.candidate.languages import Language
from src.core.candidate.signals import CandidateSignals
from src.core.candidate.scores import CandidateScores
from src.core.candidate.evidence import EvidenceCollection
from src.core.candidate.features import CandidateFeatures

class Candidate(AthenaModel):
    """
    Aggregate root representing one normalized candidate.
    """

    candidate_id: str = Field(
        ...,
        description="Unique candidate identifier.",
    )

    profile: CandidateProfile = Field(
        ...,
        description="Candidate profile information.",
    )

    education: list[Education] = Field(
        default_factory=list,
        description="Educational qualifications.",
    )

    experiences: list[Experience] = Field(
        default_factory=list,
        description="Professional experiences.",
    )

    projects: list[Project] = Field(
        default_factory=list,
        description="Candidate projects.",
    )

    skills: list[Skill] = Field(
        default_factory=list,
        description="Candidate skills.",
    )

    certifications: list[Certification] = Field(
        default_factory=list,
        description="Professional certifications.",
    )

    languages: list[Language] = Field(
        default_factory=list,
        description="Languages known.",
    )

    signals: CandidateSignals | None = Field(
    default=None,
    description="Candidate signals and inferred attributes.",)
    
    features: CandidateFeatures = Field(
    default_factory=CandidateFeatures,
    description="Normalized feature scores.",
)
    scores: CandidateScores = Field(
        default_factory=CandidateScores,
        description="Candidate scores.",
    )

    evidence: EvidenceCollection = Field(
        default_factory=EvidenceCollection,
        description="Evidence supporting ranking decisions.",
    )
    reason: str | None = Field(
    default=None,
    description="Generated explanation for the candidate ranking.",
)
    metadata: dict[str, Any] = Field(
        default_factory=dict,
        description="Internal metadata.",
    )


###############################################################################
# END OF FILE
###############################################################################
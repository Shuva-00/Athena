"""
Project : Athena
Module  : Evidence Collection

Purpose
-------
Aggregates all evidence models for a candidate.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel

from src.core.candidate.skill_evidence import SkillEvidence
from src.core.candidate.experience_evidence import ExperienceEvidence
from src.core.candidate.education_evidence import EducationEvidence
from src.core.candidate.certification_evidence import CertificationEvidence
from src.core.candidate.signal_evidence import SignalEvidence
from src.core.candidate.integrity_evidence import IntegrityEvidence
class EvidenceCollection(AthenaModel):
    """
    Aggregate root for all candidate evidence.
    """

    skill: SkillEvidence = Field(
        default_factory=SkillEvidence,
    )

    experience: ExperienceEvidence = Field(
        default_factory=ExperienceEvidence,
    )

    education: EducationEvidence = Field(
        default_factory=EducationEvidence,
    )

    certification: CertificationEvidence = Field(
        default_factory=CertificationEvidence,
    )

    signal: SignalEvidence = Field(
        default_factory=SignalEvidence,
    )

    integrity: IntegrityEvidence = Field(
        default_factory=IntegrityEvidence,
    )
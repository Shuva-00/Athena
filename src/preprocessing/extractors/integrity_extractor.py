"""
Project : Athena
Module  : Integrity Extractor

Purpose
-------
Extracts factual integrity evidence from a candidate profile.

Guidelines
----------
- No scoring.
- No ranking.
- No weighting.
- Populates IntegrityEvidence only.
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate
from src.core.candidate.integrity_evidence import IntegrityEvidence
from src.core.job.job_description import JobDescription

from .base_extractor import BaseExtractor


class IntegrityExtractor(BaseExtractor):
    """
    Extracts integrity-related evidence.
    """

    ###########################################################################
    # Public API
    ###########################################################################

    def extract(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> IntegrityEvidence:

        evidence = IntegrityEvidence()

        self._extract_missing_fields(
            candidate,
            evidence,
        )

        self._extract_duplicate_skills(
            candidate,
            evidence,
        )

        self._extract_duplicate_certifications(
            candidate,
            evidence,
        )

        self._extract_timeline_consistency(
            candidate,
            evidence,
        )

        self._extract_experience_consistency(
            candidate,
            evidence,
        )

        self._extract_confidence(
            candidate,
            evidence,
        )

        candidate.evidence.integrity = evidence

        return evidence

    ###########################################################################
    # Missing Fields
    ###########################################################################

    def _extract_missing_fields(
        self,
        candidate: Candidate,
        evidence: IntegrityEvidence,
    ) -> None:

        if not candidate.profile.full_name:
            evidence.missing_required_fields += 1

        if not candidate.profile.email:
            evidence.missing_required_fields += 1

        if len(candidate.experiences) == 0:
            evidence.missing_required_fields += 1

    ###########################################################################
    # Duplicate Skills
    ###########################################################################

    def _extract_duplicate_skills(
        self,
        candidate: Candidate,
        evidence: IntegrityEvidence,
    ) -> None:

        seen = set()

        for skill in candidate.skills:

            key = skill.name.strip().lower()

            if key in seen:
                evidence.duplicate_skills += 1

            else:
                seen.add(key)

    ###########################################################################
    # Duplicate Certifications
    ###########################################################################

    def _extract_duplicate_certifications(
        self,
        candidate: Candidate,
        evidence: IntegrityEvidence,
    ) -> None:

        seen = set()

        for certification in candidate.certifications:

            key = certification.name.strip().lower()

            if key in seen:
                evidence.duplicate_certifications += 1

            else:
                seen.add(key)

    ###########################################################################
    # Timeline Consistency
    ###########################################################################

    def _extract_timeline_consistency(
        self,
        candidate: Candidate,
        evidence: IntegrityEvidence,
    ) -> None:

        for experience in candidate.experiences:

            if (
                experience.start_date is not None
                and
                experience.end_date is not None
                and
                experience.end_date < experience.start_date
            ):
                evidence.timeline_inconsistencies += 1

            if (
                experience.is_current
                and
                experience.end_date is not None
            ):
                evidence.timeline_inconsistencies += 1

    ###########################################################################
    # Experience Consistency
    ###########################################################################

    def _extract_experience_consistency(
        self,
        candidate: Candidate,
        evidence: IntegrityEvidence,
    ) -> None:

        for experience in candidate.experiences:

            if (
                experience.duration_months is not None
                and
                experience.duration_months < 0
            ):
                evidence.experience_inconsistencies += 1

    ###########################################################################
    # Confidence
    ###########################################################################

    def _extract_confidence(
        self,
        candidate: Candidate,
        evidence: IntegrityEvidence,
    ) -> None:

        issues = (

            evidence.missing_required_fields

            + evidence.duplicate_skills

            + evidence.duplicate_certifications

            + evidence.timeline_inconsistencies

            + evidence.experience_inconsistencies

        )

        evidence.confidence = max(
            0.0,
            1.0 - (issues * 0.10),
        )
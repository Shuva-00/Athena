"""
Project : Athena
Module  : Certification Extractor

Purpose
-------
Extracts factual certification evidence from a candidate profile.

Guidelines
----------
- No scoring.
- No ranking.
- No weighting.
- No inference.
- Populates CertificationEvidence only.
"""

from __future__ import annotations

from datetime import date

from src.core.candidate.certification_evidence import (
    CertificationEvidence,
)
from src.core.candidate.entity import Candidate
from src.core.job.job_description import JobDescription

from .base_extractor import BaseExtractor


class CertificationExtractor(BaseExtractor):
    """
    Extracts certification-related evidence.
    """

    ###########################################################################
    # Public API
    ###########################################################################

    def extract(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> CertificationEvidence:

        evidence = CertificationEvidence()

        self._extract_matching(
            candidate,
            job,
            evidence,
        )

        self._extract_statistics(
            candidate,
            evidence,
        )

        self._extract_recency(
            candidate,
            evidence,
        )

        self._extract_verification(
            candidate,
            evidence,
        )

        self._extract_semantic_similarity(
            evidence,
        )

        self._extract_confidence(
            candidate,
            evidence,
        )

        candidate.evidence.certification = evidence

        return evidence

    ###########################################################################
    # Matching
    ###########################################################################

    def _extract_matching(
        self,
        candidate: Candidate,
        job: JobDescription,
        evidence: CertificationEvidence,
    ) -> None:

        candidate_names = {
            cert.name.strip().lower()
            for cert in candidate.certifications
        }

        required = {
            cert.strip().lower()
            for cert in job.certifications
        }

        evidence.matched_certifications = sorted(
            candidate_names & required
        )

        evidence.missing_certifications = sorted(
            required - candidate_names
        )

        evidence.matched_total = len(
            evidence.matched_certifications
        )

    ###########################################################################
    # Statistics
    ###########################################################################

    def _extract_statistics(
        self,
        candidate: Candidate,
        evidence: CertificationEvidence,
    ) -> None:

        evidence.total_certifications = len(
            candidate.certifications
        )

        if evidence.total_certifications > 0:

            evidence.certification_relevance = (
                evidence.matched_total
                / evidence.total_certifications
            )

    ###########################################################################
    # Recency
    ###########################################################################

    def _extract_recency(
        self,
        candidate: Candidate,
        evidence: CertificationEvidence,
    ) -> None:

        current_year = date.today().year

        for cert in candidate.certifications:

            if cert.issue_date is None:
                continue

            if current_year - cert.issue_date.year <= 3:
                evidence.recent_certifications += 1

    ###########################################################################
    # Verification
    ###########################################################################

    def _extract_verification(
        self,
        candidate: Candidate,
        evidence: CertificationEvidence,
    ) -> None:

        for cert in candidate.certifications:

            if cert.verified:
                evidence.verified_count += 1

    ###########################################################################
    # Future AI Components
    ###########################################################################

    def _extract_semantic_similarity(
        self,
        evidence: CertificationEvidence,
    ) -> None:

        evidence.semantic_similarity = 0.0

    def _extract_confidence(
        self,
        candidate: Candidate,
        evidence: CertificationEvidence,
    ) -> None:

        if evidence.total_certifications == 0:

            evidence.confidence = 0.0

            return

        evidence.confidence = 1.0
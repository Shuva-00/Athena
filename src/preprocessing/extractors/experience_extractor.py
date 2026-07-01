"""
Project : Athena
Module  : Experience Extractor

Purpose
-------
Extracts factual experience evidence from a candidate profile.

Guidelines
----------
- No scoring.
- No ranking.
- No weighting.
- No inference.
- Populates ExperienceEvidence only.
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate
from src.core.candidate.experience_evidence import ExperienceEvidence
from src.core.job.job_description import JobDescription

from .base_extractor import BaseExtractor


class ExperienceExtractor(BaseExtractor):
    """
    Extracts factual experience evidence.
    """

    ###########################################################################
    # Public API
    ###########################################################################

    def extract(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> ExperienceEvidence:

        evidence = ExperienceEvidence()

        self._extract_basic_statistics(
            candidate,
            evidence,
        )

        self._extract_relevant_experience(
            candidate,
            job,
            evidence,
        )

        self._extract_tenure_statistics(
            candidate,
            evidence,
        )

        self._extract_employment_gaps(
            candidate,
            evidence,
        )

        #######################################################################
        # Future Intelligence
        #######################################################################

        self._extract_career_progression(
            candidate,
            evidence,
        )

        self._extract_leadership(
            candidate,
            evidence,
        )

        self._extract_company_relevance(
            candidate,
            job,
            evidence,
        )

        self._extract_semantic_similarity(
            candidate,
            job,
            evidence,
        )

        self._extract_confidence(
            candidate,
            evidence,
        )

        candidate.evidence.experience = evidence

        return evidence

    ###########################################################################
    # Basic Statistics
    ###########################################################################

    def _extract_basic_statistics(
        self,
        candidate: Candidate,
        evidence: ExperienceEvidence,
    ) -> None:

        evidence.total_roles = len(candidate.experiences)

        durations = [
            exp.duration_months
            for exp in candidate.experiences
            if exp.duration_months is not None
        ]

        evidence.total_experience_months = sum(durations)

        for exp in candidate.experiences:
            if exp.is_current and exp.duration_months is not None:
                evidence.current_role_months = exp.duration_months
                break

    ###########################################################################
    # Relevant Experience
    ###########################################################################

    def _extract_relevant_experience(
        self,
        candidate: Candidate,
        job: JobDescription,
        evidence: ExperienceEvidence,
    ) -> None:

        required = {
            skill.lower()
            for skill in job.required_skills
        }

        for exp in candidate.experiences:

            skills = {
                skill.lower()
                for skill in exp.skills
            }

            if skills & required:

                evidence.relevant_role_count += 1

                if exp.duration_months:
                    evidence.relevant_experience_months += (
                        exp.duration_months
                    )

                evidence.relevant_roles.append(
                    exp.job_title
                )

    ###########################################################################
    # Tenure Statistics
    ###########################################################################

    def _extract_tenure_statistics(
        self,
        candidate: Candidate,
        evidence: ExperienceEvidence,
    ) -> None:

        durations = [
            exp.duration_months
            for exp in candidate.experiences
            if exp.duration_months is not None
        ]

        if not durations:
            return

        evidence.average_tenure_months = (
            sum(durations)
            / len(durations)
        )

        evidence.longest_tenure_months = max(durations)

        evidence.shortest_tenure_months = min(durations)

    ###########################################################################
    # Employment Gaps
    ###########################################################################

    def _extract_employment_gaps(
        self,
        candidate: Candidate,
        evidence: ExperienceEvidence,
    ) -> None:

        # Placeholder
        # Will compute timeline gaps in V2.

        evidence.employment_gap_months = 0

    ###########################################################################
    # Future Intelligence
    ###########################################################################

    def _extract_career_progression(
        self,
        candidate: Candidate,
        evidence: ExperienceEvidence,
    ) -> None:
        pass

    def _extract_leadership(
        self,
        candidate: Candidate,
        evidence: ExperienceEvidence,
    ) -> None:
        pass

    def _extract_company_relevance(
        self,
        candidate: Candidate,
        job: JobDescription,
        evidence: ExperienceEvidence,
    ) -> None:
        pass

    def _extract_semantic_similarity(
        self,
        candidate: Candidate,
        job: JobDescription,
        evidence: ExperienceEvidence,
    ) -> None:

        evidence.semantic_title_similarity = 0.0
        evidence.semantic_responsibility_similarity = 0.0

    def _extract_confidence(
        self,
        candidate: Candidate,
        evidence: ExperienceEvidence,
    ) -> None:

        evidence.confidence = 1.0
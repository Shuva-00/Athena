"""
Project : Athena
Module  : Skill Extractor

Purpose
-------
Extracts raw skill evidence from a candidate profile.

Guidelines
----------
- No scoring.
- No ranking.
- No weighting.
- Only evidence extraction.
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate
from src.core.candidate.skill_evidence import SkillEvidence
from src.core.job.job_description import JobDescription

from .base_extractor import BaseExtractor


class SkillExtractor(BaseExtractor):
    """
    Extracts skill-related evidence.
    """

    def extract(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> SkillEvidence:

        evidence = SkillEvidence()

        candidate_skills = self._candidate_skill_set(candidate)
        required_skills = self._required_skill_set(job)

        self._extract_basic_statistics(
            candidate_skills,
            required_skills,
            evidence,
        )

        self._extract_exact_matches(
            candidate_skills,
            required_skills,
            evidence,
        )

        self._extract_missing_required_skills(
            candidate_skills,
            required_skills,
            evidence,
        )

        # Remaining stages will be implemented later

        # self._extract_semantic_matches(...)
        # self._extract_critical_skills(...)
        # self._extract_skill_support(...)
        # self._extract_duplicate_mentions(...)
        # self._extract_rare_skills(...)

        return evidence

    ###########################################################################
    # Helpers
    ###########################################################################

    def _candidate_skill_set(
        self,
        candidate: Candidate,
    ) -> set[str]:

        return {
            skill.name.strip().lower()
            for skill in candidate.skills
            if skill.name.strip()
        }

    def _required_skill_set(
        self,
        job: JobDescription,
    ) -> set[str]:

        return {
            skill.strip().lower()
            for skill in job.required_skills
            if skill.strip()
        }

    ###########################################################################
    # Extraction
    ###########################################################################

    def _extract_basic_statistics(
        self,
        candidate_skills: set[str],
        required_skills: set[str],
        evidence: SkillEvidence,
    ) -> None:

        evidence.total_candidate_skills = len(
            candidate_skills
        )

        evidence.total_required_skills = len(
            required_skills
        )

    def _extract_exact_matches(
        self,
        candidate_skills: set[str],
        required_skills: set[str],
        evidence: SkillEvidence,
    ) -> None:

        evidence.exact_skill_matches = len(
            candidate_skills & required_skills
        )

    def _extract_missing_required_skills(
        self,
        candidate_skills: set[str],
        required_skills: set[str],
        evidence: SkillEvidence,
    ) -> None:

        evidence.missing_required_skills = len(
            required_skills - candidate_skills
        )
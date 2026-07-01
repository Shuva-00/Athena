"""
Project : Athena
Module  : Skill Extractor

Purpose
-------
Extracts factual skill evidence from a candidate profile.

Guidelines
----------
- No scoring.
- No ranking.
- No weighting.
- No inference.
- Populates SkillEvidence only.
"""

from __future__ import annotations
from src.core.candidate.skill_evidence import SkillEvidence
from src.core.job.job_description import JobDescription
from src.core.candidate.entity import Candidate
from .base_extractor import BaseExtractor


class SkillExtractor(BaseExtractor):
    """
    Extracts all skill-related evidence from a candidate profile.
    """

    ###########################################################################
    # Public API
    ###########################################################################

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

        self._extract_missing_required(
            candidate_skills,
            required_skills,
            evidence,
        )

        self._extract_additional_skills(
            candidate_skills,
            required_skills,
            evidence,
        )

        #######################################################################
        # Future Improvements
        #######################################################################

        self._extract_confidence(
            candidate,
            evidence,
        )

        self._extract_duration(
            candidate,
            evidence,
        )

        self._extract_endorsements(
            candidate,
            evidence,
        )

        self._extract_semantic_similarity(
            candidate,
            job,
            evidence,
        )

        #######################################################################
        # Store Evidence
        #######################################################################

        candidate.evidence.skill = evidence

        return evidence

    ###########################################################################
    # Candidate Skill Set
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

    ###########################################################################
    # Required Skill Set
    ###########################################################################

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

        evidence.candidate_total = len(candidate_skills)
        evidence.required_total = len(required_skills)

    def _extract_exact_matches(
        self,
        candidate_skills: set[str],
        required_skills: set[str],
        evidence: SkillEvidence,
    ) -> None:

        matches = sorted(
            candidate_skills & required_skills
        )

        evidence.exact_matches = len(matches)
        evidence.matched_skills = matches

    def _extract_missing_required(
        self,
        candidate_skills: set[str],
        required_skills: set[str],
        evidence: SkillEvidence,
    ) -> None:

        evidence.missing_required = sorted(
            required_skills - candidate_skills
        )

    def _extract_additional_skills(
        self,
        candidate_skills: set[str],
        required_skills: set[str],
        evidence: SkillEvidence,
    ) -> None:

        evidence.additional_skills = sorted(
            candidate_skills - required_skills
        )

    ###########################################################################
    # Future Evidence Extraction
    ###########################################################################


    def _extract_duration(
        self,
        candidate: Candidate,
        evidence: SkillEvidence,
    ) -> None:
        """
        Extract duration statistics for matched skills.
        """

        durations: dict[str, int] = {}

        matched = {
            skill.lower()
            for skill in evidence.matched_skills
        }

        for experience in candidate.experiences:

            if experience.duration_months is None:
                continue

            for skill in experience.skills:

                skill = skill.strip().lower()

                if skill not in matched:
                    continue

                durations.setdefault(skill, 0)

                durations[skill] += experience.duration_months

        if not durations:
           return

        values = list(durations.values())

        evidence.total_duration_months = sum(values)

        evidence.average_duration_months = (
        sum(values) / len(values)
    )

        evidence.maximum_duration_months = max(values)
    
    def _extract_confidence(
        self,
        candidate: Candidate,
        evidence: SkillEvidence,
    ) -> None:
        """
        Estimate extraction confidence from matched skills.
        """

        matched = {
            skill.lower()
            for skill in evidence.matched_skills
        }

        confidences = []

        for skill in candidate.skills:

            if skill.name.lower() in matched:
                confidences.append(skill.confidence)

        if not confidences:
            evidence.confidence = 0.0
            return

        evidence.confidence = (
            sum(confidences) / len(confidences)
    )

    def _extract_endorsements(
        self,
        candidate: Candidate,
        evidence: SkillEvidence,
    ) -> None:
        """
        Placeholder until endorsement sources are available.
        """

        evidence.total_endorsements = 0

        evidence.average_endorsements = 0.0

        evidence.maximum_endorsements = 0

    def _extract_semantic_similarity(
        self,
        candidate: Candidate,
        job: JobDescription,
        evidence: SkillEvidence,
    ) -> None:
        """
        Placeholder.

        Semantic similarity will be computed using embeddings
        after the retrieval pipeline is complete.
       """

        evidence.semantic_similarity = 0.0
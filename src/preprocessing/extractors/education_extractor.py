"""
Project : Athena
Module  : Education Extractor

Purpose
-------
Extracts factual education evidence from a candidate profile.

Guidelines
----------
- No scoring.
- No ranking.
- No weighting.
- No inference.
- Populates EducationEvidence only.
"""

from __future__ import annotations

from sympy import re


from src.core.candidate.education_evidence import EducationEvidence
from src.core.candidate.entity import Candidate
from src.core.enums import InstitutionTier
from src.core.job.job_description import JobDescription

from .base_extractor import BaseExtractor


class EducationExtractor(BaseExtractor):
    """
    Extracts factual education evidence.
    """

    ###########################################################################
    # Public API
    ###########################################################################

    def extract(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> EducationEvidence:

        evidence = EducationEvidence()

        self._extract_degree_information(
            candidate,
            job,
            evidence,
        )

        self._extract_academic_information(
            candidate,
            evidence,
        )

        self._extract_institution_information(
            candidate,
            evidence,
        )

        self._extract_course_information(
            candidate,
            job,
            evidence,
        )

        self._extract_research_information(
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

        candidate.evidence.education = evidence

        return evidence

    ###########################################################################
    # Degree
    ###########################################################################

    def _extract_degree_information(
        self,
        candidate: Candidate,
        job: JobDescription,
        evidence: EducationEvidence,
    ) -> None:

        evidence.total_degrees = len(candidate.education)

        required = {
            degree.strip().upper()
            for degree in job.minimum_degree
        }

        highest = None

        for education in candidate.education:

            if (
                highest is None
                or job.minimum_degree_level.value > highest.value
           ):
                highest = job.minimum_degree_level

            evidence.relevant_degree_count += 1

            evidence.relevant_degrees.append(
                job.minimum_degree
            )

            if job.minimum_degree_level.value in required:
                evidence.minimum_degree_met = True
 
        evidence.highest_degree = highest

    ###########################################################################
    # Academic
    ###########################################################################

    def _extract_academic_information(
        self,
        candidate: Candidate,
        evidence: EducationEvidence,
    ) -> None:

        cgpas = [
            education.cgpa
            for education in candidate.education
            if education.cgpa is not None
        ]

        if not cgpas:
            return

        evidence.highest_cgpa = max(cgpas)

        evidence.average_cgpa = (
            sum(cgpas)
            / len(cgpas)
        )

    ###########################################################################
    # Institution
    ###########################################################################

    def _extract_institution_information(
        self,
        candidate: Candidate,
        evidence: EducationEvidence,
    ) -> None:

        ranking = {
           InstitutionTier.UNKNOWN: 0,
           InstitutionTier.TIER_3: 1,
           InstitutionTier.TIER_2: 2,
           InstitutionTier.TIER_1: 3,
       }

        highest = InstitutionTier.UNKNOWN

        for education in candidate.education:

            if ranking[education.tier] > ranking[highest]:
                highest = education.tier

            if education.tier != InstitutionTier.UNKNOWN:
                evidence.relevant_institution_count += 1

        evidence.institution_tier = highest

    ###########################################################################
    # Courses
    ###########################################################################

    def _extract_course_information(
        self,
        candidate: Candidate,
        job: JobDescription,
        evidence: EducationEvidence,
    ) -> None:

        required = {
            skill.lower()
            for skill in job.required_skills
        }

        matched = set()

        for education in candidate.education:

            for course in education.relevant_courses:

                if (
                    course.lower()
                    in required
                ):
                    matched.add(course)

        evidence.relevant_courses = sorted(
            matched
        )

    ###########################################################################
    # Research
    ###########################################################################

    def _extract_research_information(
        self,
        candidate: Candidate,
        evidence: EducationEvidence,
    ) -> None:

        for education in candidate.education:

            evidence.research_project_count += len(
                education.research_projects
            )

            evidence.research_publication_count += len(
                education.publications
            )

    ###########################################################################
    # Future AI Components
    ###########################################################################

    def _extract_semantic_similarity(
        self,
        evidence: EducationEvidence,
    ) -> None:

        evidence.semantic_similarity = 0.0

    def _extract_confidence(
        self,
        candidate: Candidate,
        evidence: EducationEvidence,
    ) -> None:

        if evidence.total_degrees == 0:

            evidence.confidence = 0.0

            return

        evidence.confidence = 1.0
"""
Project : Athena
Module  : Evidence Collector

Purpose
-------
Collects factual evidence by comparing a candidate with a job
description.

Guidelines
----------
- No inference.
- No ranking.
- No text generation.
"""

from __future__ import annotations

from src.core.candidate import Candidate
from src.core.candidate.evidence import EvidenceCollection
from src.core.job import JobDescription


class EvidenceCollector:
    """
    Collects factual evidence for explainable ranking.
    """

    def collect(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> EvidenceCollection:
        """
        Collect evidence from a candidate and job description.
        """

        evidence = EvidenceCollection()

        #######################################################################
        # Raw Facts
        #######################################################################

        if candidate.profile.headline:
            evidence.facts.append(candidate.profile.headline)

        if candidate.profile.summary:
            evidence.facts.append(candidate.profile.summary)

        #######################################################################
        # Skills
        #######################################################################

        candidate_skills = {
            skill.name.lower()
            for skill in candidate.skills
        }

        required_skills = {
            skill.lower()
            for skill in job.required_skills
        }

        evidence.matched_skills.extend(
            sorted(candidate_skills & required_skills)
        )

        evidence.missing_skills.extend(
            sorted(required_skills - candidate_skills)
        )

        #######################################################################
        # Technologies
        #######################################################################

        candidate_technologies = {
            tech.lower()
            for tech in candidate.metadata.get(
                "technologies",
                [],
            )
        }

        required_technologies = {
            tech.lower()
            for tech in job.technologies
        }

        evidence.matched_technologies.extend(
            sorted(
                candidate_technologies &
                required_technologies
            )
        )

        evidence.missing_technologies.extend(
            sorted(
                required_technologies -
                candidate_technologies
            )
        )

        #######################################################################
        # Certifications
        #######################################################################

        candidate_certifications = {
            certification.name.lower()
            for certification in candidate.certifications
        }

        required_certifications = {
            certification.lower()
            for certification in job.certifications
        }

        evidence.matched_certifications.extend(
            sorted(
                candidate_certifications &
                required_certifications
            )
        )

        evidence.missing_certifications.extend(
            sorted(
                required_certifications -
                candidate_certifications
            )
        )

        #######################################################################
        # Education
        #######################################################################

        for education in candidate.education:

            if education.degree:

                evidence.education_matches.append(
                    education.degree
                )

        #######################################################################
        # Experience
        #######################################################################

        required_skills = {
            skill.lower()
            for skill in job.required_skills
        }

        for experience in candidate.experiences:

          if not experience.description:
              continue

          description = experience.description.lower()

        if any(
        skill in description
        for skill in required_skills
    ):

            evidence.relevant_experiences.append(
            experience.title
        )

        #######################################################################
        # Projects
        #######################################################################

        for project in candidate.projects:

             text = (
        f"{project.title} "
        f"{project.description}"
    ).lower()

             if any(
              skill in text
        for skill in required_skills
    ):

                  evidence.relevant_projects.append(
            project.title
        )

        return evidence


###############################################################################
# END OF FILE
###############################################################################
"""
Project : Athena
Module  : Document Builder

Purpose
-------
Builds canonical retrieval documents from Candidate objects.

Guidelines
----------
- Produces one retrieval document per candidate.
- Shared by BM25 and dense retrieval.
- No indexing.
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Candidate


class DocumentBuilder:
    """
    Builds retrieval documents.
    """

    def build(
        self,
        candidate: Candidate,
    ) -> dict[str, Any]:
        """
        Build one retrieval document.
        """

        parts: list[str] = []

        profile = candidate.profile

        if profile.full_name:
            parts.append(profile.full_name)

        if profile.headline:
            parts.append(profile.headline)

        if profile.summary:
            parts.append(profile.summary)

        for skill in candidate.skills:
            parts.append(skill.name)
        ###########################################################################
# Certifications
###########################################################################

        for certification in candidate.certifications:

           parts.append(
              certification.name
    )

           if certification.issuer:

               parts.append(
            certification.issuer
        )
        for education in candidate.education:
            parts.extend(
                [
                    education.degree,
                    education.field_of_study,
                    education.institution,
                ]
            )

        for experience in candidate.experiences:

            parts.extend(
                [
                    experience.company,
                    experience.job_title,
                ]
            )
            s=" ".join(experience.responsibilities)
            if s:
                parts.append(s)

        for project in candidate.projects:

            parts.append(project.title)

            if project.description:
                parts.append(project.description)

        document = " ".join(
            part.strip()
            for part in parts
            if part
        )

        return {
            "candidate_id": candidate.candidate_id,
            "text": document,
        }


###############################################################################
# END OF FILE
###############################################################################
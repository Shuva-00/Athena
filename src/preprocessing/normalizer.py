"""
Project : Athena
Module  : Candidate Normalizer

Purpose
-------
Normalizes candidate information into canonical forms.

Guidelines
----------
- Operates on Candidate objects.
- Standardizes terminology.
- Does not create new information.
"""

from __future__ import annotations

from src.core.candidate import Candidate


class Normalizer:
    """
    Normalizes candidate data.
    """

    SKILL_MAP = {
        "js": "JavaScript",
        "javascript": "JavaScript",
        "ts": "TypeScript",
        "py": "Python",
        "postgres": "PostgreSQL",
        "postgresql": "PostgreSQL",
        "aws": "AWS",
        "gcp": "Google Cloud Platform",
        "azure cloud": "Microsoft Azure",
        "ml": "Machine Learning",
        "ai": "Artificial Intelligence",
    }

    COMPANY_MAP = {
        "google llc": "Google",
        "google inc.": "Google",
        "amazon web services": "AWS",
        "microsoft india": "Microsoft",
    }

    def normalize(
        self,
        candidate: Candidate,
    ) -> Candidate:
        """
        Normalize one candidate.
        """

        self._normalize_skills(candidate)
        self._normalize_companies(candidate)

        return candidate

    def _normalize_skills(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Normalize skill names.
        """

        for skill in candidate.skills:

            key = skill.name.strip().lower()

            if key in self.SKILL_MAP:
                skill.name = self.SKILL_MAP[key]

    def _normalize_companies(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Normalize company names.
        """

        for experience in candidate.experiences:

            key = experience.company.strip().lower()

            if key in self.COMPANY_MAP:
                experience.company = self.COMPANY_MAP[key]


###############################################################################
# END OF FILE
###############################################################################
"""
Project : Athena
Module  : Feature Builder

Purpose
-------
Builds engineered features from a normalized Candidate object.

Guidelines
----------
- Operates on Candidate objects.
- Produces deterministic features only.
- No ranking.
- No embeddings.
- No machine learning.
"""

from __future__ import annotations

from datetime import date

from src.core.candidate import Candidate


class FeatureBuilder:
    """
    Builds engineered candidate features.
    """

    def build(
        self,
        candidate: Candidate,
    ) -> Candidate:
        """
        Build engineered features.
        """

        features = {
            "education_count": self._education_count(candidate),
            "experience_count": self._experience_count(candidate),
            "project_count": self._project_count(candidate),
            "skill_count": self._skill_count(candidate),
            "certification_count": self._certification_count(candidate),
            "language_count": self._language_count(candidate),
            "total_experience_months": self._total_experience(candidate),
            "average_tenure_months": self._average_tenure(candidate),
            "technology_diversity": self._technology_diversity(candidate),
            "achievement_count": self._achievement_count(candidate),
            "keyword_count": self._keyword_count(candidate),
        }

        candidate.metadata["features"] = features

        return candidate

    def _education_count(
        self,
        candidate: Candidate,
    ) -> int:
        return len(candidate.education)

    def _experience_count(
        self,
        candidate: Candidate,
    ) -> int:
        return len(candidate.experiences)

    def _project_count(
        self,
        candidate: Candidate,
    ) -> int:
        return len(candidate.projects)

    def _skill_count(
        self,
        candidate: Candidate,
    ) -> int:
        return len(candidate.skills)

    def _certification_count(
        self,
        candidate: Candidate,
    ) -> int:
        return len(candidate.certifications)

    def _language_count(
        self,
        candidate: Candidate,
    ) -> int:
        return len(candidate.languages)

    def _total_experience(
        self,
        candidate: Candidate,
    ) -> int:
        """
        Returns total experience in months.
        """

        total = 0

        for experience in candidate.experiences:

            if experience.duration_months is not None:
                total += experience.duration_months

        return total

    def _average_tenure(
        self,
        candidate: Candidate,
    ) -> float:
        """
        Returns average tenure in months.
        """

        durations = [
            exp.duration_months
            for exp in candidate.experiences
            if exp.duration_months is not None
        ]

        if not durations:
            return 0.0

        return sum(durations) / len(durations)

    def _technology_diversity(
        self,
        candidate: Candidate,
    ) -> int:
        """
        Number of unique extracted technologies.
        """

        technologies = candidate.metadata.get(
            "technologies",
            [],
        )

        return len(set(technologies))

    def _achievement_count(
        self,
        candidate: Candidate,
    ) -> int:
        """
        Number of extracted achievements.
        """

        achievements = candidate.metadata.get(
            "achievements",
            [],
        )

        return len(achievements)

    def _keyword_count(
        self,
        candidate: Candidate,
    ) -> int:
        """
        Number of extracted keywords.
        """

        keywords = candidate.metadata.get(
            "keywords",
            [],
        )

        return len(keywords)


###############################################################################
# END OF FILE
###############################################################################
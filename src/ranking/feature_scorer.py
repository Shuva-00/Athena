"""
Project : Athena
Module  : Feature Scorer

Purpose
-------
Computes a deterministic feature-based relevance score
between a candidate and a job description.

Guidelines
----------
- Uses engineered features.
- No ML models.
- No embeddings.
"""

from __future__ import annotations
from config import settings
import re

from src.core.candidate import Candidate


class FeatureScorer:
    """
    Scores candidates using engineered features.
    """

    WORD_PATTERN = re.compile(r"[A-Za-z0-9+#.]+")

    def score(
        self,
        job_description: str,
        candidate: Candidate,
    ) -> float:
        """
        Compute feature score.
        """

        features = candidate.metadata.get(
            "features",
            {},
        )

        jd_words = {
            word.lower()
            for word in self.WORD_PATTERN.findall(
                job_description
            )
        }

        candidate_skills = {
            skill.name.lower()
            for skill in candidate.skills
        }

        skill_overlap = len(
            jd_words.intersection(candidate_skills)
        )

        score = 0.0

        score += skill_overlap * settings.weights.features.skill_match

        score += (
    features["total_experience_months"] / 12
) * settings.weights.features.experience

        score += (
    features["project_count"]
) * settings.weights.features.project_count

        score += (
    features["certification_count"]
) * settings.weights.features.certification_count

        score += (
    features["technology_diversity"]
) * settings.weights.features.technology_diversity

        return score


###############################################################################
# END OF FILE
###############################################################################
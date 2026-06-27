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
from src.config import (
    SKILL_MATCH_WEIGHT,
    EXPERIENCE_WEIGHT,
    PROJECT_WEIGHT,
    CERTIFICATION_WEIGHT,
    TECHNOLOGY_WEIGHT,
)
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

        score += skill_overlap * SKILL_MATCH_WEIGHT

        score += (
    features["total_experience_months"] / 12
) * EXPERIENCE_WEIGHT

        score += (
    features["project_count"]
) * PROJECT_WEIGHT

        score += (
    features["certification_count"]
) * CERTIFICATION_WEIGHT

        score += (
    features["technology_diversity"]
) * TECHNOLOGY_WEIGHT

        return score


###############################################################################
# END OF FILE
###############################################################################
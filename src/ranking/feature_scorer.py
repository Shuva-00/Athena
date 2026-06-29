"""
Project : Athena
Module  : Feature Scorer

Purpose
-------
Computes normalized feature scores for a candidate.

Guidelines
----------
- Orchestrates individual feature scorers.
- Does not implement scoring logic itself.
- Updates candidate.feature_scores.
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate

from src.ranking.scorers.skill_scorer import SkillScorer


class FeatureScorer:
    """
    Computes all normalized feature scores.
    """

    def __init__(self) -> None:

        self.skill_scorer = SkillScorer()

    ###########################################################################
    # Public API
    ###########################################################################

    def score(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Compute all candidate feature scores.
        """

        self._score_skills(candidate)

    ###########################################################################
    # Private Helpers
    ###########################################################################

    def _score_skills(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Compute skill feature score.
        """

        candidate.feature_scores.skill_score = (
            self.skill_scorer.score(
                candidate.evidence.skill,
            )
        )
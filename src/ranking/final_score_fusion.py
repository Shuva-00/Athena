"""
Project : Athena
Module  : Final Score Fusion

Purpose
-------
Combines semantic and engineered feature scores into the final ranking score.

Guidelines
----------
- Pure scoring logic.
- No sorting.
- No ranking.
- Uses configuration-driven weights.
"""

from __future__ import annotations

from src.config import settings
from src.core.candidate.entity import Candidate


class FinalScoreFusion:
    """
    Computes the final ranking score for a candidate.
    """

    ###########################################################################
    # Initialization
    ###########################################################################

    def __init__(self) -> None:

        self._weights = settings.weights.fusion

    ###########################################################################
    # Score One Candidate
    ###########################################################################

    def score(
        self,
        candidate: Candidate,
    ) -> float:

        score = (

            candidate.scores.semantic_score
            * self._weights.cross_encoder

            +

            candidate.features.feature_score
            * self._weights.feature_score

        )

        score = min(
            max(score, 0.0),
            1.0,
        )

        candidate.scores.feature_score = (
            candidate.features.feature_score
        )

        candidate.scores.final_score = score

        return score

    ###########################################################################
    # Score Multiple Candidates
    ###########################################################################

    def score_all(
        self,
        candidates: list[Candidate],
    ) -> None:

        for candidate in candidates:

            self.score(candidate)
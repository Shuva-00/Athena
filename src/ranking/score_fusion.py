"""
Project : Athena
Module  : Score Fusion

Purpose
-------
Combines semantic and feature scores into a final ranking score.

Guidelines
----------
- Normalizes scores before fusion.
- Uses configurable weights.
- No ranking logic.
"""

from __future__ import annotations
from src.config import settings


class ScoreFusion:
    """
    Combines multiple scoring signals.
    """

    def fuse(
        
        self,
        cross_scores: list[float],
        feature_scores: list[float],
    ) -> list[float]:
        """
        Fuse semantic and feature scores.
        """
        if len(cross_scores) != len(feature_scores):
           raise ValueError(
               "Score lists must have equal length."
    )
        cross_scores = self._normalize(cross_scores)
        feature_scores = self._normalize(feature_scores)

        fused_scores = []

        for cross_score, feature_score in zip(
            cross_scores,
            feature_scores,
        ):

            score = (
                settings.weights.fusion.cross_encoder * cross_score
                + settings.weights.fusion.feature_encoder * feature_score
            )

            fused_scores.append(score)

        return fused_scores

    def _normalize(
        self,
        scores: list[float],
    ) -> list[float]:
        """
        Min-Max normalization.
        """

        if not scores:
            return []

        minimum = min(scores)
        maximum = max(scores)

        if maximum == minimum:
            return [1.0] * len(scores)

        return [
            (score - minimum) / (maximum - minimum)
            for score in scores
        ]


###############################################################################
# END OF FILE
###############################################################################
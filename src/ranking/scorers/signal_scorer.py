"""
Project : Athena
Module  : Signal Scorer

Purpose
-------
Computes the normalized behavioural signal score.

Guidelines
----------
- Pure scoring logic.
- Reads only SignalEvidence.
- Returns normalized score in [0,1].
- Uses configuration-driven weights.
"""

from __future__ import annotations

from src.config import settings
from src.core.candidate.signal_evidence import SignalEvidence

from .base_scorer import BaseScorer


class SignalScorer(BaseScorer):
    """
    Computes normalized behavioural signal score.
    """

    ###########################################################################
    # Initialization
    ###########################################################################

    def __init__(self) -> None:

        self._weights = settings.weights.feature_scoring.signal

    ###########################################################################
    # Public API
    ###########################################################################

    def score(
        self,
        evidence: SignalEvidence,
    ) -> float:

        responsiveness = self._responsiveness_score(
            evidence,
        )

        engagement = self._engagement_score(
            evidence,
        )

        assessment = self._assessment_score(
            evidence,
        )

        return self._weighted_score(
            responsiveness,
            engagement,
            assessment,
        )

    ###########################################################################
    # Components
    ###########################################################################

    def _responsiveness_score(
        self,
        evidence: SignalEvidence,
    ) -> float:

        return evidence.responsiveness_score

    def _engagement_score(
        self,
        evidence: SignalEvidence,
    ) -> float:

        return evidence.engagement_score

    def _assessment_score(
        self,
        evidence: SignalEvidence,
    ) -> float:

        return evidence.assessment_score

    ###########################################################################
    # Final Score
    ###########################################################################

    def _weighted_score(
        self,
        responsiveness: float,
        engagement: float,
        assessment: float,
    ) -> float:

        score = (

            responsiveness
            * self._weights.responsiveness

            +

            engagement
            * self._weights.engagement

            +

            assessment
            * self._weights.assessment

        )

        return min(
            max(score, 0.0),
            1.0,
        )
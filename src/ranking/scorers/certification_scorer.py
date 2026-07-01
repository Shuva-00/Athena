"""
Project : Athena
Module  : Certification Scorer

Purpose
-------
Computes the normalized certification feature score.

Guidelines
----------
- Pure scoring logic.
- Reads only CertificationEvidence.
- Returns normalized score in [0,1].
- Uses configuration-driven weights.
"""

from __future__ import annotations

from src.config import settings
from src.core.candidate.certification_evidence import (
    CertificationEvidence,
)

from .base_scorer import BaseScorer


class CertificationScorer(BaseScorer):
    """
    Computes normalized certification score.
    """

    def __init__(self) -> None:

        self._weights = settings.weights.feature_scoring.certification

    ###########################################################################
    # Public API
    ###########################################################################

    def score(
        self,
        evidence: CertificationEvidence,
    ) -> float:

        relevance = self._relevance_score(evidence)

        recency = self._recency_score(evidence)

        return self._weighted_score(
            relevance,
            recency,
        )

    ###########################################################################
    # Component Scores
    ###########################################################################

    def _relevance_score(
        self,
        evidence: CertificationEvidence,
    ) -> float:

        return evidence.certification_relevance

    def _recency_score(
        self,
        evidence: CertificationEvidence,
    ) -> float:

        if evidence.total_certifications == 0:
            return 0.0

        return min(
            evidence.recent_certifications
            / evidence.total_certifications,
            1.0,
        )

    ###########################################################################
    # Weighted Score
    ###########################################################################

    def _weighted_score(
        self,
        relevance: float,
        recency: float,
    ) -> float:

        score = (

            relevance
            * self._weights.relevance

            +

            recency
            * self._weights.recency

        )

        return min(
            max(score, 0.0),
            1.0,
        )
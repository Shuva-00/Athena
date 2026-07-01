"""
Project : Athena
Module  : Integrity Scorer

Purpose
-------
Computes the normalized integrity feature score.

Guidelines
----------
- Pure scoring logic.
- Reads only IntegrityEvidence.
- Returns normalized score in [0,1].
- Uses configuration-driven weights.
"""

from __future__ import annotations

from src.config import settings
from src.core.candidate.integrity_evidence import IntegrityEvidence

from .base_scorer import BaseScorer


class IntegrityScorer(BaseScorer):
    """
    Computes normalized integrity score.
    """

    ###########################################################################
    # Initialization
    ###########################################################################

    def __init__(self) -> None:

        self._weights = settings.weights.feature_scoring.integrity

    ###########################################################################
    # Public API
    ###########################################################################

    def score(
        self,
        evidence: IntegrityEvidence,
    ) -> float:

        consistency = self._consistency_score(
            evidence,
        )

        confidence = self._confidence_score(
            evidence,
        )

        return self._weighted_score(
            consistency,
            confidence,
        )

    ###########################################################################
    # Components
    ###########################################################################

    def _consistency_score(
        self,
        evidence: IntegrityEvidence,
    ) -> float:

        issues = (

            evidence.missing_required_fields

            + evidence.duplicate_skills

            + evidence.duplicate_certifications

            + evidence.timeline_inconsistencies

            + evidence.experience_inconsistencies

        )

        return max(
            0.0,
            1.0 - (issues * 0.10),
        )

    def _confidence_score(
        self,
        evidence: IntegrityEvidence,
    ) -> float:

        return evidence.confidence

    ###########################################################################
    # Final Score
    ###########################################################################

    def _weighted_score(
        self,
        consistency: float,
        confidence: float,
    ) -> float:

        score = (

            consistency
            * self._weights.consistency

            +

            confidence
            * self._weights.confidence

        )

        return min(
            max(score, 0.0),
            1.0,
        )
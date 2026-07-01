"""
Project : Athena
Module  : Experience Scorer

Purpose
-------
Computes the normalized experience feature score.

Guidelines
----------
- Pure scoring logic.
- Reads only ExperienceEvidence.
- Returns normalized score in [0,1].
- Uses configuration-driven weights.
"""

from __future__ import annotations

from src.config import settings
from src.core.candidate.experience_evidence import ExperienceEvidence

from .base_scorer import BaseScorer


class ExperienceScorer(BaseScorer):
    """
    Computes normalized experience score.
    """

    ###########################################################################
    # Initialization
    ###########################################################################

    def __init__(self) -> None:

        self._weights = settings.weights.feature_scoring.experience

        self._normalization = settings.weights.normalization

    ###########################################################################
    # Public API
    ###########################################################################

    def score(
        self,
        evidence: ExperienceEvidence,
    ) -> float:
        """
        Compute overall experience score.
        """

        relevance = self._relevance_score(evidence)

        stability = self._stability_score(evidence)

        leadership = self._leadership_score(evidence)

        semantic = self._semantic_score(evidence)

        return self._weighted_score(
            relevance,
            stability,
            leadership,
            semantic,
        )

    ###########################################################################
    # Individual Components
    ###########################################################################

    def _relevance_score(
        self,
        evidence: ExperienceEvidence,
    ) -> float:

        if evidence.total_experience_months == 0:
            return 0.0

        return min(
            evidence.relevant_experience_months
            / evidence.total_experience_months,
            1.0,
        )


    def _stability_score(
        self,
        evidence: ExperienceEvidence,
    ) -> float:

        cap = self._normalization.duration_cap_months

        return min(
            evidence.average_tenure_months / cap,
            1.0,
        )

    def _leadership_score(
        self,
        evidence: ExperienceEvidence,
    ) -> float:

        if evidence.total_roles == 0:
            return 0.0

        return min(
            evidence.leadership_role_count
            / evidence.total_roles,
            1.0,
        )


    def _semantic_score(
        self,
        evidence: ExperienceEvidence,
    ) -> float:

        return (
            evidence.semantic_title_similarity
            + evidence.semantic_responsibility_similarity
        ) / 2

    ###########################################################################
    # Final Weighted Score
    ###########################################################################

    def _weighted_score(
        self,
        relevance: float,
        stability: float,
        leadership: float,
        semantic: float,
    ) -> float:

        score = (

    relevance
    * self._weights.relevance

    +

    stability
    * self._weights.stability

    +

    leadership
    * self._weights.leadership
    +

    semantic
    * self._weights.semantic

)

        return min(
            max(score, 0.0),
            1.0,
        )
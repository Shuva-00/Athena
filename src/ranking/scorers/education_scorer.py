"""
Project : Athena
Module  : Education Scorer

Purpose
-------
Computes the normalized education feature score.

Guidelines
----------
- Pure scoring logic.
- Reads only EducationEvidence.
- Returns normalized score in [0,1].
- Uses configuration-driven weights.
"""

from __future__ import annotations

from src.config import settings
from src.core.candidate.education_evidence import EducationEvidence

from .base_scorer import BaseScorer


class EducationScorer(BaseScorer):
    """
    Computes normalized education score.
    """

    ###########################################################################
    # Initialization
    ###########################################################################

    def __init__(self) -> None:

        self._weights = settings.weights.feature_scoring.education

    ###########################################################################
    # Public API
    ###########################################################################

    def score(
        self,
        evidence: EducationEvidence,
    ) -> float:

        degree = self._degree_score(evidence)

        cgpa = self._cgpa_score(evidence)

        institution = self._institution_score(evidence)

        research = self._research_score(evidence)

        semantic = self._semantic_score(evidence)

        confidence = self._confidence_score(evidence)

        return self._weighted_score(
            degree,
            cgpa,
            institution,
            research,
            semantic,
            confidence,
        )

    ###########################################################################
    # Component Scores
    ###########################################################################

    def _degree_score(
        self,
        evidence: EducationEvidence,
    ) -> float:

        return 1.0 if evidence.minimum_degree_met else 0.0

    def _cgpa_score(
        self,
        evidence: EducationEvidence,
    ) -> float:

        if evidence.highest_cgpa is None:
            return 0.0

        return min(
            evidence.highest_cgpa / 10.0,
            1.0,
        )

    def _institution_score(
        self,
        evidence: EducationEvidence,
    ) -> float:

        mapping = {
            "TIER_1": 1.0,
            "TIER_2": 0.8,
            "TIER_3": 0.6,
            "UNKNOWN": 0.0,
        }

        return mapping.get(
            evidence.institution_tier.value,
            0.0,
        )

    def _research_score(
        self,
        evidence: EducationEvidence,
    ) -> float:

        total = (
            evidence.research_project_count
            + evidence.research_publication_count
        )

        return min(
            total / 5,
            1.0,
        )

    def _semantic_score(
        self,
        evidence: EducationEvidence,
    ) -> float:

        return evidence.semantic_similarity

    def _confidence_score(
        self,
        evidence: EducationEvidence,
    ) -> float:

        return evidence.confidence

    ###########################################################################
    # Weighted Score
    ###########################################################################

    def _weighted_score(
        self,
        degree: float,
        cgpa: float,
        institution: float,
        research: float,
        semantic: float,
        confidence: float,
    ) -> float:

        score = (

            degree
            * self._weights.degree

            +

            cgpa
            * self._weights.cgpa

            +

            institution
            * self._weights.institution

            +

            research
            * self._weights.research

            +

            semantic
            * self._weights.semantic

            +

            confidence
            * self._weights.confidence

        )

        return min(
            max(score, 0.0),
            1.0,
        )
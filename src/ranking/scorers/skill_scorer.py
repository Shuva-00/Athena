"""
Project : Athena
Module  : Skill Scorer

Purpose
-------
Computes the normalized skill feature score.

Guidelines
----------
- Pure scoring logic.
- Reads only SkillEvidence.
- Returns normalized score in [0,1].
- Uses configuration-driven weights.
"""

from __future__ import annotations
from src.config import settings

from src.core.candidate.skill_evidence import SkillEvidence

from .base_scorer import BaseScorer


class SkillScorer(BaseScorer):
    """
    Computes normalized skill score.
    """

    def __init__(self) -> None:
        self._weights = settings.weights.feature_scoring.skill
        self._normalization = settings.weights.normalization

    ###########################################################################
    # Public API
    ###########################################################################

    def score(
        self,
        evidence: SkillEvidence,
    ) -> float:
        """
        Compute overall normalized skill score.
        """

        matching = self._matching_score(evidence)

        duration = self._duration_score(evidence)

        confidence = self._confidence_score(evidence)

        endorsement = self._endorsement_score(evidence)

        semantic = self._semantic_score(evidence)

        return self._weighted_score(
            matching,
            duration,
            confidence,
            endorsement,
            semantic,
)

    ###########################################################################
    # Individual Components
    ###########################################################################
    
    def _matching_score(
        self,
        evidence: SkillEvidence,
    ) -> float:

        if evidence.required_total == 0:
            return 0.0

        return min(
            evidence.exact_matches /
            evidence.required_total,
            1.0,
        )


    def _duration_score(
        self,
        evidence: SkillEvidence,
    ) -> float:
        cap = self._normalization.duration_cap_months

        return min(
            evidence.average_duration_months / cap,
            1.0,
)


    def _endorsement_score(
        self,
        evidence: SkillEvidence,
    ) -> float:
        """
        Placeholder.

        Will use:
        average_endorsements
        """

        return 0.0

    def _semantic_score(
        self,
        evidence: SkillEvidence,
    ) -> float:

        return evidence.semantic_similarity

    ###########################################################################
    # Final Weighted Score
    ###########################################################################
   
    def _weighted_score(
        self,
        matching: float,
        duration: float,
        confidence: float,
        endorsement: float,
        semantic: float,
    ) -> float:

        score = (

            matching
            * self._weights.matching

            +

            duration
            * self._weights.duration

            +

            confidence
            * self._weights.confidence

            +

            endorsement
            * self._weights.endorsement

            +

            semantic
            * self._weights.semantic

       )

        return min(
               max(score, 0.0),
               1.0,
)
    def _confidence_score(
        self,
        evidence: SkillEvidence,
    ) -> float:
        """
        Compute confidence score for the extracted skills.
        """

        return evidence.confidence
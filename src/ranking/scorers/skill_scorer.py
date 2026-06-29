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
- Returns score in [0,1].
"""

from __future__ import annotations

from src.config import settings

from src.core.candidate.skill_evidence import SkillEvidence

from .base_scorer import BaseScorer


class SkillScorer(BaseScorer):
    """
    Computes normalized skill score.
    """

    ###########################################################################
    # Public API
    ###########################################################################

    def score(
        self,
        evidence: SkillEvidence,
    ) -> float:
        """
        Compute overall skill score.
        """

        return self._matching_score(
            evidence,
        )

    ###########################################################################
    # Private Helpers
    ###########################################################################

    def _matching_score(
        self,
        evidence: SkillEvidence,
    ) -> float:
        """
        Compute exact skill matching score.
        """

        if evidence.required_total == 0:
            return 0.0

        return min(
            evidence.exact_matches
            / evidence.required_total,
            1.0,
        )
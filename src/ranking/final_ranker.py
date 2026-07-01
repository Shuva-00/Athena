"""
Project : Athena
Module  : Final Ranker

Purpose
-------
Produces the final ranked list of candidates.

Guidelines
----------
- Sorts candidates by fused score.
- Updates CandidateScores.
- No score computation.
"""

from __future__ import annotations

from src.config import settings
from src.core.candidate import Candidate


class FinalRanker:
    """
    Produces the final ranked candidate list.
    """

    def rank(
        self,
        candidates: list[Candidate],
        cross_scores: list[float],
        feature_scores: list[float],
        final_scores: list[float],
        top_k: int = settings.ranking.ranking.final_top_k,
    ) -> list[Candidate]:
        """
        Rank candidates using the final fused scores.
        """

        if not (
            len(candidates)
            == len(cross_scores)
            == len(feature_scores)
            == len(final_scores)
        ):
            raise ValueError(
                "All input lists must have the same length."
            )

        for candidate, cross_score, feature_score, final_score in zip(
            candidates,
            cross_scores,
            feature_scores,
            final_scores,
        ):

            candidate.scores.semantic_score = cross_score
            candidate.scores.feature_score = feature_score
            candidate.scores.final_score = final_score

        ranked_candidates = sorted(
            candidates,
            key=lambda candidate: candidate.scores.final_score,
            reverse=True,
        )
        for rank, candidate in enumerate(
            ranked_candidates,
            start=1,
            ):

            candidate.scores.rank = rank
        return ranked_candidates[:top_k]


###############################################################################
# END OF FILE
###############################################################################
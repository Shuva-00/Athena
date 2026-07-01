"""
Project : Athena
Module  : Ranking Engine

Purpose
-------
Produces the final ranked list of candidates.

Guidelines
----------
- Pure ranking logic.
- No feature extraction.
- No model inference.
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate


class RankingEngine:
    """
    Produces the final ranking.
    """

    def __init__(self) -> None:

        pass

    ###########################################################################
    # Public API
    ###########################################################################

    def rank(
        self,
        candidates: list[Candidate],
    ) -> list[Candidate]:


        #######################################################################
        # Sort
        #######################################################################

        candidates.sort(
            key=lambda candidate: candidate.scores.final_score,
            reverse=True,
        )

        #######################################################################
        # Rank
        #######################################################################

        total = len(candidates)

        for index, candidate in enumerate(
            candidates,
            start=1,
        ):

            candidate.scores.rank = index

            if total == 1:

                candidate.scores.percentile = 100.0

            else:

                candidate.scores.percentile = (
                    (total - index)
                    /
                    (total - 1)
                ) * 100.0

        return candidates
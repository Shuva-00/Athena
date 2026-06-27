"""
Project : Athena
Module  : Reciprocal Rank Fusion

Purpose
-------
Fuses multiple ranked retrieval lists using
Reciprocal Rank Fusion (RRF).

Reference
---------
Cormack et al., 2009.
"""

from __future__ import annotations

from collections import defaultdict

from src.config import FINAL_RETRIEVAL_TOP_K
from src.config import RRF_K


class Fusion:
    """
    Reciprocal Rank Fusion.
    """

    def fuse(
        self,
        *rankings: list[tuple[str, float]],
        top_k: int = FINAL_RETRIEVAL_TOP_K,
    ) -> list[tuple[str, float]]:
        """
        Fuse multiple ranked lists.
        """

        scores: dict[str, float] = defaultdict(float)

        for ranking in rankings:

            for rank, (candidate_id, _) in enumerate(
                ranking,
                start=1,
            ):

                scores[candidate_id] += 1.0 / (
                    RRF_K + rank
                )

        fused = sorted(
            scores.items(),
            key=lambda item: item[1],
            reverse=True,
        )

        return fused[:top_k]


###############################################################################
# END OF FILE
###############################################################################
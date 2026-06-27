"""
Project : Athena
Module  : BM25 Retriever

Purpose
-------
Performs sparse retrieval using BM25.
"""

from __future__ import annotations

from rank_bm25 import BM25Okapi

from src.config import BM25_TOP_K


class BM25Retriever:
    """
    Sparse retriever based on BM25.
    """

    def retrieve(
        self,
        query: str,
        bm25: BM25Okapi,
        candidate_ids: list[str],
        top_k: int = BM25_TOP_K,
    ) -> list[tuple[str, float]]:
        """
        Retrieve top candidates using BM25.
        """

        query_tokens = query.lower().split()

        scores = bm25.get_scores(query_tokens)

        ranked = sorted(
            zip(candidate_ids, scores),
            key=lambda x: x[1],
            reverse=True,
        )

        return ranked[:top_k]


###############################################################################
# END OF FILE
###############################################################################
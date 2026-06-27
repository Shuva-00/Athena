"""
Project : Athena
Module  : Dense Retriever

Purpose
-------
Performs dense retrieval using BGE embeddings and FAISS.
"""

from __future__ import annotations

import faiss
import numpy as np

from config import settings
from src.retrieval.candidate_encoder import CandidateEncoder


class DenseRetriever:
    """
    Dense semantic retriever.
    """

    def __init__(self) -> None:

        self.encoder = CandidateEncoder()

    def retrieve(
        self,
        query: str,
        faiss_index: faiss.Index,
        candidate_ids: list[str],
        top_k: int = settings.retrieval.dense.top_k,
    ) -> list[tuple[str, float]]:
        """
        Retrieve top candidates using dense retrieval.
        """

        embedding = self.encoder.encode(query)

        embedding = embedding.astype(np.float32)

        faiss.normalize_L2(
            embedding.reshape(1, -1)
        )

        scores, indices = faiss_index.search(
            embedding.reshape(1, -1),
            top_k,
        )

        results: list[tuple[str, float]] = []

        for score, index in zip(
            scores[0],
            indices[0],
        ):

            if index == -1:
                continue

            results.append(
                (
                    candidate_ids[index],
                    float(score),
                )
            )

        return results


###############################################################################
# END OF FILE
###############################################################################
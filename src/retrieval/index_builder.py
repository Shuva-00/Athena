"""
Project : Athena
Module  : Index Builder

Purpose
-------
Builds BM25 and FAISS indexes from retrieval documents.
"""

from __future__ import annotations

import faiss
import numpy as np
from rank_bm25 import BM25Okapi

from config import settings
from src.retrieval.candidate_encoder import CandidateEncoder


class IndexBuilder:
    """
    Builds retrieval indexes.
    """

    def __init__(self) -> None:

        self.encoder = CandidateEncoder()

    def build(
        self,
        documents: list[dict],
    ) -> tuple[
        BM25Okapi,
        faiss.IndexFlatIP,
        list[str],
    ]:
        """
        Build BM25 and FAISS indexes.
        """

        texts = [
            doc["text"]
            for doc in documents
        ]

        candidate_ids = [
            doc["candidate_id"]
            for doc in documents
        ]

        tokenized = [
            text.lower().split()
            for text in texts
        ]

        bm25 = BM25Okapi(tokenized)

        embeddings = self.encoder.encode_batch(
            texts
        )

        embeddings = embeddings.astype(
            np.float32
        )

        if settings.retrieval.dense.normalize_embeddings:
            faiss.normalize_L2(embeddings)

        dimension = embeddings.shape[1]

        faiss_index = faiss.IndexFlatIP(
            dimension
        )

        faiss_index.add(
            embeddings
        )

        return (
            bm25,
            faiss_index,
            candidate_ids,
        )


###############################################################################
# END OF FILE
###############################################################################
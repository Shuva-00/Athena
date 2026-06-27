"""
Project : Athena
Module  : Candidate Encoder

Purpose
-------
Encodes candidate and job description text into dense embeddings
using a SentenceTransformer model.

Guidelines
----------
- Responsible only for embedding generation.
- No retrieval.
- No indexing.
"""

from __future__ import annotations

from sentence_transformers import SentenceTransformer
import numpy as np
from src.config.settings import EMBEDDING_MODEL

class CandidateEncoder:
    """
    Dense embedding encoder.
    """

    MODEL_NAME = EMBEDDING_MODEL

    def __init__(self) -> None:

        self.model = SentenceTransformer(
            self.MODEL_NAME
        )

    def encode(
        self,
        text: str,
    ) -> np.ndarray:
        """
        Encode one text.
        """

        embedding = self.model.encode(
            text,
            normalize_embeddings=True,
            convert_to_numpy=True,
        )

        return embedding

    def encode_batch(
        self,
        texts: list[str],
    ) -> np.ndarray:
        """
        Encode multiple texts.
        """

        embeddings = self.model.encode(
            texts,
            normalize_embeddings=True,
            convert_to_numpy=True,
            show_progress_bar=True,
        )

        return embeddings


###############################################################################
# END OF FILE
###############################################################################
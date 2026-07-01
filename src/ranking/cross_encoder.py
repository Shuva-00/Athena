"""
Project : Athena
Module  : Cross Encoder

Purpose
-------
Computes semantic relevance scores between a job description
and candidate documents using a CrossEncoder model.

Guidelines
----------
- No retrieval.
- No feature engineering.
- No ranking.
"""

from __future__ import annotations

from sentence_transformers import CrossEncoder

from src.config import settings
import numpy as np
import math
class CrossEncoderRanker:
    """
    Cross Encoder semantic scorer.
    """

    def __init__(self) -> None:

        self.model = CrossEncoder(
            settings.models.cross_encoder.model_name
        )

    def score(
        self,
        job_description: str,
        candidate_document: str,
    ) -> float:
        """
        Score one candidate.
        """

        score = self.model.predict(
            [
                (
                    job_description,
                    candidate_document,
                )
            ]
        )[0]

        return 1.0 / (1.0 + math.exp(-float(score)))

    def score_batch(
        self,
        job_description: str,
        candidate_documents: list[str],
    ) -> list[float]:
        """
        Score multiple candidates.

        Returns normalized semantic scores in [0, 1].
        """

    ###########################################################################
    # Build sentence pairs
    ###########################################################################

        pairs = [
            (
               job_description,
                document,
            )
            for document in candidate_documents
        ]

    ###########################################################################
    # Raw CrossEncoder logits
    ###########################################################################

        scores = self.model.predict(
            pairs
        )

        scores = np.asarray(
            scores,
            dtype=float,
        )

    ###########################################################################
    # Min-Max Normalization
    ###########################################################################

        minimum = scores.min()
        maximum = scores.max()

        if maximum - minimum < 1e-12:

            normalized = np.full_like(
    scores,
    0.5,
)

        else:

            normalized = (
                scores - minimum
            ) / (
                maximum - minimum
            )

        return normalized.tolist()


###############################################################################
# END OF FILE
###############################################################################
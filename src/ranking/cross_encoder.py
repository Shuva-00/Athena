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

from config import settings


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

        return float(score)

    def score_batch(
        self,
        job_description: str,
        candidate_documents: list[str],
    ) -> list[float]:
        """
        Score multiple candidates.
        """

        pairs = [
            (
                job_description,
                document,
            )
            for document in candidate_documents
        ]

        scores = self.model.predict(
            pairs
        )

        return [
            float(score)
            for score in scores
        ]


###############################################################################
# END OF FILE
###############################################################################
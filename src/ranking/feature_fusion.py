

from __future__ import annotations

from src.config import settings
from src.core.candidate.features import CandidateFeatures


class FeatureFusion:
    """
    Computes the overall feature score.
    """

    def __init__(self) -> None:

        self._weights = settings.weights.feature_fusion

    def score(
        self,
        features: CandidateFeatures,
    ) -> float:

        score = (

            features.skill_score
            * self._weights.skill

            +

            features.experience_score
            * self._weights.experience

            +

            features.education_score
            * self._weights.education

            +

            features.certification_score
            * self._weights.certification

            +

            features.signal_score
            * self._weights.signal

            +

            features.integrity_score
            * self._weights.integrity

        )

        return min(
            max(score, 0.0),
            1.0,
        )
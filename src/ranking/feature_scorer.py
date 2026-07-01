"""
Project : Athena
Module  : Feature Scorer

Purpose
-------
Computes normalized feature scores for a candidate.

Guidelines
----------
- Orchestrates individual feature scorers.
- Does not implement scoring logic.
- Updates candidate.features.
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate
from src.ranking.scorers.experience_scorer import ExperienceScorer
from src.ranking.scorers.skill_scorer import SkillScorer
from src.ranking.scorers.education_scorer import EducationScorer
from src.ranking.scorers.certification_scorer import CertificationScorer
from src.ranking.scorers.signal_scorer import SignalScorer
from src.ranking.scorers.integrity_scorer import IntegrityScorer
from src.ranking.feature_fusion import FeatureFusion
class FeatureScorer:
    """
    Computes all normalized feature scores.
    """

    ###########################################################################
    # Initialization
    ###########################################################################

    def __init__(self) -> None:

        self._skill_scorer = SkillScorer()
        self._experience_scorer = ExperienceScorer()
        self._education_scorer = EducationScorer()
        self._certification_scorer=CertificationScorer()
        self._signal_scorer = SignalScorer()
        self._integrity_scorer = IntegrityScorer()
        self._feature_fusion = FeatureFusion()
    ###########################################################################
    # Public API
    ###########################################################################

    def score(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Compute all feature scores for a candidate.
        """

        self._score_skills(candidate)
        self._score_experience(candidate)

        self._score_education(candidate)

        self._score_certifications(candidate)

        self._score_signals(candidate)

        self._score_integrity(candidate)
        candidate.features.feature_score = (
        self._feature_fusion.score(
         candidate.features
    )
)
    ###########################################################################
    # Skill
    ###########################################################################

    def _score_skills(
        self,
        candidate: Candidate,
    ) -> None:

        candidate.features.skill_score = (
            self._skill_scorer.score(
                candidate.evidence.skill,
            )
        )

    ###########################################################################
    # Experience
    ###########################################################################

    def _score_experience(
        self,
        candidate: Candidate,
    ) -> None:
        """
         Compute experience feature score.
        """

        candidate.features.experience_score = (
            self._experience_scorer.score(
                candidate.evidence.experience,
            )
        )

    ###########################################################################
    # Education
    ###########################################################################

    def _score_education(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Compute education feature score.
        """

        candidate.features.education_score = (
            self._education_scorer.score(
                candidate.evidence.education,
            )
        )

    ###########################################################################
    # Certifications
    ###########################################################################

    def _score_certifications(
        self,
        candidate: Candidate,
     ) -> None:
        """
        Compute certification feature score.
        """

        candidate.features.certification_score = (
            self._certification_scorer.score(
                candidate.evidence.certification,
            )
        )

    ###########################################################################
    # Signals
    ###########################################################################

    def _score_signals(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Compute behavioural signal score.
        """

        candidate.features.signal_score = (

            self._signal_scorer.score(

                candidate.evidence.signal,

            )

        )

    ###########################################################################
    # Integrity
    ###########################################################################

    def _score_integrity(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Compute integrity feature score.
        """

        candidate.features.integrity_score = (

            self._integrity_scorer.score(

                candidate.evidence.integrity,
 
        )

    )

    


###############################################################################
# END OF FILE
###############################################################################
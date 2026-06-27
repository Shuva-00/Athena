"""
Project : Athena
Module  : Evidence Analyzer

Purpose
-------
Analyzes collected evidence and derives strengths,
weaknesses, and hiring risks.

Guidelines
----------
- Deterministic.
- No text generation.
- No ranking.
"""

from __future__ import annotations

from src.core.candidate.evidence import EvidenceCollection
from src.config import (
    MIN_STRONG_SKILL_MATCH,
    MIN_STRONG_TECH_MATCH,
)

class EvidenceAnalyzer:
    """
    Analyzes candidate evidence.
    """

    def analyze(
        self,
        evidence: EvidenceCollection,
    ) -> EvidenceCollection:
        """
        Analyze collected evidence.
        """

        #######################################################################
        # Strengths
        #######################################################################

        if len(evidence.matched_skills) >= MIN_STRONG_SKILL_MATCH:
            evidence.strengths.append(
                "Strong skill alignment with the job requirements."
            )

        if len(evidence.matched_technologies) >= MIN_STRONG_TECH_MATCH:
            evidence.strengths.append(
                "Strong technology stack alignment."
            )

        if evidence.relevant_projects:
            evidence.strengths.append(
                "Relevant project experience."
            )

        if evidence.relevant_experiences:
            evidence.strengths.append(
                "Relevant professional experience."
            )

        if evidence.education_matches:
            evidence.strengths.append(
                "Relevant educational background."
            )

        #######################################################################
        # Weaknesses
        #######################################################################

        if evidence.missing_skills:
            evidence.weaknesses.append(
                f"Missing {len(evidence.missing_skills)} required skill(s)."
            )

        if evidence.missing_technologies:
            evidence.weaknesses.append(
                f"Missing {len(evidence.missing_technologies)} required technology(s)."
            )

        if evidence.missing_certifications:
            evidence.weaknesses.append(
                "Required certifications are missing."
            )

        #######################################################################
        # Risks
        #######################################################################

        if (
            len(evidence.missing_skills)
            >= len(evidence.matched_skills)
        ):
            evidence.risks.append(
                "Low overall skill match."
            )

        if (
            len(evidence.missing_technologies)
            > len(evidence.matched_technologies)
        ):
            evidence.risks.append(
                "Technology mismatch."
            )

        if not evidence.relevant_experiences:
            evidence.risks.append(
                "No relevant professional experience found."
            )

        return evidence


###############################################################################
# END OF FILE
###############################################################################
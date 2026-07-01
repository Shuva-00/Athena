"""
Project : Athena
Module  : Reason Generator

Purpose
-------
Generates recruiter-friendly explanations from structured evidence.

Guidelines
----------
- Uses analyzed evidence only.
- No inference.
- No scoring.
"""

from __future__ import annotations

from src.core.candidate import Candidate


class ReasonGenerator:
    """
    Generates recruiter-readable explanations.
    """
    @staticmethod
    def _append_unique(
        destination: list[str],
        source: list[str],
    ) -> None:

        for item in source:

            if item not in destination:

                destination.append(item)

    def generate(
        self,
        candidate: Candidate,
    ) -> Candidate:

        evidence = candidate.evidence

        strengths: list[str] = []

        concerns: list[str] = []

        #######################################################################
        # Aggregate Strengths
        #######################################################################

        self._append_unique(
    strengths,
    evidence.skill.strengths,
)

        self._append_unique(
            strengths,
            evidence.experience.strengths
        )

        self._append_unique(
            strengths,
            evidence.education.strengths
        )

        self._append_unique(
            strengths,
            evidence.certification.strengths
        )

        self._append_unique(
            strengths,
            evidence.signal.strengths
        )

        self._append_unique(
            strengths,
            evidence.integrity.strengths
        )

        #######################################################################
        # Aggregate Concerns
        #######################################################################

        self._append_unique(
    concerns,
    evidence.skill.concerns,
)

        self._append_unique(
            concerns,
            evidence.experience.concerns
        )

        self._append_unique(
            concerns,
            evidence.education.concerns
        )

        self._append_unique(
            concerns,
            evidence.certification.concerns
        )

        self._append_unique(
            concerns,
            evidence.signal.concerns
        )

        self._append_unique(
            concerns,
            evidence.integrity.concerns
        )

        #######################################################################
        # Remove duplicates
        #######################################################################

        

        #######################################################################
        # Build explanation
        #######################################################################

        lines: list[str] = []

        lines.append(

            f"Final Score : {candidate.scores.final_score:.3f}"

        )

        lines.append("")

        if strengths:

            lines.append("Strengths (1-10)")

            lines.append("----------")

            for item in strengths[:10]:

                lines.append(f"✓ {item}")

            lines.append("")

        if concerns:

            lines.append("Concerns (1-8)")

            lines.append("---------")

            for item in concerns[:8]:

                lines.append(f"• {item}")

        candidate.reason = "\n".join(lines)

        return candidate
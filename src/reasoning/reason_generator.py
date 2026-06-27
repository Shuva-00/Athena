"""
Project : Athena
Module  : Reason Generator

Purpose
-------
Generates an explainable hiring reason from analyzed evidence.

Guidelines
----------
- Uses only analyzed evidence.
- No inference.
- No scoring.
- No ranking.
"""

from __future__ import annotations

from src.core.candidate import Candidate
from src.reasoning.template_engine import TemplateEngine


class ReasonGenerator:
    """
    Generates explainable hiring reasons.
    """

    def generate(
        self,
        candidate: Candidate,
    ) -> Candidate:
        """
        Generate a human-readable explanation for a candidate.
        """

        evidence = candidate.evidence

        sections: list[str] = []

        #######################################################################
        # Summary
        #######################################################################

        if evidence.strengths:
            summary = ", ".join(evidence.strengths)
        else:
            summary = "the available candidate evidence"

        sections.append(
            TemplateEngine.SUMMARY_TEMPLATE.format(
                summary=summary
            )
        )

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.strengths:
            sections.append(
                TemplateEngine.STRENGTH_TEMPLATE.format(
                    strengths=", ".join(evidence.strengths)
                )
            )

        #######################################################################
        # Weaknesses
        #######################################################################

        if evidence.weaknesses:
            sections.append(
                TemplateEngine.WEAKNESS_TEMPLATE.format(
                    weaknesses=", ".join(evidence.weaknesses)
                )
            )

        #######################################################################
        # Risks
        #######################################################################

        if evidence.risks:
            sections.append(
                TemplateEngine.RISK_TEMPLATE.format(
                    risks=", ".join(evidence.risks)
                )
            )

        #######################################################################
        # Matched Skills
        #######################################################################

        if evidence.matched_skills:
            sections.append(
                TemplateEngine.MATCHED_SKILLS_TEMPLATE.format(
                    skills=", ".join(evidence.matched_skills)
                )
            )

        #######################################################################
        # Missing Skills
        #######################################################################

        if evidence.missing_skills:
            sections.append(
                TemplateEngine.MISSING_SKILLS_TEMPLATE.format(
                    skills=", ".join(evidence.missing_skills)
                )
            )

        #######################################################################
        # Matched Technologies
        #######################################################################

        if evidence.matched_technologies:
            sections.append(
                TemplateEngine.MATCHED_TECHNOLOGIES_TEMPLATE.format(
                    technologies=", ".join(
                        evidence.matched_technologies
                    )
                )
            )

        #######################################################################
        # Missing Technologies
        #######################################################################

        if evidence.missing_technologies:
            sections.append(
                TemplateEngine.MISSING_TECHNOLOGIES_TEMPLATE.format(
                    technologies=", ".join(
                        evidence.missing_technologies
                    )
                )
            )

        #######################################################################
        # Matched Certifications
        #######################################################################

        if evidence.matched_certifications:
            sections.append(
                TemplateEngine.MATCHED_CERTIFICATIONS_TEMPLATE.format(
                    certifications=", ".join(
                        evidence.matched_certifications
                    )
                )
            )

        #######################################################################
        # Missing Certifications
        #######################################################################

        if evidence.missing_certifications:
            sections.append(
                TemplateEngine.MISSING_CERTIFICATIONS_TEMPLATE.format(
                    certifications=", ".join(
                        evidence.missing_certifications
                    )
                )
            )

        #######################################################################
        # Store Generated Reason
        #######################################################################

        candidate.reason = "\n".join(sections)

        return candidate


###############################################################################
# END OF FILE
###############################################################################
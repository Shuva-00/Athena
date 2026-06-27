"""
Project : Athena
Module  : Template Engine

Purpose
-------
Provides reusable templates for explainable candidate reasoning.

Guidelines
----------
- Contains no business logic.
- Stores reusable templates only.
"""

from __future__ import annotations


class TemplateEngine:
    """
    Provides reasoning templates.
    """

    SUMMARY_TEMPLATE = (
        "The candidate is a strong match because {summary}."
    )

    STRENGTH_TEMPLATE = (
        "Strengths: {strengths}."
    )

    WEAKNESS_TEMPLATE = (
        "Weaknesses: {weaknesses}."
    )

    RISK_TEMPLATE = (
        "Potential risks: {risks}."
    )

    MATCHED_SKILLS_TEMPLATE = (
        "Matched skills: {skills}."
    )

    MISSING_SKILLS_TEMPLATE = (
        "Missing skills: {skills}."
    )

    MATCHED_TECHNOLOGIES_TEMPLATE = (
        "Matched technologies: {technologies}."
    )

    MISSING_TECHNOLOGIES_TEMPLATE = (
        "Missing technologies: {technologies}."
    )

    MATCHED_CERTIFICATIONS_TEMPLATE = (
        "Matched certifications: {certifications}."
    )

    MISSING_CERTIFICATIONS_TEMPLATE = (
        "Missing certifications: {certifications}."
    )


###############################################################################
# END OF FILE
###############################################################################
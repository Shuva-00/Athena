"""
Project : Athena
Module  : Normalization Utilities

Purpose
-------
Provides common text normalization helpers used during preprocessing.
"""

from __future__ import annotations

from src.core.candidate.skills import Skill


def normalize_text(
    text: str,
) -> str:
    """
    Normalize text for comparison.
    """

    return text.strip().lower()


def build_skill_set(
    skills: list[Skill],
) -> set[str]:
    """
    Build normalized skill set.
    """

    return {
        normalize_text(skill.name)
        for skill in skills
        if skill.name.strip()
    }


def build_string_set(
    values: list[str],
) -> set[str]:
    """
    Build normalized string set.
    """

    return {
        normalize_text(value)
        for value in values
        if value.strip()
    }
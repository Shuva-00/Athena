"""
Project : Athena
Module  : Candidate Projects

Purpose
-------
Defines project information associated with a candidate.

Guidelines
----------
- Represents one software project.
- Pure domain model.
- No scoring or retrieval logic.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class Project(AthenaModel):
    """
    Represents a single candidate project.
    """

    title: str = Field(
        ...,
        min_length=1,
        description="Project title.",
    )

    description: str = Field(
        default="",
        description="Project description.",
    )

    technologies: list[str] = Field(
        default_factory=list,
        description="Technologies used in the project.",
    )

    skills: list[str] = Field(
        default_factory=list,
        description="Skills demonstrated by the project.",
    )

    role: str | None = Field(
        default=None,
        description="Candidate's role in the project.",
    )

    duration_months: int | None = Field(
        default=None,
        ge=0,
        description="Project duration in months.",
    )

    organization: str | None = Field(
        default=None,
        description="Organization or client.",
    )

    github_url: str | None = Field(
        default=None,
        description="GitHub repository URL.",
    )

    demo_url: str | None = Field(
        default=None,
        description="Live demo URL.",
    )

    achievements: list[str] = Field(
        default_factory=list,
        description="Project achievements or outcomes.",
    )

    keywords: list[str] = Field(
        default_factory=list,
        description="Extracted project keywords.",
    )

    is_open_source: bool = Field(
        default=False,
        description="Whether the project is open source.",
    )

    is_deployed: bool = Field(
        default=False,
        description="Whether the project has a live deployment.",
    )


###############################################################################
# END OF FILE
###############################################################################
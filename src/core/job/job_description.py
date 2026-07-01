"""
Project : Athena
Module  : Job Description

Purpose
-------
Represents a job description in structured form.

Guidelines
----------
- Pure domain model.
- No parsing logic.
- No ranking logic.
"""

from __future__ import annotations

from pydantic import Field

from src.core.model import AthenaModel


class JobDescription(AthenaModel):
    """
    Structured representation of a job description.
    """

    title: str = Field(
        default="",
        description="Job title.",
    )

    description: str = Field(
        default="",
        description="Complete job description.",
    )

    responsibilities: list[str] = Field(
        default_factory=list,
        description="Primary responsibilities.",
    )

    required_skills: list[str] = Field(
        default_factory=list,
        description="Required skills.",
    )

    preferred_skills: list[str] = Field(
        default_factory=list,
        description="Preferred skills.",
    )

    technologies: list[str] = Field(
        default_factory=list,
        description="Technologies mentioned.",
    )

    minimum_degree: list[str] = Field(
        default_factory=list,
        description="Minimum educational qualifications.",
    )

    certifications: list[str] = Field(
        default_factory=list,
        description="Desired certifications.",
    )

    experience_years: float | None = Field(
        default=None,
        description="Minimum years of experience.",
    )

    location: str | None = Field(
        default=None,
        description="Job location.",
    )

    employment_type: str | None = Field(
        default=None,
        description="Employment type.",
    )

    work_mode: str | None = Field(
        default=None,
        description="Remote, hybrid or onsite.",
    )
        ###########################################################################
    # Text Representation
    ###########################################################################

    def to_text(self) -> str:
        """
        Build a canonical textual representation of the job description
        for retrieval and semantic search.
        """

        parts: list[str] = []

        #######################################################################
        # Basic Information
        #######################################################################

        if self.title:
            parts.append(self.title)

        if self.description:
            parts.append(self.description)

        #######################################################################
        # Responsibilities
        #######################################################################

        parts.extend(self.responsibilities)

        #######################################################################
        # Skills
        #######################################################################

        parts.extend(self.required_skills)
        parts.extend(self.preferred_skills)

        #######################################################################
        # Technologies
        #######################################################################

        parts.extend(self.technologies)

        #######################################################################
        # Qualifications
        #######################################################################

        parts.extend(self.minimum_degree)

        #######################################################################
        # Certifications
        #######################################################################

        parts.extend(self.certifications)

        #######################################################################
        # Experience
        #######################################################################

        if self.experience_years is not None:
            parts.append(
                f"{self.experience_years} years experience"
            )

        #######################################################################
        # Location
        #######################################################################

        if self.location:
            parts.append(self.location)

        #######################################################################
        # Employment
        #######################################################################

        if self.employment_type:
            parts.append(self.employment_type)

        if self.work_mode:
            parts.append(self.work_mode)

        return "\n".join(
    part.strip()
    for part in parts
    if part.strip()
)
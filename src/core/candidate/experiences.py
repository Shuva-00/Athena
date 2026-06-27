"""
Project : Athena
Module  : Candidate Experiences

Purpose
-------
Defines a candidate's professional work experience.

Guidelines
----------
- Represents one employment experience.
- Pure domain model.
- No ranking or business logic.
"""

from __future__ import annotations

from datetime import date

from pydantic import Field

from src.core.enums import EmploymentType
from src.core.model import AthenaModel


class Experience(AthenaModel):
    """
    Represents one professional work experience.
    """

    company: str = Field(
        ...,
        min_length=1,
        description="Company or organization name.",
    )

    job_title: str = Field(
        ...,
        min_length=1,
        description="Job title held by the candidate.",
    )

    employment_type: EmploymentType | None = Field(
        default=None,
        description="Employment type (Full-time, Internship, Contract, etc.).",
    )

    location: str | None = Field(
        default=None,
        description="Work location.",
    )

    start_date: date | None = Field(
        default=None,
        description="Employment start date.",
    )

    end_date: date | None = Field(
        default=None,
        description="Employment end date. None indicates current employment.",
    )

    is_current: bool = Field(
        default=False,
        description="Whether this is the candidate's current role.",
    )
    
    industry: str | None = Field(
    default=None,
    description="Industry of the company.",
)

    company_size: str | None = Field(
    default=None,
    description="Company size.",
)

    duration_months: int | None = Field(
    default=None,
    ge=0,
    description="Duration of employment in months.",
)
    
    responsibilities: list[str] = Field(
        default_factory=list,
        description="Major responsibilities.",
    )

    achievements: list[str] = Field(
        default_factory=list,
        description="Key achievements.",
    )

    technologies: list[str] = Field(
        default_factory=list,
        description="Technologies used.",
    )

    skills: list[str] = Field(
        default_factory=list,
        description="Skills demonstrated.",
    )

    keywords: list[str] = Field(
        default_factory=list,
        description="Extracted keywords.",
    )
    
    impact_metrics: dict[str, str] = Field(
        default_factory=dict,
        description="Structured measurable impact (e.g. {'latency_reduction':'35%'}).",
    )
    


###############################################################################
# END OF FILE
###############################################################################
"""
Project : Athena
Module  : Candidate Profile

Purpose
-------
Defines the normalized profile information of a candidate.

Guidelines
----------
- Represents only profile-level information.
- Does not contain education, projects, scores, or evidence.
- Pure domain model.
"""

from __future__ import annotations
from pydantic import HttpUrl
from pydantic import EmailStr, Field

from src.core.model import AthenaModel


class CandidateProfile(AthenaModel):
    """
    Represents the normalized profile of a candidate.
    """

    full_name: str | None = Field(
        default=None,
        description="Candidate full name.",
    )

    headline: str | None = Field(
        default=None,
        description="Professional headline.",
    )
    
    credential_url: HttpUrl | None = Field(
    default=None,
    description="Credential verification URL.",
    ) 
    summary: str | None = Field(
        default=None,
        description="Professional summary.",
    )

    email: EmailStr | None = Field(
        default=None,
        description="Email address.",
    )

    phone: str | None = Field(
        default=None,
        description="Phone number.",
    )

    location: str | None = Field(
        default=None,
        description="Current location.",
    )

    linkedin_url: HttpUrl | None = Field(
        default=None,
        description="LinkedIn profile URL.",
    )

    github_url: HttpUrl| None = Field(
        default=None,
        description="GitHub profile URL.",
    )

    portfolio_url: HttpUrl | None = Field(
        default=None,
        description="Portfolio website.",
    )

    total_experience_months: int | None = Field(
        default=None,
        ge=0,
        description="Total professional experience in months.",
    )

    primary_skills: list[str] = Field(
        default_factory=list,
        description="Primary technical skills.",
    )

    secondary_skills: list[str] = Field(
        default_factory=list,
        description="Secondary technical skills.",
    )

    languages: list[str] = Field(
        default_factory=list,
        description="Languages known.",
    )

    certifications: list[str] = Field(
        default_factory=list,
        description="Professional certifications.",
    )

    keywords: list[str] = Field(
        default_factory=list,
        description="Profile keywords extracted during preprocessing.",
    )


###############################################################################
# END OF FILE
###############################################################################
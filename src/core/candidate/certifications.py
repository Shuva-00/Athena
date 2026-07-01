"""
Project : Athena
Module  : Candidate Certifications

Purpose
-------
Defines professional certifications held by a candidate.

Guidelines
----------
- Represents one certification.
- Pure domain model.
- No business logic.
- No scoring logic.
"""

from __future__ import annotations

from datetime import date

from pydantic import Field

from src.core.model import AthenaModel


class Certification(AthenaModel):
    """
    Represents one professional certification.
    """

    name: str = Field(
        ...,
        min_length=1,
        description="Certification name.",
    )

    issuer: str | None = Field(
        default=None,
        description="Issuing organization.",
    )

    issue_date: date | None = Field(
        default=None,
        description="Certification issue date.",
    )

    expiry_date: date | None = Field(
        default=None,
        description="Certification expiry date.",
    )

    credential_id: str | None = Field(
        default=None,
        description="Credential or certificate ID.",
    )


    credential_url: str | None = Field(
        default=None,
        description="Credential verification URL.",
    )
    verified: bool = Field(
    default=False,
    description="Whether the certification has been verified.",
)

    skills: list[str] = Field(
    default_factory=list,
    description="Skills covered by the certification.",
)

    level: str | None = Field(
    default=None,
    description="Certification level (Associate, Professional, Expert, etc.).",
)

    keywords: list[str] = Field(
    default_factory=list,
    description="Extracted certification keywords.",
)

###############################################################################
# END OF FILE
###############################################################################
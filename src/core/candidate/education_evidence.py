from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class EducationEvidence(BaseModel):
    """
    Raw evidence extracted from candidate education.
    """

    model_config = ConfigDict(
        frozen=False,
        extra="forbid",
    )

    highest_degree: str = ""

    education_field: str = ""

    relevant_degree: bool = False

    institution_name: str = ""

    institution_tier: int = 0

    graduation_year: int | None = None

    cgpa: float | None = None

    education_score: float = 0.0
from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class ExperienceEvidence(BaseModel):
    """
    Raw evidence extracted from candidate work experience.
    """

    model_config = ConfigDict(
        frozen=False,
        extra="forbid",
    )

    total_experience_months: int = 0

    relevant_experience_months: int = 0

    current_role_match: bool = False

    promotion_count: int = 0

    lateral_move_count: int = 0

    job_hop_count: int = 0

    average_job_tenure_months: float = 0.0

    longest_job_tenure_months: int = 0

    shortest_job_tenure_months: int = 0

    employment_gap_months: int = 0

    relevant_company_count: int = 0

    leadership_roles: int = 0

    senior_titles: int = 0

    management_roles: int = 0

    startup_experience: int = 0

    enterprise_experience: int = 0
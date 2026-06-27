from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class BehaviourEvidence(BaseModel):
    """
    Raw behavioural evidence extracted from the candidate profile.
    """

    model_config = ConfigDict(
        frozen=False,
        extra="forbid",
    )

    recruiter_interest_score: float = 0.0

    profile_views: int = 0

    recruiter_contacts: int = 0

    interview_invitations: int = 0

    interview_completion_rate: float = 0.0

    response_rate: float = 0.0

    response_time_hours: float = 0.0

    availability_score: float = 0.0

    profile_completeness: float = 0.0

    activity_score: float = 0.0

    platform_engagement: float = 0.0

    recent_activity_days: int = 0

    profile_verified: bool = False

    open_to_work: bool = False
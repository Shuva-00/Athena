from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class SkillEvidence(BaseModel):
    """
    Raw evidence extracted from candidate skills.
    """

    model_config = ConfigDict(
        frozen=False,
        extra="forbid",
    )

    total_candidate_skills: int = 0

    total_required_skills: int = 0

    exact_skill_matches: int = 0

    semantic_skill_matches: int = 0

    missing_required_skills: int = 0

    critical_skill_matches: int = 0

    critical_skill_missing: int = 0

    rare_skill_matches: int = 0

    skills_supported_by_experience: int = 0

    skills_supported_by_projects: int = 0

    duplicate_skill_mentions: int = 0
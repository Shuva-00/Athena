from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class ProjectEvidence(BaseModel):
    """
    Raw evidence extracted from candidate projects.
    """

    model_config = ConfigDict(
        frozen=False,
        extra="forbid",
    )

    total_projects: int = 0

    relevant_projects: int = 0

    production_projects: int = 0

    deployed_projects: int = 0

    open_source_projects: int = 0

    ai_ml_projects: int = 0

    backend_projects: int = 0

    frontend_projects: int = 0

    cloud_projects: int = 0

    project_keywords_matched: int = 0

    measurable_impact_projects: int = 0

    quantified_achievements: int = 0

    average_project_description_length: float = 0.0

    project_complexity_score: float = 0.0

    project_recency_score: float = 0.0

    teamwork_projects: int = 0

    leadership_projects: int = 0
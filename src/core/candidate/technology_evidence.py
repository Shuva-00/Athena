from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict


class TechnologyEvidence(BaseModel):
    """
    Raw evidence extracted from candidate technologies.
    """

    model_config = ConfigDict(
        frozen=False,
        extra="forbid",
    )

    total_technologies: int = 0

    distinct_technologies: int = 0

    programming_languages: int = 0

    frameworks: int = 0

    databases: int = 0

    cloud_services: int = 0

    devops_tools: int = 0

    ai_ml_tools: int = 0

    vector_database_tools: int = 0

    llm_frameworks: int = 0

    modern_stack_technologies: int = 0

    technologies_used_in_experience: int = 0

    technologies_used_in_projects: int = 0

    repeated_technology_mentions: int = 0

    unsupported_technologies: int = 0

    technology_diversity_score: float = 0.0

    technology_depth_score: float = 0.0
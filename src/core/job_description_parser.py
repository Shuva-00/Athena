"""
Project : Athena
Module  : Job Description Parser
"""

from __future__ import annotations

import re

from src.core.job.job_description import JobDescription


class JobDescriptionParser:
    """
    Converts raw job description text into a JobDescription model.
    """

    def parse(
        self,
        text: str,
    ) -> JobDescription:

        title = ""

        lines = [
            line.strip()
            for line in text.splitlines()
            if line.strip()
        ]

        if lines:
            title = lines[0]

        experience = 0

        match = re.search(
            r"(\d+)\s*[–-]\s*(\d+)\s*years",
            text,
            flags=re.IGNORECASE,
        )

        if match:
            experience = int(match.group(1))

        return JobDescription(
            title=title,
            description=text,
            responsibilities=[],
            required_skills=[],
            preferred_skills=[],
            technologies=[],
            required_degree=["BACHELOR"],
            certifications=[],
            experience_years=experience,
            location="",
            employment_type="FULL_TIME",
            work_mode="HYBRID",
        )
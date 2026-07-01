"""
Project : Athena
Module  : Candidate Parser

Purpose
-------
Parses one raw candidate record into a fully populated
Athena Candidate domain object.
"""

from __future__ import annotations

from typing import Any

from src.core.candidate import Candidate

from .profile_parser import ProfileParser
from .education_parser import EducationParser
from .experience_parser import ExperienceParser
from .project_parser import ProjectParser
from .skill_parser import SkillParser
from .certification_parser import CertificationParser
from .language_parser import LanguageParser
from .signals_parser import SignalsParser


class CandidateParser:
    """
    Orchestrates parsing of an entire candidate record.
    """

    def __init__(self) -> None:
        self.profile_parser = ProfileParser()
        self.education_parser = EducationParser()
        self.experience_parser = ExperienceParser()
        self.project_parser = ProjectParser()
        self.skill_parser = SkillParser()
        self.certification_parser = CertificationParser()
        self.language_parser = LanguageParser()
        self.signals_parser = SignalsParser()

    def parse(
        self,
        candidate_data: dict[str, Any],
    ) -> Candidate:
        """
        Convert one raw candidate dictionary into a Candidate object.
        """

        experiences = self.experience_parser.parse(
            candidate_data.get("career_history", [])
        )

        projects = self.project_parser.parse(
            experiences
        )

        return Candidate(
            candidate_id=candidate_data["candidate_id"],

            profile=self.profile_parser.parse(
                candidate_data.get("profile", {})
            ),

            education=self.education_parser.parse(
                candidate_data.get("education", [])
            ),

            experiences=experiences,

            projects=projects,

            skills=self.skill_parser.parse(
                candidate_data.get("skills", [])
            ),

            certifications=self.certification_parser.parse(
                candidate_data.get("certifications", [])
            ),

            languages=self.language_parser.parse(
                candidate_data.get("languages", [])
            ),

            signals=self.signals_parser.parse(
                candidate_data.get("redrob_signals", {})
            ),
        )


###############################################################################
# END OF FILE
###############################################################################
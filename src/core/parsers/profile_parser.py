"""
Project : Athena
Module  : Project Parser

Purpose
-------
Extracts basic project information from candidate experience
descriptions.

Guidelines
----------
- Uses deterministic rules only.
- No AI.
- No embeddings.
- No ranking logic.
"""

from __future__ import annotations

import re

from src.core.candidate import Experience, Project


class ProjectParser:
    """
    Builds preliminary Project objects from experience descriptions.
    """

    SENTENCE_SPLITTER = re.compile(r"[.!?]\s+|\n+")

    MIN_LENGTH = 20

    MAX_SENTENCES = 5

    def parse(
        self,
        experiences: list[Experience],
    ) -> list[Project]:
        """
        Extract projects from candidate experience descriptions.
        """

        projects: list[Project] = []

        for experience in experiences:

            description = experience.description

            if not description:
                continue

            sentences = self.SENTENCE_SPLITTER.split(description)

            count = 1

            for sentence in sentences:

                sentence = sentence.strip()

                if len(sentence) < self.MIN_LENGTH:
                    continue

                project = Project(

                    title=f"{experience.company} Project {count}",

                    description=sentence,

                    organization=experience.company,

                    technologies=[],

                    achievements=[],

                    keywords=[],
                )

                projects.append(project)

                count += 1

                if count > self.MAX_SENTENCES:
                    break

        return projects


###############################################################################
# END OF FILE
###############################################################################
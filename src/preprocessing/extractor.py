
"""
Project : Athena
Module  : Candidate Extractor

Purpose
-------
Extracts structured information from candidate
profiles, experiences, and projects.

Guidelines
----------
- Operates on Candidate objects.
- Uses deterministic extraction.
- No ranking logic.
"""

from __future__ import annotations

import re

from src.core.candidate import Candidate


class Extractor:
    """
    Extracts structured information from candidate text.
    """

    TECHNOLOGIES = {
        "python",
        "java",
        "c++",
        "c",
        "javascript",
        "typescript",
        "react",
        "angular",
        "vue",
        "node",
        "fastapi",
        "django",
        "flask",
        "spring",
        "aws",
        "azure",
        "gcp",
        "docker",
        "kubernetes",
        "postgresql",
        "mysql",
        "mongodb",
        "redis",
        "git",
        "linux",
    }

    ACTION_VERBS = {
        "built",
        "developed",
        "implemented",
        "created",
        "designed",
        "optimized",
        "led",
        "managed",
        "improved",
        "automated",
        "deployed",
        "migrated",
        "integrated",
    }

    METRIC_PATTERN = re.compile(
        r"\b\d+(?:\.\d+)?\s*(?:%|percent|ms|million|billion|k|x)\b",
        re.IGNORECASE,
    )

    WORD_PATTERN = re.compile(r"[A-Za-z0-9+#.]+")

    def extract(
        self,
        candidate: Candidate,
    ) -> Candidate:
        """
        Enrich one candidate.
        """

        self._extract_keywords(candidate)
        self._extract_technologies(candidate)
        self._extract_achievements(candidate)

        return candidate

    def _extract_keywords(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Extract keywords from profile summary,
        experiences, and projects. 
        """

        texts = []

        if candidate.profile.summary:
            texts.append(candidate.profile.summary)

        for experience in candidate.experiences:
            s=" ".join(
                  experience.responsibilities
)
            if s:
                texts.append(s)

        for project in candidate.projects:

            if project.title:
                texts.append(project.title)

            if project.description:
                texts.append(project.description)

        keywords = set()

        for text in texts:

            for word in self.WORD_PATTERN.findall(
                text.lower()
            ):

                if len(word) >= 3:
                    keywords.add(word)

        candidate.metadata["keywords"] = sorted(
            keywords
        )

    def _extract_technologies(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Extract technology mentions from profile,
experiences, and projects.
        """

        technologies = set()

        texts = []

        if candidate.profile.summary:
            texts.append(candidate.profile.summary)

        for experience in candidate.experiences:
            s=" ".join(
                    experience.responsibilities)
            if s:
             texts.append(s)

        for project in candidate.projects:

            if project.title:
                texts.append(project.title)

            if project.description:
                texts.append(project.description)

        for text in texts:

           words = {
                word.lower()
                for word in self.WORD_PATTERN.findall(
                    text
                )
           }
        

           technologies.update(
                words.intersection(
                    self.TECHNOLOGIES
                )
            )

        candidate.metadata["technologies"] = sorted(
            technologies
        )

    def _extract_achievements(
        self,
        candidate: Candidate,
    ) -> None:
        """
        Extract quantified achievements.
        """

        achievements = []

    ###########################################################################
    # Experience
    ###########################################################################

        for experience in candidate.experiences:

            s=" ".join(
                  experience.responsibilities
)
            if not s:
                continue

            sentences = re.split(
                r"[.!?]",
                s,
            )

            for sentence in sentences:

                lower = sentence.lower()

                if any(
                    verb in lower
                    for verb in self.ACTION_VERBS
               ):

                    if self.METRIC_PATTERN.search(
                        sentence
                    ):

                        achievements.append(
                            sentence.strip()
                        )

    ###########################################################################
    # Projects
    ###########################################################################

        for project in candidate.projects:

            if not project.description:
                continue

            sentences = re.split(
                r"[.!?]",
                project.description,
           )

            for sentence in sentences:

                lower = sentence.lower()

                if any(
                    verb in lower
                    for verb in self.ACTION_VERBS
                ):

                    if self.METRIC_PATTERN.search(
                        sentence
                    ):

                        achievements.append(
                            sentence.strip()
                        )

        candidate.metadata["achievements"] = achievements

###############################################################################
# END OF FILE
###############################################################################
"""
Project : Athena
Module  : Debug Report

Purpose
-------
Produces a complete pipeline debug report for one candidate.

Guidelines
----------
- Read-only.
- No scoring.
- No ranking.
- No mutation.
- Displays pipeline outputs only.
"""

from __future__ import annotations

from src.core.candidate.entity import Candidate


class DebugReport:
    """
    Produces a complete debugging report for a candidate.
    """

    ###########################################################################
    # Public API
    ###########################################################################

    def generate(
        self,
        candidate: Candidate,
    ) -> str:
        """
        Generate a complete pipeline debugging report.
        """

        lines: list[str] = []

        self._header(
            lines,
            candidate,
        )

        self._candidate_section(
            lines,
            candidate,
        )

        self._parser_section(
            lines,
            candidate,
        )

        self._evidence_section(
            lines,
            candidate,
        )

        self._analysis_section(
            lines,
            candidate,
        )

        self._score_section(
            lines,
            candidate,
        )

        self._ranking_section(
            lines,
            candidate,
        )

        self._reason_section(
            lines,
            candidate,
        )

        self._warning_section(
            lines,
            candidate,
        )

        self._footer(
            lines,
        )

        return "\n".join(lines)

    ###########################################################################
    # Header
    ###########################################################################

    def _header(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        lines.extend(
            [
                "=" * 78,
                "ATHENA DEBUG REPORT",
                "=" * 78,
                "",
            ]
        )

    ###########################################################################
    # Candidate
    ###########################################################################

    def _candidate_section(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        lines.extend(
            [
                "CANDIDATE",
                "-" * 78,
                f"Candidate ID      : {candidate.candidate_id}",
                f"Rank              : {candidate.scores.rank}",
                f"Semantic Score    : {candidate.scores.semantic_score:.4f}",
                f"Feature Score     : {candidate.scores.feature_score:.4f}",
                f"Final Score       : {candidate.scores.final_score:.4f}",
                "",
            ]
        )

    ###########################################################################
    # Parser Summary
    ###########################################################################

    def _parser_section(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        lines.extend(
            [
                "PARSER SUMMARY",
                "-" * 78,
                f"Skills Parsed         : {len(candidate.skills)}",
                f"Experiences Parsed    : {len(candidate.experiences)}",
                f"Education Parsed      : {len(candidate.education)}",
                f"Certifications Parsed : {len(candidate.certifications)}",
                f"Projects Parsed       : {len(candidate.projects)}",
                "",
            ]
        )

        ###########################################################################
    # Evidence Summary
    ###########################################################################

    def _evidence_section(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        evidence = candidate.evidence

        #######################################################################
        # Skill
        #######################################################################

        skill = evidence.skill

        lines.extend(
            [
                "EVIDENCE",
                "-" * 78,
                "",
                "[Skill]",
                f"Matched Skills        : {skill.exact_matches}",
                f"Required Skills       : {skill.required_total}",
                f"Candidate Skills      : {skill.candidate_total}",
                f"Missing Skills        : {len(skill.missing_required)}",
                f"Additional Skills     : {len(skill.additional_skills)}",
                f"Confidence            : {skill.confidence:.4f}",
                "",
            ]
        )

        #######################################################################
        # Experience
        #######################################################################

        experience = evidence.experience

        lines.extend(
            [
                "[Experience]",
                f"Total Roles           : {experience.total_roles}",
                f"Relevant Roles        : {experience.relevant_role_count}",
                f"Experience (Months)   : {experience.total_experience_months}",
                f"Relevant Experience   : {experience.relevant_experience_months}",
                f"Current Role          : {experience.current_role_months}",
                f"Leadership Roles      : {experience.leadership_role_count}",
                f"Leadership Months     : {experience.leadership_experience_months}",
                f"Average Tenure        : {experience.average_tenure_months:.2f}",
                f"Confidence            : {experience.confidence:.4f}",
                "",
            ]
        )

        #######################################################################
        # Education
        #######################################################################

        education = evidence.education

        lines.extend(
            [
                "[Education]",
                f"Highest Degree        : {education.highest_degree}",
                f"Minimum Degree        : {education.minimum_degree_met}",
                f"Relevant Degrees      : {education.relevant_degree_count}",
                f"Highest CGPA          : {education.highest_cgpa}",
                f"Average CGPA          : {education.average_cgpa}",
                f"Institution Tier      : {education.institution_tier}",
                f"Research Projects     : {education.research_project_count}",
                f"Publications          : {education.research_publication_count}",
                f"Confidence            : {education.confidence:.4f}",
                "",
            ]
        )

        #######################################################################
        # Certification
        #######################################################################

        certification = evidence.certification

        lines.extend(
            [
                "[Certification]",
                f"Total                 : {certification.total_certifications}",
                f"Matched               : {certification.matched_total}",
                f"Verified              : {certification.verified_count}",
                f"Recent                : {certification.recent_certifications}",
                f"Relevance             : {certification.certification_relevance:.4f}",
                f"Confidence            : {certification.confidence:.4f}",
                "",
            ]
        )

        #######################################################################
        # Signal
        #######################################################################

        signal = evidence.signal

        lines.extend(
            [
                "[Signal]",
                f"Open To Work          : {signal.open_to_work}",
                f"Notice Period         : {signal.notice_period_days}",
                f"Engagement            : {signal.engagement_score:.4f}",
                f"Responsiveness        : {signal.responsiveness_score:.4f}",
                f"Assessment            : {signal.assessment_score:.4f}",
                f"Profile Completeness  : {signal.profile_completeness:.4f}",
                f"Confidence            : {signal.confidence:.4f}",
                "",
            ]
        )

        #######################################################################
        # Integrity
        #######################################################################

        integrity = evidence.integrity

        lines.extend(
            [
                "[Integrity]",
                f"Missing Fields        : {integrity.missing_required_fields}",
                f"Duplicate Skills      : {integrity.duplicate_skills}",
                f"Duplicate Projects    : {integrity.duplicate_projects}",
                f"Duplicate Certificates: {integrity.duplicate_certifications}",
                f"Timeline Issues       : {integrity.timeline_inconsistencies}",
                f"Experience Issues     : {integrity.experience_inconsistencies}",
                f"Confidence            : {integrity.confidence:.4f}",
                "",
            ]
        )

    ###########################################################################
    # Analyzer Summary
    ###########################################################################

    def _analysis_section(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        evidence = candidate.evidence

        lines.extend(
            [
                "ANALYZER SUMMARY",
                "-" * 78,
            ]
        )

        modules = [
            ("Skill", evidence.skill),
            ("Experience", evidence.experience),
            ("Education", evidence.education),
            ("Certification", evidence.certification),
            ("Signal", evidence.signal),
            ("Integrity", evidence.integrity),
        ]

        for name, module in modules:

            lines.append("")
            lines.append(f"[{name}]")

            if module.strengths:

                lines.append("Strengths")

                for item in module.strengths:

                    lines.append(f"  ✓ {item}")

            else:

                lines.append("Strengths : None")

            if module.concerns:

                lines.append("Concerns")

                for item in module.concerns:

                    lines.append(f"  • {item}")

            else:

                lines.append("Concerns : None")

        lines.append("")

        ###########################################################################
    # Feature Scores
    ###########################################################################

    def _score_section(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        features = candidate.features

        lines.extend(
            [
                "FEATURE SCORES",
                "-" * 78,
                f"Skill Score          : {features.skill_score:.4f}",
                f"Experience Score     : {features.experience_score:.4f}",
                f"Education Score      : {features.education_score:.4f}",
                f"Certification Score  : {features.certification_score:.4f}",
                f"Signal Score         : {features.signal_score:.4f}",
                f"Integrity Score      : {features.integrity_score:.4f}",
                "",
                f"Overall Feature Score: {features.feature_score:.4f}",
                "",
            ]
        )

    ###########################################################################
    # Ranking Summary
    ###########################################################################

    def _ranking_section(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        scores = candidate.scores

        lines.extend(
            [
                "RANKING",
                "-" * 78,
                f"Semantic Score       : {scores.semantic_score:.4f}",
                f"Feature Score        : {scores.feature_score:.4f}",
                f"Final Score          : {scores.final_score:.4f}",
                f"Rank                 : {scores.rank}",
                f"Percentile           : {scores.percentile:.2f}",
                "",
            ]
        )

    ###########################################################################
    # Generated Reason
    ###########################################################################

    def _reason_section(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        lines.extend(
            [
                "GENERATED REASON",
                "-" * 78,
            ]
        )

        if candidate.reason:

            for line in candidate.reason.splitlines():

                lines.append(line)

        else:

            lines.append(
                "No reasoning generated."
            )

        lines.append("")

        ###########################################################################
    # Warning Summary
    ###########################################################################

    def _warning_section(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        lines.extend(
            [
                "WARNINGS",
                "-" * 78,
            ]
        )

        warnings: list[str] = []

        #######################################################################
        # Parser
        #######################################################################

        if not candidate.skills:
            warnings.append(
                "No skills parsed."
            )

        if not candidate.experiences:
            warnings.append(
                "No professional experience parsed."
            )

        if not candidate.education:
            warnings.append(
                "No education parsed."
            )

        #######################################################################
        # Skill
        #######################################################################

        skill = candidate.evidence.skill

        if (
            skill.required_total > 0
            and skill.exact_matches == 0
        ):
            warnings.append(
                "No required skills matched."
            )

        #######################################################################
        # Experience
        #######################################################################

        experience = candidate.evidence.experience

        if (
            experience.total_experience_months > 0
            and experience.relevant_experience_months == 0
        ):
            warnings.append(
                "No relevant experience identified."
            )

        #######################################################################
        # Education
        #######################################################################

        education = candidate.evidence.education

        if not education.minimum_degree_met:
            warnings.append(
                "Minimum degree not satisfied."
            )

        #######################################################################
        # Integrity
        #######################################################################

        integrity = candidate.evidence.integrity

        issues = (

            integrity.missing_required_fields

            + integrity.duplicate_skills

            + integrity.duplicate_projects

            + integrity.duplicate_certifications

            + integrity.timeline_inconsistencies

            + integrity.experience_inconsistencies

        )

        if issues > 0:

            warnings.append(
                f"{issues} integrity issue(s) detected."
            )

        #######################################################################
        # Feature Scores
        #######################################################################

        features = candidate.features

        scores = {

            "Skill": features.skill_score,

            "Experience": features.experience_score,

            "Education": features.education_score,

            "Certification": features.certification_score,

            "Signal": features.signal_score,

            "Integrity": features.integrity_score,

            "Feature": features.feature_score,

            "Final": candidate.scores.final_score,

        }

        for name, value in scores.items():

            if not (0.0 <= value <= 1.0):

                warnings.append(
                    f"{name} score outside [0,1]."
                )

        #######################################################################
        # Output
        #######################################################################

        if warnings:

            for warning in warnings:

                lines.append(
                    f"⚠ {warning}"
                )

        else:

            lines.append(
                "No warnings detected."
            )

        lines.append("")

    ###########################################################################
    # Footer
    ###########################################################################

    def _footer(
        self,
        lines: list[str],
    ) -> None:

        lines.extend(
            [
                "=" * 78,
                "END OF ATHENA DEBUG REPORT",
                "=" * 78,
            ]
        )
"""
Project : Athena
Module  : Score Audit Report

Purpose
-------
Produces a detailed audit explaining exactly how a candidate's final score
was produced.

Guidelines
----------
- Read-only.
- No scoring.
- No ranking.
- No mutation.
- Uses already computed scores.
"""

from __future__ import annotations

from src.config import settings
from src.core.candidate.entity import Candidate


class ScoreAuditReport:
    """
    Produces a detailed score audit for a candidate.
    """

    ###########################################################################
    # Public API
    ###########################################################################

    def generate(
        self,
        candidate: Candidate,
    ) -> str:
        """
        Generate a complete score audit report.
        """

        lines: list[str] = []

        self._header(
            lines,
            candidate,
        )

        self._semantic_section(
            lines,
            candidate,
        )

        self._feature_scores(
            lines,
            candidate,
        )

        self._feature_fusion(
            lines,
            candidate,
        )

        self._final_fusion(
            lines,
            candidate,
        )

        self._validation_checks(
            lines,
            candidate,
        )

        self._evidence_summary(
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
                "ATHENA SCORE AUDIT REPORT",
                "=" * 78,
                "",
                f"Candidate ID      : {candidate.candidate_id}",
                f"Rank              : {candidate.scores.rank}",
                f"Final Score       : {candidate.scores.final_score:.4f}",
                "",
            ]
        )

    ###########################################################################
    # Semantic Score
    ###########################################################################

    def _semantic_section(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        fusion = settings.weights.fusion

        semantic_score = candidate.scores.semantic_score

        contribution = (
            semantic_score
            * fusion.cross_encoder
        )

        lines.extend(
            [
                "SEMANTIC SCORE",
                "-" * 78,
                f"Raw Score         : {semantic_score:.4f}",
                f"Fusion Weight     : {fusion.cross_encoder:.4f}",
                f"Contribution      : {contribution:.4f}",
                "",
            ]
        )

        ###########################################################################
    # Feature Scores
    ###########################################################################

    def _feature_scores(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        features = candidate.features

        lines.extend(
            [
                "FEATURE SCORES",
                "-" * 78,
                f"Skill Score      : {features.skill_score:.4f}",
                f"Experience Score : {features.experience_score:.4f}",
                f"Education Score  : {features.education_score:.4f}",
                f"Certification    : {features.certification_score:.4f}",
                f"Signal Score     : {features.signal_score:.4f}",
                f"Integrity Score  : {features.integrity_score:.4f}",
                "",
            ]
        )

    ###########################################################################
    # Feature Fusion
    ###########################################################################

    def _feature_fusion(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        weights = settings.weights.feature_fusion

        features = candidate.features

        skill = (
            features.skill_score
            * weights.skill
        )

        experience = (
            features.experience_score
            * weights.experience
        )

        education = (
            features.education_score
            * weights.education
        )

        certification = (
            features.certification_score
            * weights.certification
        )

        signal = (
            features.signal_score
            * weights.signal
        )

        integrity = (
            features.integrity_score
            * weights.integrity
        )

        computed_feature_score = (

            skill

            + experience

            + education

            + certification

            + signal

            + integrity

        )

        lines.extend(
            [
                "FEATURE FUSION",
                "-" * 78,
                f"Skill          : {features.skill_score:.4f} × {weights.skill:.2f}"
                f" = {skill:.4f}",
                f"Experience     : {features.experience_score:.4f} × {weights.experience:.2f}"
                f" = {experience:.4f}",
                f"Education      : {features.education_score:.4f} × {weights.education:.2f}"
                f" = {education:.4f}",
                f"Certification  : {features.certification_score:.4f} × {weights.certification:.2f}"
                f" = {certification:.4f}",
                f"Signal         : {features.signal_score:.4f} × {weights.signal:.2f}"
                f" = {signal:.4f}",
                f"Integrity      : {features.integrity_score:.4f} × {weights.integrity:.2f}"
                f" = {integrity:.4f}",
                "",
                f"Computed Feature Score : {computed_feature_score:.4f}",
                f"Stored Feature Score   : {features.feature_score:.4f}",
                "",
            ]
        )

        ###########################################################################
    # Final Score Fusion
    ###########################################################################

    def _final_fusion(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        fusion = settings.weights.fusion

        semantic = candidate.scores.semantic_score

        feature = candidate.features.feature_score

        semantic_contribution = (
            semantic
            * fusion.cross_encoder
        )

        feature_contribution = (
            feature
            * fusion.feature_score
        )

        computed_final_score = (

            semantic_contribution

            + feature_contribution

        )

        lines.extend(
            [
                "FINAL SCORE FUSION",
                "-" * 78,
                f"Semantic Score     : {semantic:.4f}",
                f"Semantic Weight    : {fusion.cross_encoder:.2f}",
                f"Semantic Contribution : {semantic_contribution:.4f}",
                "",
                f"Feature Score      : {feature:.4f}",
                f"Feature Weight     : {fusion.feature_score:.2f}",
                f"Feature Contribution : {feature_contribution:.4f}",
                "",
                f"Computed Final Score : {computed_final_score:.4f}",
                f"Stored Final Score   : {candidate.scores.final_score:.4f}",
                "",
            ]
        )

    ###########################################################################
    # Validation Checks
    ###########################################################################

    def _validation_checks(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        lines.extend(
            [
                "VALIDATION CHECKS",
                "-" * 78,
            ]
        )

        features = candidate.features

        feature_weights = settings.weights.feature_fusion

        fusion_weights = settings.weights.fusion

        #######################################################################
        # Feature Score Range
        #######################################################################

        feature_scores = {
            "Skill": features.skill_score,
            "Experience": features.experience_score,
            "Education": features.education_score,
            "Certification": features.certification_score,
            "Signal": features.signal_score,
            "Integrity": features.integrity_score,
            "Feature": features.feature_score,
        }

        for name, score in feature_scores.items():

            if 0.0 <= score <= 1.0:

                lines.append(
                    f"[PASS] {name:<15} within range."
                )

            else:

                lines.append(
                    f"[FAIL] {name:<15} outside [0,1]."
                )

        #######################################################################
        # Final Score Range
        #######################################################################

        if 0.0 <= candidate.scores.final_score <= 1.0:

            lines.append(
                "[PASS] Final Score     within range."
            )

        else:

            lines.append(
                "[FAIL] Final Score     outside [0,1]."
            )

        #######################################################################
        # Feature Weight Sum
        #######################################################################

        feature_sum = (

            feature_weights.skill

            + feature_weights.experience

            + feature_weights.education

            + feature_weights.certification

            + feature_weights.signal

            + feature_weights.integrity

        )

        if abs(feature_sum - 1.0) < 1e-6:

            lines.append(
                "[PASS] Feature weights sum to 1.0."
            )

        else:

            lines.append(
                f"[FAIL] Feature weights sum = {feature_sum:.4f}"
            )

        #######################################################################
        # Final Fusion Weight Sum
        #######################################################################

        fusion_sum = (

            fusion_weights.cross_encoder

            + fusion_weights.feature_score

        )

        if abs(fusion_sum - 1.0) < 1e-6:

            lines.append(
                "[PASS] Fusion weights sum to 1.0."
            )

        else:

            lines.append(
                f"[FAIL] Fusion weights sum = {fusion_sum:.4f}"
            )

        #######################################################################
        # Feature Score Consistency
        #######################################################################

        expected_feature = (

            features.skill_score
            * feature_weights.skill

            +

            features.experience_score
            * feature_weights.experience

            +

            features.education_score
            * feature_weights.education

            +

            features.certification_score
            * feature_weights.certification

            +

            features.signal_score
            * feature_weights.signal

            +

            features.integrity_score
            * feature_weights.integrity

        )

        if abs(
            expected_feature
            - features.feature_score
        ) < 1e-6:

            lines.append(
                "[PASS] Feature fusion verified."
            )

        else:

            lines.append(
                "[FAIL] Feature fusion mismatch."
            )

        #######################################################################
        # Final Score Consistency
        #######################################################################

        expected_final = (

            candidate.scores.semantic_score
            * fusion_weights.cross_encoder

            +

            features.feature_score
            * fusion_weights.feature_score

        )

        if abs(
            expected_final
            - candidate.scores.final_score
        ) < 1e-6:

            lines.append(
                "[PASS] Final score verified."
            )

        else:

            lines.append(
                "[FAIL] Final score mismatch."
            )

        lines.append("")

        ###########################################################################
    # Evidence Summary
    ###########################################################################

    def _evidence_summary(
        self,
        lines: list[str],
        candidate: Candidate,
    ) -> None:

        evidence = candidate.evidence

        lines.extend(
            [
                "EVIDENCE SUMMARY",
                "-" * 78,
                "",
            ]
        )

        #######################################################################
        # Skill
        #######################################################################

        skill = evidence.skill

        lines.extend(
            [
                "[Skill]",
                f"Matched Skills        : {skill.exact_matches}",
                f"Required Skills       : {skill.required_total}",
                f"Candidate Skills      : {skill.candidate_total}",
                f"Missing Skills        : {len(skill.missing_required)}",
                f"Additional Skills     : {len(skill.additional_skills)}",
                f"Semantic Similarity   : {skill.semantic_similarity:.4f}",
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
                f"Current Role Months   : {experience.current_role_months}",
                f"Leadership Roles      : {experience.leadership_role_count}",
                f"Leadership Months     : {experience.leadership_experience_months}",
                f"Average Tenure        : {experience.average_tenure_months:.2f}",
                f"Semantic Title        : {experience.semantic_title_similarity:.4f}",
                f"Semantic Responsibility : {experience.semantic_responsibility_similarity:.4f}",
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
                f"Minimum Degree Met    : {education.minimum_degree_met}",
                f"Relevant Degrees      : {education.relevant_degree_count}",
                f"Highest CGPA          : {education.highest_cgpa}",
                f"Average CGPA          : {education.average_cgpa}",
                f"Institution Tier      : {education.institution_tier}",
                f"Research Projects     : {education.research_project_count}",
                f"Research Publications : {education.research_publication_count}",
                f"Semantic Similarity   : {education.semantic_similarity:.4f}",
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
                f"Total Certifications  : {certification.total_certifications}",
                f"Matched               : {certification.matched_total}",
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

        total_issues = (

            integrity.missing_required_fields

            + integrity.duplicate_skills

            + integrity.duplicate_projects

            + integrity.duplicate_certifications

            + integrity.timeline_inconsistencies

            + integrity.experience_inconsistencies

        )

        lines.extend(
            [
                "[Integrity]",
                f"Missing Fields        : {integrity.missing_required_fields}",
                f"Duplicate Skills      : {integrity.duplicate_skills}",
                f"Duplicate Projects    : {integrity.duplicate_projects}",
                f"Duplicate Certificates: {integrity.duplicate_certifications}",
                f"Timeline Issues       : {integrity.timeline_inconsistencies}",
                f"Experience Issues     : {integrity.experience_inconsistencies}",
                f"Total Integrity Issues: {total_issues}",
                f"Confidence            : {integrity.confidence:.4f}",
                "",
            ]
        )

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
                "END OF ATHENA SCORE AUDIT REPORT",
                "=" * 78,
            ]
        )

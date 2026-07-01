"""
Project : Athena
Module  : Evidence Analyzer

Purpose
-------
Analyzes structured evidence collected from a candidate.

Guidelines
----------
- Deterministic.
- No ranking.
- No text generation.
- Only enriches existing evidence objects.
"""

from __future__ import annotations

from src.core.candidate import EvidenceCollection


class EvidenceAnalyzer:
    """
    Derives explainability information from structured evidence.
    """

    def analyze(
        self,
        evidence: EvidenceCollection,
    ) -> EvidenceCollection:

        self._analyze_skill(
            evidence.skill,
        )

        self._analyze_experience(
            evidence.experience,
        )

        self._analyze_education(
            evidence.education,
        )

        self._analyze_certification(
            evidence.certification,
        )

        self._analyze_signal(
            evidence.signal,
        )

        self._analyze_integrity(
            evidence.integrity,
        )

        self._analyze_cross_evidence(
            evidence,
        )

        self._finalize(
            evidence,
        )

        return evidence
    
    def _analyze_skill(
        self,
        skill,
    ) -> None:

        #######################################################################
        # Excellent Coverage
        #######################################################################

        if skill.required_total == 0:
            return

        coverage = (
            skill.exact_matches
            /
            skill.required_total
        )

        #######################################################################
        # Strengths
        #######################################################################

        if coverage >= 0.90:

            skill.strengths.append(
                "Excellent technical alignment."
            )

        elif coverage >= 0.70:

            skill.strengths.append(
                "Strong technical alignment."
            )

        elif coverage >= 0.50:

            skill.strengths.append(
                "Moderate technical alignment."
            )

        #######################################################################
        # Breadth
        #######################################################################

        if len(skill.additional_skills) >= 10:

            skill.strengths.append(
                "Broad technical skillset."
            )

        elif len(skill.additional_skills) >= 5:

            skill.strengths.append(
                "Additional transferable skills."
            )

        #######################################################################
        # Missing Skills
        #######################################################################

        if len(skill.missing_required) >= 5:

            skill.concerns.append(
                "Several required skills are missing."
            )

        elif len(skill.missing_required) > 0:

            skill.concerns.append(
                "Some required skills are missing."
            )

    def _analyze_experience(
        self,
        experience,
    ) -> None:

        #######################################################################
        # Relevant Experience
        #######################################################################

        if experience.relevant_role_count >= 5:

            experience.strengths.append(
                "Extensive relevant professional experience."
            )

        elif experience.relevant_role_count >= 2:

            experience.strengths.append(
                "Relevant professional experience."
            )

        else:

            experience.concerns.append(
                "Limited relevant professional experience."
            )

        #######################################################################
        # Leadership
        #######################################################################

        if experience.leadership_role_count >= 3:

            experience.strengths.append(
                "Strong leadership background."
            )

        elif experience.leadership_role_count > 0:

            experience.strengths.append(
                "Leadership experience identified."
            )

        #######################################################################
        # Career Stability
        #######################################################################

        if experience.average_tenure_months >= 36:

            experience.strengths.append(
                "Stable employment history."
            )

        elif (
            experience.average_tenure_months > 0
            and
            experience.average_tenure_months < 12
        ):

            experience.concerns.append(
                "Frequent job changes."
            )

        #######################################################################
        # Employment Gaps
        #######################################################################

        if experience.employment_gap_months >= 12:

            experience.concerns.append(
                "Significant employment gap detected."
            )

        elif experience.employment_gap_months >= 6:

            experience.concerns.append(
                "Moderate employment gap detected."
            )

        #######################################################################
        # Experience Depth
        #######################################################################

        if experience.total_experience_months >= 120:

            experience.strengths.append(
                "Highly experienced candidate."
            )

        elif experience.total_experience_months >= 60:

            experience.strengths.append(
                "Experienced candidate."
            )

    def _analyze_education(
        self,
        education,
    ) -> None:

        #######################################################################
        # Required Degree
        #######################################################################

        if education.minimum_degree_met:

            education.strengths.append(
                "Minimum educational qualification satisfied."
            )

        else:

            education.concerns.append(
                "Minimum educational qualification not satisfied."
            )

        #######################################################################
        # Academic Performance
        #######################################################################

        if education.highest_cgpa is not None:

            if education.highest_cgpa >= 9.0:

                education.strengths.append(
                    "Outstanding academic performance."
                )

            elif education.highest_cgpa >= 8.0:

                education.strengths.append(
                    "Strong academic performance."
                )

            elif education.highest_cgpa < 6.0:

                education.concerns.append(
                    "Below-average academic performance."
                )

        #######################################################################
        # Higher Education
        #######################################################################

        if education.highest_degree:

            degree = education.highest_degree.value.lower()

            if any(
                keyword in degree
                for keyword in (
                    "phd",
                    "doctor",
                )
            ):

                education.strengths.append(
                    "Doctoral qualification."
                )

            elif any(
                keyword in degree
                for keyword in (
                    "master",
                    "m.tech",
                    "m.e",
                    "ms",
                )
            ):

                education.strengths.append(
                    "Postgraduate qualification."
                )

        #######################################################################
        # Research
        #######################################################################

        if education.research_publication_count >= 3:

            education.strengths.append(
                "Strong research publication record."
            )

        elif education.research_publication_count > 0:

            education.strengths.append(
                "Research publications available."
            )

        if education.research_project_count >= 2:

            education.strengths.append(
                "Research project experience."
            )

        #######################################################################
        # Coursework
        #######################################################################


        if len(education.relevant_courses) >= 5:

            education.strengths.append(
                "Strong relevant academic coursework."
            )

        elif len(education.relevant_courses) >= 2:

            education.strengths.append(
                "Relevant coursework identified."
            )
        
    def _analyze_certification(
        self,
        certification,
    ) -> None:

        #######################################################################
        # Relevant Certifications
        #######################################################################

        if certification.matched_total >= 3:

            certification.strengths.append(
                "Multiple role-relevant certifications."
            )

        elif certification.matched_total > 0:

            certification.strengths.append(
                "Relevant professional certifications."
            )

        else:

            certification.concerns.append(
                "No role-relevant certifications."
            )

        #######################################################################
        # Verification
        #######################################################################

        if certification.verified_count >= 3:

            certification.strengths.append(
                "Multiple verified certifications."
            )

        elif certification.verified_count > 0:

            certification.strengths.append(
                "Verified certifications available."
            )

        #######################################################################
        # Recent Learning
        #######################################################################

        if certification.recent_certifications >= 2:

            certification.strengths.append(
                "Demonstrates continuous learning."
            )

        elif certification.recent_certifications == 0:

            certification.concerns.append(
                "No recently earned certifications."
            )

        #######################################################################
        # Relevance
        #######################################################################

        if certification.certification_relevance >= 0.80:

            certification.strengths.append(
                "Certifications closely align with the role."
            )

        elif certification.certification_relevance >= 0.50:

            certification.strengths.append(
                "Certifications moderately align with the role."
            )

        elif (
            certification.matched_total > 0
            and certification.certification_relevance < 0.30
        ):

            certification.concerns.append(
                "Limited certification relevance."
            )

    def _analyze_signal(
        self,
        signal,
    ) -> None:

        #######################################################################
        # Availability
        #######################################################################

        if signal.open_to_work:

            signal.strengths.append(
                "Actively open to new opportunities."
            )

        else:

            signal.concerns.append(
                "Not actively seeking opportunities."
            )

        if signal.notice_period_days <= 30:

            signal.strengths.append(
                "Immediately or quickly available."
            )

        elif signal.notice_period_days >= 90:

            signal.concerns.append(
                "Long notice period."
            )

        #######################################################################
        # Recruiter Engagement
        #######################################################################

        if signal.engagement_score >= 0.80:

            signal.strengths.append(
                "Strong professional engagement."
            )

        elif signal.engagement_score < 0.40:

            signal.concerns.append(
                "Limited professional engagement."
            )

        #######################################################################
        # Profile Quality
        #######################################################################

        if signal.profile_completeness >= 0.90:

            signal.strengths.append(
                "Highly complete professional profile."
            )

        elif signal.profile_completeness < 0.50:

            signal.concerns.append(
                "Profile requires additional information."
            )

        #######################################################################
        # Recruiter Visibility
        #######################################################################

        if signal.profile_views >= 50:

            signal.strengths.append(
                "High recruiter visibility."
            )

        elif signal.profile_views == 0:

            signal.concerns.append(
                "Low recruiter visibility."
            )

        #######################################################################
        # Responsiveness
        #######################################################################

        if signal.responsiveness_score >= 0.80:

            signal.strengths.append(
                "Highly responsive candidate."
            )

        elif signal.responsiveness_score < 0.40:

            signal.concerns.append(
                "Low recruiter responsiveness."
            )

        #######################################################################
        # Assessment
        #######################################################################

        if signal.assessment_score >= 0.85:

            signal.strengths.append(
                "Excellent assessment performance."
            )

        elif signal.assessment_score < 0.50:

            signal.concerns.append(
                "Assessment performance could be improved."
            )

        #######################################################################
        # Verification
        #######################################################################

        verified = sum(
            [
                signal.verified_email,
                signal.verified_phone,
                signal.linkedin_connected,
            ]
        )

        if verified == 3:

            signal.strengths.append(
                "Fully verified professional profile."
            )

        elif verified == 0:

            signal.concerns.append(
                "Profile lacks verification."
            )

    def _analyze_integrity(
        self,
        integrity,
    ) -> None:

        #######################################################################
        # Missing Fields
        #######################################################################

        if integrity.missing_required_fields == 0:

            integrity.strengths.append(
                "Complete candidate profile."
            )

        elif integrity.missing_required_fields >= 3:

            integrity.concerns.append(
                "Several required profile sections are missing."
            )

        #######################################################################
        # Duplicate Content
        #######################################################################

        duplicates = (

            integrity.duplicate_skills

            + integrity.duplicate_projects

            + integrity.duplicate_certifications

        )

        if duplicates == 0:

            integrity.strengths.append(
                "No duplicate information detected."
            )

        else:

            integrity.concerns.append(
                "Duplicate profile information detected."
            )

        #######################################################################
        # Timeline
        #######################################################################

        if integrity.timeline_inconsistencies == 0:

            integrity.strengths.append(
                "Employment timeline is consistent."
            )

        else:

            integrity.concerns.append(
                "Employment timeline requires review."
            )

        #######################################################################
        # Experience Consistency
        #######################################################################

        if integrity.experience_inconsistencies == 0:

            integrity.strengths.append(
                "Experience records are internally consistent."
            )

        else:

            integrity.concerns.append(
                "Experience records contain inconsistencies."
            )

        #######################################################################
        # Overall Trust
        #######################################################################

        if integrity.confidence >= 0.95:

            integrity.strengths.append(
                "High confidence in profile integrity."
            )

        elif integrity.confidence < 0.60:

            integrity.concerns.append(
                "Profile integrity requires manual verification."
            )

    def _analyze_cross_evidence(
        self,
        evidence: EvidenceCollection,
    ) -> None:

        skill = evidence.skill
        experience = evidence.experience
        education = evidence.education
        certification = evidence.certification
        signal = evidence.signal
        integrity = evidence.integrity

        #######################################################################
        # Technical Profile
        #######################################################################

        if (

            skill.exact_matches >= 5

            and

            experience.relevant_role_count >= 3

        ):

            experience.strengths.append(
                "Strong technical profile supported by relevant experience."
            )

        #######################################################################
        # High Potential Candidate
        #######################################################################

        if (

            education.minimum_degree_met

            and

            education.highest_cgpa is not None

            and

            education.highest_cgpa >= 8.5

            and

            experience.total_experience_months < 24

        ):

            education.strengths.append(
                "Strong academic potential with developing industry experience."
            )

        #######################################################################
        # Industry Ready
        #######################################################################

        if (

            certification.matched_total >= 2

            and

            experience.relevant_role_count >= 2

        ):

            certification.strengths.append(
                "Professional certifications reinforce practical experience."
            )

        #######################################################################
        # Hiring Readiness
        #######################################################################

        if (

            signal.open_to_work

            and

            signal.notice_period_days <= 30

            and

            signal.engagement_score >= 0.70

        ):

            signal.strengths.append(
                "High hiring readiness."
            )

        #######################################################################
        # Integrity Warning
        #######################################################################

        if (

            skill.exact_matches >= 5

            and

            integrity.confidence < 0.70

        ):

            integrity.concerns.append(
                "Strong technical profile requires additional profile verification."
            )

        #######################################################################
        # Experience vs Education
        #######################################################################

        if (

            experience.total_experience_months >= 120

            and

            not education.minimum_degree_met

        ):

            experience.strengths.append(
                "Extensive professional experience compensates for educational gap."
            )

        #######################################################################
        # Continuous Learning
        #######################################################################

        if (

            certification.recent_certifications >= 2

            and

            skill.additional_skills

        ):

            certification.strengths.append(
                "Evidence of continuous professional development."
            )

        #######################################################################
        # Recruiter Attraction
        #######################################################################

        if (

            signal.profile_views >= 50

            and

            signal.saved_by_recruiters >= 5

        ):

            signal.strengths.append(
                "Strong recruiter interest."
            )

    def _finalize(
        self,
        evidence: EvidenceCollection,
    ) -> None:

        modules = [

            evidence.skill,
            evidence.experience,
            evidence.education,
            evidence.certification,
            evidence.signal,
            evidence.integrity,

        ]

        for module in modules:

            ###################################################################
            # Remove duplicate strengths
            ###################################################################

            module.strengths = list(
                dict.fromkeys(
                    module.strengths
                )
            )

            ###################################################################
            # Remove duplicate concerns
            ###################################################################

            module.concerns = list(
                dict.fromkeys(
                    module.concerns
                )
            )

            ###################################################################
            # Optional Sorting
            ###################################################################

            module.strengths.sort()

            module.concerns.sort()
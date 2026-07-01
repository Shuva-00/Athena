"""
Project : Athena
Module  : Evidence Collector

Purpose
-------
Collects structured factual evidence from a candidate and a job description.

Guidelines
----------
- Collect facts only.
- No scoring.
- No reasoning.
- No English sentences.
"""

from __future__ import annotations
from datetime import date

from src.core.candidate.certifications import Certification
from src.core.candidate.education import Education
from src.core.enums import DegreeLevel, InstitutionTier
from src.core.candidate.experiences import Experience
from src.core import (
    Candidate,
    JobDescription,
)
from src.core.candidate import (
    EvidenceCollection,
    SkillEvidence,
    ExperienceEvidence,
    EducationEvidence,
    CertificationEvidence,
    SignalEvidence,
    IntegrityEvidence,
)
import re

class EvidenceCollector:
    """
        Collects structured evidence for recruiter explainability.
    """

    

###########################################################################
# Public API
###########################################################################


    def collect(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> EvidenceCollection:

        evidence = EvidenceCollection()

        #######################################################################
        # Skill Evidence
        #######################################################################

        evidence.skill = self._collect_skill_evidence(
            candidate,
            job,
        )

        #######################################################################
        # Remaining modules
        #######################################################################

        evidence.experience = self._collect_experience_evidence(
    candidate,
    job,
)

        evidence.education = self._collect_education_evidence(
    candidate,
    job,
)

        evidence.certification = self._collect_certification_evidence(
            candidate,
            job,
        )

        evidence.signal = self._collect_signal_evidence(
            candidate,
            job,
        )

        evidence.integrity = self._collect_integrity_evidence(
            candidate,
            job,
        )

        return evidence


    ###########################################################################
    # Skill Evidence
    ###########################################################################
    def _collect_skill_evidence(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> SkillEvidence:

        evidence = SkillEvidence()

        #######################################################################
        # Candidate Skills
        #######################################################################

        candidate_skill_confidence: dict[str, float] = {}

        for skill in candidate.skills:

            if not skill.name.strip():
                continue

            normalized = self._normalize_skill(
                skill.name
            )

            confidence = skill.confidence or 1.0

            if normalized not in candidate_skill_confidence:

                candidate_skill_confidence[
                    normalized
                ] = confidence

            else:

                candidate_skill_confidence[
                    normalized
                ] = max(
                    confidence,
                    candidate_skill_confidence[
                        normalized
                    ],
                )

        #######################################################################
        # Job Skills
        #######################################################################

        job_skills = {

            self._normalize_skill(skill)

            for skill in (

                job.required_skills
                + job.preferred_skills
                + job.technologies

            )

            if skill.strip()

        }

        #######################################################################
        # Statistics
        #######################################################################

        evidence.candidate_total = len(
            candidate_skill_confidence
        )

        evidence.required_total = len(
            job_skills
        )

        #######################################################################
        # Matching
        #######################################################################

        matched = sorted(

            candidate_skill_confidence.keys()

            &

            job_skills

        )

        missing = sorted(

            job_skills

            -

            candidate_skill_confidence.keys()

        )

        additional = sorted(

            candidate_skill_confidence.keys()

            -

            job_skills

        )

        evidence.matched_skills = matched

        evidence.missing_required = missing

        evidence.additional_skills = additional

        evidence.exact_matches = len(
            matched
        )

        #######################################################################
        # Confidence
        #######################################################################

        if job_skills:

            total = sum(

                candidate_skill_confidence[skill]

                for skill in matched

            )

            evidence.confidence = min(

                total / len(job_skills),

                1.0,

            )

        else:

            evidence.confidence = 1.0

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.exact_matches >= 8:

            evidence.strengths.append(
                "Excellent technical skill coverage."
            )

        elif evidence.exact_matches >= 5:

            evidence.strengths.append(
                "Strong technical skill coverage."
            )

        elif evidence.exact_matches >= 3:

            evidence.strengths.append(
                "Good technical skill coverage."
            )

        #######################################################################
        # Concerns
        #######################################################################

        if evidence.required_total > 0:

            ratio = (

                evidence.exact_matches

                /

                evidence.required_total

            )

            if ratio < 0.30:

                evidence.concerns.append(
                    "Limited required skill coverage."
                )

            elif ratio < 0.60:

                evidence.concerns.append(
                    "Partial required skill coverage."
                )

        return evidence
    ###########################################################################
    # Experience Evidence
    ###########################################################################
    
    def _tokenize(
        self,
        text: str,
    ) -> set[str]:

        return {

            self._normalize_skill(token)

            for token in re.findall(
                r"[A-Za-z0-9+#.\-]+",
                text.lower(),
            )

            if token.strip()

        }

    def _normalize_skill(
        self,
        text: str,
    ) -> str:

        return (
            text.lower()
            .replace("-", "")
            .replace("_", "")
            .replace(" ", "")
            .strip()
        )

    def _collect_experience_evidence(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> ExperienceEvidence:

        evidence = ExperienceEvidence()

        experiences = candidate.experiences

        if not experiences:

            evidence.concerns.append(
                "No professional experience."
            )

            return evidence

        #######################################################################
        # Phase 1
        #######################################################################

        self._compute_experience_statistics(
            experiences,
            evidence,
        )

        #######################################################################
        # Phase 2
        #######################################################################

        self._compute_relevant_experience(
            experiences,
            job,
            evidence,
        )

        #######################################################################
        # Phase 3
        #######################################################################

        self._compute_employment_gaps(
            experiences,
            evidence,
        )

        #######################################################################
        # Phase 4
        #######################################################################

        self._compute_career_progression(
            experiences,
            evidence,
        )

        #######################################################################
        # Phase 5
        #######################################################################

        self._extract_domains(
            experiences,
            evidence,
        )

        #######################################################################
        # Phase 6
        #######################################################################

        self._extract_projects(
            experiences,
            evidence,
        )

        #######################################################################
        # Finalization
        #######################################################################

        self._finalize_experience(
            evidence,
        )

        return evidence
    
    def _compute_experience_statistics(
        self,
        experiences: list[Experience],
        evidence: ExperienceEvidence,
    ) -> None:

        evidence.total_roles = len(experiences)

        durations: list[int] = []

        leadership_keywords = (
            "lead",
            "manager",
            "architect",
            "principal",
            "director",
            "head",
            "staff",
        )

        today = date.today()

        for experience in experiences:

            months = experience.duration_months

            if (
                months is None
                and experience.start_date
            ):

                end = experience.end_date or today

                months = max(
                    0,
                    (
                        (end.year - experience.start_date.year) * 12
                        +
                        (end.month - experience.start_date.month)
                    ),
                )

            months = months or 0

            durations.append(months)

            evidence.total_experience_months += months

            if experience.is_current:

                evidence.current_role_months = months

            title = experience.job_title.lower()

            if any(
                keyword in title
                for keyword in leadership_keywords
            ):

                evidence.leadership_role_count += 1

                evidence.leadership_experience_months += months

                evidence.strengths.append(
                    f"Leadership role: {experience.job_title}"
                )

        if durations:

            evidence.average_tenure_months = (
                sum(durations)
                /
                len(durations)
            )

            evidence.longest_tenure_months = max(
                durations
            )

            evidence.shortest_tenure_months = min(
                durations
            )

    def _compute_relevant_experience(
        self,
        experiences: list[Experience],
        job: JobDescription,
        evidence: ExperienceEvidence,
    ) -> None:

        #######################################################################
        # Build job keyword set
        #######################################################################

        job_keywords = {
            keyword.strip().lower()
            for keyword in (
                job.required_skills
                + job.preferred_skills
                + job.technologies
            )
            if keyword.strip()
        }

        #######################################################################
        # Check every experience
        #######################################################################

        relevant_companies = set()

        for experience in experiences:

            tokens = self._tokenize(

            " ".join(

                [
                    experience.job_title,
                    experience.company,
                    " ".join(experience.responsibilities),
                    " ".join(experience.technologies),
                    " ".join(experience.skills),
                    " ".join(experience.keywords),
                ]

            )

        )

            matched_keywords = (
                    job_keywords
                    &
                    tokens
                )

            overlap = len(
                    matched_keywords
                )

            ###################################################################
            # Relevant role
            ###################################################################

            if matched_keywords:

                evidence.relevant_role_count += 1

                evidence.relevant_roles.append(
                    experience.job_title
                )

                relevant_companies.add(
                    experience.company
                )

                evidence.relevant_experience_months += (
                    experience.duration_months or 0
                )

                ################################################################
                # Save project evidence
                ################################################################

                for responsibility in experience.responsibilities:

                    if len(responsibility) > 20:

                        evidence.relevant_projects.append(
                            responsibility
                        )

        evidence.relevant_company_count = len(
            relevant_companies
        )


    def _compute_employment_gaps(
        self,
        experiences: list[Experience],
        evidence: ExperienceEvidence,
    ) -> None:

        #######################################################################
        # Keep only dated experiences
        #######################################################################

        dated_experiences = [

            experience

            for experience in experiences

            if experience.start_date

        ]

        #######################################################################
        # Nothing to compare
        #######################################################################

        if len(dated_experiences) < 2:

            return

        #######################################################################
        # Sort chronologically
        #######################################################################

        dated_experiences.sort(
            key=lambda experience: experience.start_date
        )

        total_gap = 0

        #######################################################################
        # Compare consecutive jobs
        #######################################################################

        for previous, current in zip(
            dated_experiences,
            dated_experiences[1:],
        ):

            if previous.end_date is None:
                continue

            gap = (
                (current.start_date.year - previous.end_date.year) * 12
                +
                (current.start_date.month - previous.end_date.month)
            )

            ###################################################################
            # Ignore overlap
            ###################################################################

            if gap > 0:

                total_gap += gap

        evidence.employment_gap_months = total_gap

        #######################################################################
        # Recruiter concern
        #######################################################################

        if total_gap >= 12:

            evidence.concerns.append(
                "Significant employment gaps."
            )

        elif total_gap >= 6:

            evidence.concerns.append(
                "Moderate employment gaps."
            )


    def _compute_career_progression(
        self,
        experiences: list[Experience],
        evidence: ExperienceEvidence,
    ) -> None:

        #######################################################################
        # Title hierarchy
        #######################################################################

        title_levels = {

            "intern": 0,

            "trainee": 1,

            "associate": 2,

            "junior": 3,

            "engineer": 4,

            "developer": 4,

            "analyst": 4,

            "senior": 5,

            "lead": 6,

            "principal": 7,

            "architect": 7,

            "manager": 8,

            "head": 9,

            "director": 10,

            "vp": 11,

            "vice president": 11,

            "cto": 12,

            "chief": 12,
        }

        #######################################################################
        # Sort chronologically
        #######################################################################

        ordered = [

            experience

            for experience in experiences

            if experience.start_date

        ]

        if len(ordered) < 2:
            return

        ordered.sort(
            key=lambda experience: experience.start_date
        )

        previous_level = None

        #######################################################################
        # Compare titles
        #######################################################################

        for experience in ordered:

            title = experience.job_title.lower()

            current_level = None

            for keyword, level in title_levels.items():

                if keyword in title:

                    current_level = level

                    break

            if current_level is None:
                continue

            if previous_level is not None:

                if current_level > previous_level:

                    evidence.career_progression_steps += 1

                    evidence.title_progression_steps += (
                        current_level - previous_level
                    )

            previous_level = current_level

        #######################################################################
        # Strength
        #######################################################################

        if evidence.career_progression_steps >= 2:

            evidence.strengths.append(
                "Consistent career progression."
            )


    def _extract_domains(
        self,
        experiences: list[Experience],
        evidence: ExperienceEvidence,
    ) -> None:

        #######################################################################
        # Domain Keywords
        #######################################################################

        DOMAIN_KEYWORDS = {

            "Cloud": {
                "aws",
                "azure",
                "gcp",
                "docker",
                "kubernetes",
                "terraform",
                "cloud",
            },

            "AI/ML": {
                "machine learning",
                "deep learning",
                "tensorflow",
                "pytorch",
                "llm",
                "nlp",
                "computer vision",
                "yolo",
                "bert",
            },

            "Backend": {
                "api",
                "fastapi",
                "flask",
                "django",
                "spring",
                "node",
                "express",
                "backend",
                "microservice",
            },

            "Data Engineering": {
                "spark",
                "hadoop",
                "kafka",
                "etl",
                "warehouse",
                "airflow",
            },

            "DevOps": {
                "jenkins",
                "github actions",
                "ci/cd",
                "ansible",
                "docker",
                "kubernetes",
            },

            "Cybersecurity": {
                "security",
                "penetration",
                "vulnerability",
                "encryption",
                "authentication",
                "oauth",
                "jwt",
            },

            "Embedded": {
                "embedded",
                "firmware",
                "rtos",
                "stm32",
                "arduino",
                "microcontroller",
                "spi",
                "i2c",
                "uart",
            },

            "Networking": {
                "tcp",
                "udp",
                "routing",
                "switching",
                "network",
                "dns",
                "http",
                "socket",
            },

            "Finance": {
                "bank",
                "payment",
                "fintech",
                "trading",
                "loan",
                "insurance",
            },

            "Healthcare": {
                "ehr",
                "patient",
                "hospital",
                "medical",
                "healthcare",
            },

        }

        detected_domains = set()

        #######################################################################
        # Scan experiences
        #######################################################################

        for experience in experiences:

            text = " ".join(

                [
                    experience.job_title,
                    experience.company,
                    " ".join(experience.responsibilities),
                    " ".join(experience.technologies),
                    " ".join(experience.skills),
                    " ".join(experience.keywords),
                ]

            ).lower()

            for domain, keywords in DOMAIN_KEYWORDS.items():

                if any(

                    keyword in text

                    for keyword in keywords

                ):

                    detected_domains.add(
                        domain
                    )

        evidence.relevant_domains = sorted(
            detected_domains
        )


    def _extract_projects(
        self,
        experiences: list[Experience],
        evidence: ExperienceEvidence,
    ) -> None:

        #######################################################################
        # Prevent duplicates
        #######################################################################

        seen_projects: set[str] = set()

        #######################################################################
        # Scan experiences
        #######################################################################

        for experience in experiences:

            ###############################################################
            # Responsibilities
            ###############################################################

            for responsibility in experience.responsibilities:

                responsibility = responsibility.strip()

                if len(responsibility) < 30:
                    continue

                if responsibility in seen_projects:
                    continue

                seen_projects.add(
                    responsibility
                )

                evidence.relevant_projects.append(
                    responsibility
                )

            ###############################################################
            # Achievements
            ###############################################################

            for achievement in experience.achievements:

                achievement = achievement.strip()

                if len(achievement) < 20:
                    continue

                if achievement in seen_projects:
                    continue

                seen_projects.add(
                    achievement
                )

                evidence.relevant_projects.append(
                    achievement
                )

        #######################################################################
        # Keep only first 10
        #######################################################################

        evidence.relevant_projects = (
            evidence.relevant_projects[:10]
        )


    def _finalize_experience(
        self,
        evidence: ExperienceEvidence,
    ) -> None:

        #######################################################################
        # Confidence
        #######################################################################

        confidence = 0.0

        if evidence.total_experience_months >= 24:
            confidence += 0.25

        if evidence.relevant_experience_months >= 12:
            confidence += 0.25

        if evidence.relevant_role_count > 0:
            confidence += 0.20

        if evidence.leadership_role_count > 0:
            confidence += 0.15

        if evidence.relevant_company_count > 0:
            confidence += 0.15

        evidence.confidence = min(
            confidence,
            1.0,
        )

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.relevant_role_count >= 3:

            evidence.strengths.append(
                "Multiple relevant roles."
            )

        if evidence.relevant_company_count >= 2:

            evidence.strengths.append(
                "Relevant experience across companies."
            )

        if len(evidence.relevant_domains) >= 2:

            evidence.strengths.append(
                "Cross-domain experience."
            )

        #######################################################################
        # Concerns
        #######################################################################

        if evidence.relevant_role_count == 0:

            evidence.concerns.append(
                "No directly relevant experience."
            )

        if evidence.total_experience_months < 12:

            evidence.concerns.append(
                "Limited professional experience."
            )

        if evidence.employment_gap_months >= 12:

            evidence.concerns.append(
                "Extended employment gaps."
            )

    def _collect_education_evidence(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> EducationEvidence:

        evidence = EducationEvidence()

        education = candidate.education

        if not education:

            evidence.concerns.append(
                "No education records."
            )

            return evidence

        self._compute_degree_statistics(
            education,
            job,
            evidence,
        )

        self._compute_academic_performance(
            education,
            evidence,
        )

        self._compute_institution_evidence(
            education,
            evidence,
        )

        self._compute_coursework(
            education,
            job,
            evidence,
        )

        self._compute_research(
            education,
            evidence,
        )

        self._finalize_education(
            evidence,
        )

        return evidence
    
    def _extract_required_degree_level(
        self,
        minimum_degree: list[str],
    ) -> DegreeLevel | None:

        text = " ".join(
            minimum_degree
        ).lower()

        ###########################################################################
        # Doctorate
        ###########################################################################

        if any(
            token in text
            for token in (
                "phd",
                "doctorate",
                "doctoral",
            )
        ):
            return DegreeLevel.DOCTORATE

        ###########################################################################
        # Master's
        ###########################################################################

        if any(
            token in text
            for token in (
                "master",
                "m.tech",
                "mtech",
                "m.e",
                "me",
                "m.sc",
                "msc",
                "mba",
                "ms",
            )
        ):
            return DegreeLevel.MASTER

        ###########################################################################
        # Bachelor's
        ###########################################################################

        if any(
            token in text
            for token in (
                "bachelor",
                "b.tech",
                "btech",
                "b.e",
                "be",
                "b.sc",
                "bsc",
            )
        ):
            return DegreeLevel.BACHELOR

        ###########################################################################
        # Diploma
        ###########################################################################

        if "diploma" in text:

            return DegreeLevel.DIPLOMA

        ###########################################################################
        # Unknown
        ###########################################################################

        return None

    def _compute_degree_statistics(
        self,
        education: list[Education],
        job: JobDescription,
        evidence: EducationEvidence,
    ) -> None:

        ###########################################################################
        # Statistics
        ###########################################################################

        evidence.total_degrees = len(education)

        highest_level: DegreeLevel | None = None

        required_level = self._extract_required_degree_level(
            job.minimum_degree
        )

        ###########################################################################
        # Scan Degrees
        ###########################################################################

        for degree in education:

            if degree.degree_level is None:
                continue

            #######################################################################
            # Highest Degree
            #######################################################################

            if (
                highest_level is None
                or degree.degree_level.value > highest_level.value
            ):

                highest_level = degree.degree_level

            #######################################################################
            # Required Degree
            #######################################################################

            if (
                required_level is not None
                and degree.degree_level.value >= required_level.value
            ):

                evidence.required_degree_met = True

            #######################################################################
            # Relevant Degree
            #######################################################################

            degree_name = degree.degree or ""
            field = degree.field_of_study or ""

            education_text = (
                degree_name
                + " "
                + field
            ).lower()

            job_text = " ".join(

                job.required_skills
                + job.preferred_skills
                + job.technologies

            ).lower()

            if any(
                token in job_text
                for token in education_text.split()
            ):

                evidence.relevant_degree_count += 1

                evidence.relevant_degrees.append(
                    f"{degree_name} ({field})"
                )

        ###########################################################################
        # Final
        ###########################################################################

        evidence.highest_degree = highest_level
    def _compute_academic_performance(
        self,
        education: list[Education],
        evidence: EducationEvidence,
    ) -> None:

        #######################################################################
        # Collect valid CGPAs
        #######################################################################

        cgpas = [

            degree.cgpa

            for degree in education

            if degree.cgpa is not None

        ]

        if not cgpas:

            return

        #######################################################################
        # Statistics
        #######################################################################

        evidence.highest_cgpa = max(
            cgpas
        )

        evidence.average_cgpa = (
            sum(cgpas)
            /
            len(cgpas)
        )
    
    def _compute_institution_evidence(
        self,
        education: list[Education],
        evidence: EducationEvidence,
    ) -> None:

        #######################################################################
        # Tier ranking
        #######################################################################

        tier_rank = {

            InstitutionTier.TIER_1: 3,

            InstitutionTier.TIER_2: 2,

            InstitutionTier.TIER_3: 1,

            InstitutionTier.UNKNOWN: 0,

        }

        best_tier = InstitutionTier.UNKNOWN

        #######################################################################
        # Scan institutions
        #######################################################################

        for degree in education:

            tier = degree.tier

            if tier is None:
                continue

            if tier_rank[tier] > tier_rank[best_tier]:

                best_tier = tier

            if tier in (
                InstitutionTier.TIER_1,
                InstitutionTier.TIER_2,
            ):

                evidence.relevant_institution_count += 1

        #######################################################################
        # Final result
        #######################################################################

        evidence.institution_tier = best_tier

    def _compute_coursework(
        self,
        education: list[Education],
        job: JobDescription,
        evidence: EducationEvidence,
    ) -> None:

        #######################################################################
        # Build Job Keyword Set
        #######################################################################

        job_keywords = {

            self._normalize_skill(keyword)

            for keyword in (

                job.required_skills
                + job.preferred_skills
                + job.technologies

            )

            if keyword.strip()

        }

        #######################################################################
        # Prevent duplicates
        #######################################################################

        matched_courses = set()

        #######################################################################
        # Scan Education
        #######################################################################

        for degree in education:

            for course in degree.relevant_courses:

                normalized = course.strip().lower()

                if not normalized:
                    continue

                ###################################################################
                # Direct Match
                ###################################################################

                if any(

                    keyword in normalized
                    or normalized in keyword

                    for keyword in job_keywords

                ):

                    matched_courses.add(
                        course.strip()
                    )

        #######################################################################
        # Save
        #######################################################################

        evidence.relevant_courses = sorted(
            matched_courses
        )
    
    def _compute_research(
        self,
        education: list[Education],
        evidence: EducationEvidence,
    ) -> None:

        #######################################################################
        # Prevent duplicates
        #######################################################################

        research_projects = set()

        publications = set()

        #######################################################################
        # Scan Education
        #######################################################################

        for degree in education:

            ###############################################################
            # Research Projects
            ###############################################################

            for project in degree.research_projects:

                project = project.strip()

                if project:

                    research_projects.add(
                        project
                    )

            ###############################################################
            # Publications
            ###############################################################

            for publication in degree.publications:

                publication = publication.strip()

                if publication:

                    publications.add(
                        publication
                    )

        #######################################################################
        # Save
        #######################################################################

        evidence.research_project_count = len(
            research_projects
        )

        evidence.research_publication_count = len(
            publications
        )
    
    def _finalize_education(
        self,
        evidence: EducationEvidence,
    ) -> None:

        #######################################################################
        # Confidence
        #######################################################################

        confidence = 0.0

        if evidence.required_degree_met:
            confidence += 0.35

        if evidence.relevant_degree_count > 0:
            confidence += 0.20

        if evidence.relevant_institution_count > 0:
            confidence += 0.15

        if evidence.highest_cgpa is not None:

            if evidence.highest_cgpa >= 8.5:
                confidence += 0.15

            elif evidence.highest_cgpa >= 7.5:
                confidence += 0.10

        if evidence.research_project_count > 0:
            confidence += 0.10

        if evidence.research_publication_count > 0:
            confidence += 0.05

        evidence.confidence = min(
            confidence,
            1.0,
        )

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.required_degree_met:

            evidence.strengths.append(
                "Required degree satisfied."
            )

        if evidence.relevant_degree_count > 0:

            evidence.strengths.append(
                "Relevant academic background."
            )

        if evidence.relevant_institution_count > 0:

            evidence.strengths.append(
                "Recognized institution."
            )

        if (
            evidence.highest_cgpa is not None
            and evidence.highest_cgpa >= 8.5
        ):

            evidence.strengths.append(
                "Strong academic performance."
            )

        if evidence.research_publication_count > 0:

            evidence.strengths.append(
                "Research publications available."
            )

        #######################################################################
        # Concerns
        #######################################################################

        if not evidence.required_degree_met:

            evidence.concerns.append(
                "Required degree not satisfied."
            )

        if evidence.relevant_degree_count == 0:

            evidence.concerns.append(
                "Academic background weakly aligned."
            )

        if (
            evidence.highest_cgpa is not None
            and evidence.highest_cgpa < 6.5
        ):

            evidence.concerns.append(
                "Low academic performance."
            )

    def _collect_certification_evidence(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> CertificationEvidence:

        evidence = CertificationEvidence()

        certifications = candidate.certifications

        if not certifications:

            evidence.concerns.append(
                "No professional certifications."
            )

            return evidence

        self._compute_certification_statistics(
            certifications,
            evidence,
        )

        self._compute_relevant_certifications(
            certifications,
            job,
            evidence,
        )

        self._finalize_certification(
            evidence,
        )

        return evidence
    
    def _compute_certification_statistics(
        self,
        certifications: list[Certification],
        evidence: CertificationEvidence,
    ) -> None:

        evidence.total_certifications = len(
            certifications
        )

        today = date.today()

        for certification in certifications:

            ###############################################################
            # Verified
            ###############################################################

            if certification.verified:

                evidence.verified_count += 1

            ###############################################################
            # Recent
            ###############################################################

            if certification.issue_date:

                years = (
                    today.year
                    -
                    certification.issue_date.year
                )

                if years <= 3:

                    evidence.recent_certifications += 1

    def _compute_relevant_certifications(
        self,
        certifications: list[Certification],
        job: JobDescription,
        evidence: CertificationEvidence,
    ) -> None:

        #######################################################################
        # Build Job Vocabulary
        #######################################################################

        job_keywords = {

            self._normalize_skill(keyword)

            for keyword in (

                job.required_skills
                + job.preferred_skills
                + job.technologies

            )

            if keyword.strip()

        }

        #######################################################################
        # Match Certifications
        #######################################################################

        matched = set()

        missing = set(job_keywords)

        total_overlap = 0

        for certification in certifications:

            tokens = self._tokenize(

                " ".join(

                    [

                        certification.name,

                        certification.issuer or "",

                        certification.level or "",

                        " ".join(certification.skills),

                        " ".join(certification.keywords),

                    ]

                )

            )

            overlap = tokens & job_keywords

            if overlap:

                matched.add(
                    certification.name
                )

                total_overlap += len(overlap)

                missing -= overlap

        #######################################################################
        # Save
        #######################################################################

        evidence.matched_certifications = sorted(
            matched
        )

        evidence.missing_certifications = sorted(
            missing
        )

        evidence.matched_total = len(
            matched
        )

        if job_keywords:

            evidence.certification_relevance = min(
                1.0,
                total_overlap / len(job_keywords),
            )
    def _finalize_certification(
        self,
        evidence: CertificationEvidence,
    ) -> None:

        #######################################################################
        # Confidence
        #######################################################################

        confidence = 0.0

        if evidence.matched_total > 0:
            confidence += 0.40

        if evidence.verified_count > 0:
            confidence += 0.20

        if evidence.recent_certifications > 0:
            confidence += 0.20

        confidence += (
            evidence.certification_relevance
            * 0.20
        )

        evidence.confidence = min(
            confidence,
            1.0,
        )

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.matched_total > 0:

            evidence.strengths.append(
                "Relevant certifications."
            )

        if evidence.verified_count > 0:

            evidence.strengths.append(
                "Verified certifications."
            )

        if evidence.recent_certifications > 0:

            evidence.strengths.append(
                "Recently earned certifications."
            )

        #######################################################################
        # Concerns
        #######################################################################

        if evidence.total_certifications == 0:

            evidence.concerns.append(
                "No certifications."
            )

        elif evidence.matched_total == 0:

            evidence.concerns.append(
                "No certifications relevant to the role."
            )
    def _collect_signal_evidence(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> SignalEvidence:

        evidence = SignalEvidence()

        signals = candidate.signals

        self._compute_responsiveness(
            signals,
            evidence,
        )

        self._compute_engagement(
            signals,
            evidence,
        )

        self._compute_assessment(
            signals,
            evidence,
        )

        self._compute_availability(
            signals,
            evidence,
        )

        self._compute_recruiter_interest(
            signals,
            evidence,
        )

        self._compute_verification(
            signals,
            evidence,
        )

        self._finalize_signal(
            evidence,
        )

        return evidence

    def _compute_responsiveness(
        self,
        signals,
        evidence,
    ) -> None:

        #######################################################################
        # Response Rate
        #######################################################################

        evidence.responsiveness_score = (
            signals.recruiter_response_rate
        )

        #######################################################################
        # Availability
        #######################################################################

        evidence.open_to_work = (
            signals.open_to_work_flag
        )

        evidence.notice_period_days = (
            signals.notice_period_days
        )

        #######################################################################
        # Response Quality
        #######################################################################

        if (
            signals.avg_response_time_hours
            <= 24
        ):

            evidence.strengths.append(
                "Responds quickly."
            )

        elif (
            signals.avg_response_time_hours
            >= 72
        ):

            evidence.concerns.append(
                "Slow recruiter response."
            )  
    
    def _compute_engagement(
        self,
        signals,
        evidence,
    ) -> None:

        #######################################################################
        # Profile
        #######################################################################

        evidence.profile_completeness = (
            signals.profile_completeness_score
            / 100.0
        )

        evidence.github_activity = (
            max(
                0.0,
                signals.github_activity_score,
            )
            / 100.0
        )

        #######################################################################
        # Activity
        #######################################################################

        evidence.applications_last_30d = (
            signals.applications_submitted_30d
        )

        evidence.connections = (
            signals.connection_count
        )

        evidence.endorsements = (
            signals.endorsements_received
        )

        #######################################################################
        # Engagement Score
        #######################################################################

        engagement = 0.0

        engagement += (
            evidence.profile_completeness * 0.40
        )

        engagement += (
            evidence.github_activity * 0.30
        )

        engagement += min(
            1.0,
            evidence.connections / 500,
        ) * 0.15

        engagement += min(
            1.0,
            evidence.endorsements / 100,
        ) * 0.15

        evidence.engagement_score = min(
            engagement,
            1.0,
        )

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.profile_completeness >= 0.90:

            evidence.strengths.append(
                "Highly complete profile."
            )

        if evidence.github_activity >= 0.70:

            evidence.strengths.append(
                "Strong GitHub activity."
            )

        #######################################################################
        # Concerns
        #######################################################################

        if evidence.profile_completeness < 0.50:

            evidence.concerns.append(
                "Incomplete profile."
            )

        if (
            signals.github_activity_score >= 0
            and evidence.github_activity < 0.20
        ):

            evidence.concerns.append(
                "Low GitHub activity."
            )

        if signals.github_activity_score >= 0:
            evidence.github_activity = (
                signals.github_activity_score / 100.0
            )
        else:
            evidence.github_activity = 0.0

    def _compute_assessment(
        self,
        signals,
        evidence,
    ) -> None:

        #######################################################################
        # Assessment Scores
        #######################################################################

        scores = list(
            signals.skill_assessment_scores.values()
        )

        if not scores:

            evidence.assessment_score = 0.0
            return

        #######################################################################
        # Normalize
        #######################################################################

        normalized = [

            max(
                0.0,
                min(
                    score,
                    100.0,
                ),
            ) / 100.0

            for score in scores

        ]

        evidence.assessment_score = (
            sum(normalized)
            /
            len(normalized)
        )

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.assessment_score >= 0.85:

            evidence.strengths.append(
                "Excellent assessment performance."
            )

        elif evidence.assessment_score >= 0.70:

            evidence.strengths.append(
                "Strong assessment performance."
            )

        #######################################################################
        # Concerns
        #######################################################################

        if evidence.assessment_score < 0.40:

            evidence.concerns.append(
                "Low assessment performance."
            )

    def _compute_availability(
        self,
        signals,
        evidence,
    ) -> None:

        #######################################################################
        # Availability
        #######################################################################

        evidence.open_to_work = (
            signals.open_to_work_flag
        )

        evidence.notice_period_days = (
            signals.notice_period_days
        )

        #######################################################################
        # Salary
        #######################################################################

        evidence.salary_expectation_min = (
            signals.expected_salary_range_inr_lpa.minimum
        )

        evidence.salary_expectation_max = (
            signals.expected_salary_range_inr_lpa.maximum
        )

        #######################################################################
        # Work Preference
        #######################################################################

        evidence.preferred_work_mode = (
            signals.preferred_work_mode.value
        )

        evidence.willing_to_relocate = (
            signals.willing_to_relocate
        )

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.open_to_work:

            evidence.strengths.append(
                "Open to work."
            )

        if evidence.notice_period_days <= 30:

            evidence.strengths.append(
                "Short notice period."
            )

        if evidence.willing_to_relocate:

            evidence.strengths.append(
                "Open to relocation."
            )

        #######################################################################
        # Concerns
        #######################################################################

        if not evidence.open_to_work:

            evidence.concerns.append(
                "Not actively seeking opportunities."
            )

        if evidence.notice_period_days > 90:

            evidence.concerns.append(
                "Long notice period."
            )

    def _compute_recruiter_interest(
        self,
        signals,
        evidence,
    ) -> None:

        #######################################################################
        # Recruiter Metrics
        #######################################################################

        evidence.profile_views = (
            signals.profile_views_received_30d
        )

        evidence.search_appearances = (
            signals.search_appearance_30d
        )

        evidence.saved_by_recruiters = (
            signals.saved_by_recruiters_30d
        )

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.profile_views >= 25:

            evidence.strengths.append(
                "Frequently viewed by recruiters."
            )

        if evidence.search_appearances >= 20:

            evidence.strengths.append(
                "High recruiter search visibility."
            )

        if evidence.saved_by_recruiters >= 5:

            evidence.strengths.append(
                "Frequently shortlisted by recruiters."
            )

        #######################################################################
        # Concerns
        #######################################################################

        if (
            evidence.profile_views == 0
            and
            evidence.search_appearances == 0
        ):

            evidence.concerns.append(
                "Low recruiter visibility."
            )

    def _compute_verification(
        self,
        signals,
        evidence,
    ) -> None:

        #######################################################################
        # Verification
        #######################################################################

        evidence.verified_email = (
            signals.verified_email
        )

        evidence.verified_phone = (
            signals.verified_phone
        )

        evidence.linkedin_connected = (
            signals.linkedin_connected
        )

        #######################################################################
        # Strengths
        #######################################################################

        if evidence.verified_email:

            evidence.strengths.append(
                "Verified email."
            )

        if evidence.verified_phone:

            evidence.strengths.append(
                "Verified phone."
            )

        if evidence.linkedin_connected:

            evidence.strengths.append(
                "LinkedIn profile connected."
            )

        #######################################################################
        # Concerns
        #######################################################################

        if not evidence.verified_email:

            evidence.concerns.append(
                "Email not verified."
            )

        if not evidence.verified_phone:

            evidence.concerns.append(
                "Phone not verified."
            )

        if not evidence.linkedin_connected:

            evidence.concerns.append(
                "LinkedIn profile not connected."
            )
    def _finalize_signal(
        self,
        evidence,
    ) -> None:

        #######################################################################
        # Available Signals
        #######################################################################

        available = 0
        total = 6

        if evidence.responsiveness_score > 0:
            available += 1

        if evidence.engagement_score > 0:
            available += 1

        if evidence.assessment_score > 0:
            available += 1

        if evidence.profile_completeness > 0:
            available += 1

        if evidence.github_activity > 0:
            available += 1

        if (
            evidence.verified_email
            or evidence.verified_phone
            or evidence.linkedin_connected
        ):
            available += 1

        #######################################################################
        # Confidence
        #######################################################################

        evidence.confidence = (
            available / total
        )

    def _collect_integrity_evidence(
        self,
        candidate: Candidate,
        job: JobDescription,
    ) -> IntegrityEvidence:

        evidence = IntegrityEvidence()

        self._check_missing_fields(
            candidate,
            evidence,
        )

        self._check_duplicates(
            candidate,
            evidence,
        )

        self._check_experience(
            candidate,
            evidence,
        )

        self._check_timeline(
            candidate,
            evidence,
        )

        self._finalize_integrity(
            evidence,
        )

        return evidence
    
    def _check_missing_fields(
        self,
        candidate,
        evidence,
    ) -> None:

        missing = 0

        if not candidate.profile.headline:
            missing += 1

        if not candidate.education:
            missing += 1

        if not candidate.skills:
            missing += 1

        if not candidate.experiences:
            missing += 1

        evidence.missing_required_fields = missing

        if missing == 0:

            evidence.strengths.append(
                "Complete profile."
            )

        else:

            evidence.concerns.append(
                f"{missing} required sections missing."
            )
    
    def _check_duplicates(
        self,
        candidate,
        evidence,
    ) -> None:

        ###############################################################
        # Skills
        ###############################################################

        skills = [

            skill.name.lower().strip()

            for skill in candidate.skills

        ]

        evidence.duplicate_skills = (
            len(skills)
            -
            len(set(skills))
        )

        ###############################################################
        # Certifications
        ###############################################################

        certifications = [

            cert.name.lower().strip()

            for cert in candidate.certifications

        ]

        evidence.duplicate_certifications = (
            len(certifications)
            -
            len(set(certifications))
        )

        ###############################################################
        # Projects
        ###############################################################

        projects = [

            project.title.lower().strip()

            for project in candidate.projects

        ]

        evidence.duplicate_projects = (
            len(projects)
            -
            len(set(projects))
        )

    def _check_experience(
        self,
        candidate,
        evidence,
    ) -> None:

        inconsistencies = 0

        experiences = candidate.experiences

        for experience in experiences:

            ###############################################################
            # Missing Job Title
            ###############################################################

            if not experience.job_title.strip():

                inconsistencies += 1

            ###############################################################
            # Missing Company
            ###############################################################

            if not experience.company.strip():

                inconsistencies += 1

            ###############################################################
            # Invalid Duration
            ###############################################################

            if (
                experience.duration_months is not None
                and experience.duration_months < 0
            ):

                inconsistencies += 1

        evidence.experience_inconsistencies = inconsistencies

        if inconsistencies == 0:

            evidence.strengths.append(
                "Experience records are consistent."
            )

        else:

            evidence.concerns.append(
                f"{inconsistencies} experience inconsistencies."
            )

    def _check_timeline(
        self,
        candidate,
        evidence,
    ) -> None:

        inconsistencies = 0

        experiences = sorted(
            candidate.experiences,
            key=lambda x: x.start_date or date.min,
        )

        for i in range(1, len(experiences)):

            previous = experiences[i - 1]
            current = experiences[i]

            if (
                previous.end_date
                and current.start_date
                and current.start_date < previous.end_date
            ):

                inconsistencies += 1

        evidence.timeline_inconsistencies = inconsistencies

        if inconsistencies == 0:

            evidence.strengths.append(
                "Timeline is consistent."
            )

        else:

            evidence.concerns.append(
                f"{inconsistencies} overlapping employments."
            )

    def _finalize_integrity(
        self,
        evidence,
    ) -> None:

        #######################################################################
        # Total Issues
        #######################################################################

        total_issues = (

            evidence.missing_required_fields

            + evidence.duplicate_skills

            + evidence.duplicate_projects

            + evidence.duplicate_certifications

            + evidence.timeline_inconsistencies

            + evidence.experience_inconsistencies

        )

        #######################################################################
        # Confidence
        #######################################################################

        evidence.confidence = max(
            0.0,
            1.0 - (total_issues * 0.10),
        )

        #######################################################################
        # Final Strength
        #######################################################################

        if total_issues == 0:

            evidence.strengths.append(
                "Resume integrity verified."
            )

        #######################################################################
        # Final Concern
        #######################################################################

        if total_issues >= 5:

            evidence.concerns.append(
                "Multiple profile integrity issues detected."
            )
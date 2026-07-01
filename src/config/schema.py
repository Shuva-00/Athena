"""
Project : Athena
Module  : Configuration Schema

Purpose
-------
Defines the strongly typed configuration models used by Athena.

Guidelines
----------
- Pure configuration models.
- No business logic.
- No file loading.
- Immutable after creation.
"""

from __future__ import annotations

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


###############################################################################
# Project
###############################################################################


class ProjectConfig(BaseModel):
    """
    Project information.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    name: str

    version: str

    description: str


###############################################################################
# Environment
###############################################################################


class EnvironmentConfig(BaseModel):
    """
    Runtime environment configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    mode: str

    random_seed: int = Field(
        ge=0,
    )


###############################################################################
# Pipeline
###############################################################################


class PipelineConfig(BaseModel):
    """
    Pipeline execution switches.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    enable_preprocessing: bool

    enable_retrieval: bool

    enable_ranking: bool

    enable_reasoning: bool

    enable_submission: bool

    enable_evaluation: bool

    enable_benchmark: bool
    build_bm25_index: bool
    build_dense_index: bool

    enable_hybrid_retrieval: bool

###############################################################################
# Evaluation
###############################################################################


class EvaluationConfig(BaseModel):
    """
    Evaluation configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    default_k: int = Field(
        ge=1,
    )
###############################################################################
# Models
###############################################################################


class EmbeddingModelConfig(BaseModel):
    """
    Embedding model configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    model_name: str

    normalize_embeddings: bool


class CrossEncoderModelConfig(BaseModel):
    """
    Cross-encoder configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    model_name: str

    rerank_input_size: int = Field(
        ge=1,
    )

    
    


class FutureModelConfig(BaseModel):
    """
    Reserved future models.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    reranker: str | None = None

    llm: str | None = None

    classifier: str | None = None


class ModelConfig(BaseModel):
    """
    AI model configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    embedding: EmbeddingModelConfig

    cross_encoder: CrossEncoderModelConfig

    future: FutureModelConfig
###############################################################################
# Retrieval
###############################################################################


class BM25Config(BaseModel):
    """
    BM25 retrieval configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    top_k: int = Field(
        ge=1,
    )
    lowercase: bool

    tokenizer: str

class DenseRetrievalConfig(BaseModel):
    """
    Dense retrieval configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    top_k: int = Field(
        ge=1,
    )

    normalize_embeddings: bool

    faiss_metric: str


class FusionRetrievalConfig(BaseModel):
    """
    Hybrid retrieval fusion configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    final_top_k: int = Field(
        ge=1,
    )

    rrf_k: int = Field(
        ge=1,
    )


class RetrievalConfig(BaseModel):
    """
    Hybrid retrieval configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    bm25: BM25Config

    dense: DenseRetrievalConfig

    fusion: FusionRetrievalConfig

###############################################################################
# Ranking
###############################################################################


class CrossEncoderRankingConfig(BaseModel):
    """
    Cross-encoder inference configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    batch_size: int = Field(
        ge=1,
    )


class FinalRankingConfig(BaseModel):
    """
    Final ranking configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    final_top_k: int = Field(
        ge=1,
    )

    assign_ranks: bool

    normalize_scores: bool


class RankingFusionConfig(BaseModel):
    """
    Score fusion configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    enable_score_fusion: bool


class RankingOutputConfig(BaseModel):
    """
    Ranking output configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    store_semantic_score: bool

    store_feature_score: bool

    store_final_score: bool

    store_rank: bool


class RankingConfig(BaseModel):
    """
    Complete ranking configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    cross_encoder: CrossEncoderRankingConfig

    ranking: FinalRankingConfig

    fusion: RankingFusionConfig

    output: RankingOutputConfig

###############################################################################
# Weights
###############################################################################


class FusionWeightConfig(BaseModel):
    """
    Fusion score weights.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    cross_encoder: float = Field(
        ge=0.0,
        le=1.0,
    )

    feature_score: float = Field(
        ge=0.0,
        le=1.0,
    )


###############################################################################
# Skill Feature Weights
###############################################################################


class SkillWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    matching: float = Field(ge=0.0, le=1.0)

    confidence: float = Field(ge=0.0, le=1.0)

    duration: float = Field(ge=0.0, le=1.0)

    endorsement: float = Field(ge=0.0, le=1.0)

    semantic: float = Field(ge=0.0, le=1.0)


###############################################################################
# Experience Feature Weights
###############################################################################


class ExperienceWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    relevance: float = Field(ge=0.0, le=1.0)

    stability: float = Field(ge=0.0, le=1.0)

    leadership: float = Field(ge=0.0, le=1.0)

    semantic: float = Field(ge=0.0, le=1.0)


###############################################################################
# Education Feature Weights
###############################################################################


class EducationWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    degree: float = Field(
        ge=0.0,
        le=1.0,
    )

    cgpa: float = Field(
        ge=0.0,
        le=1.0,
    )

    institution: float = Field(
        ge=0.0,
        le=1.0,
    )

    research: float = Field(
        ge=0.0,
        le=1.0,
    )

    semantic: float = Field(
        ge=0.0,
        le=1.0,
    )

    confidence: float = Field(
        ge=0.0,
        le=1.0,
    )


###############################################################################
# Certification Feature Weights
###############################################################################


class CertificationWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    relevance: float = Field(ge=0.0, le=1.0)

    recency: float = Field(ge=0.0, le=1.0)


###############################################################################
# Signal Feature Weights
###############################################################################


class SignalWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    responsiveness: float = Field(ge=0.0, le=1.0)

    engagement: float = Field(ge=0.0, le=1.0)

    assessment: float = Field(ge=0.0, le=1.0)


###############################################################################
# Integrity Feature Weights
###############################################################################


class IntegrityWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    consistency: float = Field(ge=0.0, le=1.0)

    confidence: float = Field(ge=0.0, le=1.0)


###############################################################################
# Feature Scoring
###############################################################################


class FeatureScoringWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    skill: SkillWeightConfig

    experience: ExperienceWeightConfig

    education: EducationWeightConfig

    certification: CertificationWeightConfig

    signal: SignalWeightConfig

    integrity: IntegrityWeightConfig

class NormalizationWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    duration_cap_months: int = Field(
        ge=1,
    )

    endorsement_cap: int = Field(
        ge=1,
    )


###############################################################################
# Final Fusion
###############################################################################


class FinalFusionWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    cross_encoder: float = Field(ge=0.0, le=1.0)

    feature_score: float = Field(ge=0.0, le=1.0)


###############################################################################
# Weight Config
###############################################################################


class WeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    fusion: FinalFusionWeightConfig
    feature_fusion: FeatureFusionWeightConfig
    feature_scoring: FeatureScoringWeightConfig
    normalization: NormalizationWeightConfig
###############################################################################
# Features
###############################################################################


class ExtractionConfig(BaseModel):
    """
    Feature extraction switches.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    extract_keywords: bool

    extract_technologies: bool

    extract_achievements: bool


class ExperienceFeatureConfig(BaseModel):
    """
    Experience feature configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    count_total_months: bool


class ProjectFeatureConfig(BaseModel):
    """
    Project feature configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    count_projects: bool


class TechnologyFeatureConfig(BaseModel):
    """
    Technology feature configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    calculate_diversity: bool


class CertificationFeatureConfig(BaseModel):
    """
    Certification feature configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    count_certifications: bool


class ThresholdConfig(BaseModel):
    """
    Feature reasoning thresholds.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    minimum_strong_skill_match: int = Field(
        ge=0,
    )

    minimum_strong_technology_match: int = Field(
        ge=0,
    )


class FeatureConfig(BaseModel):
    """
    Feature engineering configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    extraction: ExtractionConfig

    experience: ExperienceFeatureConfig

    projects: ProjectFeatureConfig

    technologies: TechnologyFeatureConfig

    certifications: CertificationFeatureConfig

    thresholds: ThresholdConfig

###############################################################################
# Paths
###############################################################################


class RootPathConfig(BaseModel):
    """
    Root project directories.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    data: str

    outputs: str

    models: str

    configs: str


class InputPathConfig(BaseModel):
    """
    Input dataset paths.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    candidates: str

    job_description: str


class OutputPathConfig(BaseModel):
    """
    Submission output paths.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    submission_directory: str

    submission_csv: str

    submission_zip: str


class ReportPathConfig(BaseModel):
    """
    Report paths.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    benchmark: str

    evaluation: str


class LogPathConfig(BaseModel):
    """
    Log paths.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    directory: str

    file: str


class PretrainedModelPathConfig(BaseModel):
    """
    Local pretrained model paths.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    embedding: str

    cross_encoder: str


class PathConfig(BaseModel):
    """
    Complete project path configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    root: RootPathConfig

    input: InputPathConfig

    output: OutputPathConfig

    reports: ReportPathConfig

    logs: LogPathConfig

    pretrained: PretrainedModelPathConfig


###############################################################################
# Logging
###############################################################################


class LoggerConfig(BaseModel):
    """
    Logger configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    name: str

    level: str


class FormatConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    standard: str

    date: str






class RotationConfig(BaseModel):
    """
    Log rotation configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )
    enabled: bool
    max_bytes: int

    backup_count: int

class ConsoleConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    enabled: bool


class FileConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    enabled: bool

    path: str
    
class LoggingConfig(BaseModel):
    """
    Complete logging configuration.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    logger: LoggerConfig

    format: FormatConfig

    console: ConsoleConfig

    file: FileConfig

    rotation: RotationConfig

class ConsoleConfig(BaseModel):

    enabled: bool

class FileConfig(BaseModel):

    enabled: bool

    path: str

###############################################################################
# Root Settings
###############################################################################


class AthenaSettings(BaseModel):
    """
    Root Athena configuration object.
    """

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    project: ProjectConfig

    environment: EnvironmentConfig

    pipeline: PipelineConfig

    evaluation: EvaluationConfig

    models: ModelConfig

    retrieval: RetrievalConfig

    ranking: RankingConfig

    weights: WeightConfig

    features: FeatureConfig

    paths: PathConfig

    logging: LoggingConfig

class FeatureFusionWeightConfig(BaseModel):

    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
    )

    skill: float = Field(ge=0.0, le=1.0)

    experience: float = Field(ge=0.0, le=1.0)

    education: float = Field(ge=0.0, le=1.0)

    certification: float = Field(ge=0.0, le=1.0)

    signal: float = Field(ge=0.0, le=1.0)

    integrity: float = Field(ge=0.0, le=1.0)
###############################################################################
# END OF FILE
###############################################################################
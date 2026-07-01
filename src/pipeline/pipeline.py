"""
Project : Athena
Module  : Pipeline

Purpose
-------
Coordinates the complete Athena candidate ranking pipeline.

Pipeline
--------
Load
→ Clean
→ Parse
→ Normalize
→ Extract
→ Feature Build
→ Build Documents
→ Build Index
→ Retrieve
→ Rank
→ Reason
→ Evaluate
→ Submit
"""

from __future__ import annotations

from pathlib import Path
from typing import Any
from src.core.job_description_parser import JobDescriptionParser
from src.core import (
    Candidate,
    CandidateParser,
    JobDescription,
)

from src.preprocessing import (
    Loader,
    Cleaner,
    Normalizer,
    Extractor,
    FeatureBuilder,
)

from src.retrieval import (
    DocumentBuilder,
    IndexBuilder,
    BM25Retriever,
    DenseRetriever,
    Fusion,
)

from src.ranking import (
    CrossEncoderRanker,
    FeatureScorer,
    FinalScoreFusion,
    RankingEngine,
)

from src.reasoning import (
    EvidenceCollector,
    EvidenceAnalyzer,
    ReasonGenerator,
)

from src.evaluation import (
    Benchmark,
)

from src.submission import (
    SubmissionGenerator,
)


class Pipeline:
    """
    Executes the complete Athena pipeline.
    """

    ###########################################################################
    # Initialization
    ###########################################################################

    def __init__(
        self,
        candidate_file: str | Path,
        job_file: str | Path,
        output_directory: str | Path,
    ) -> None:

        #######################################################################
        # Paths
        #######################################################################

        self.candidate_file = Path(candidate_file)
        self.job_file = Path(job_file)
        self.output_directory = Path(output_directory)
        self.job_parser = JobDescriptionParser()
        self.output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        #######################################################################
        # Data
        #######################################################################

        self.job: JobDescription | None = None

        self.raw_candidates: list[dict[str, Any]] = []

        self.candidates: list[Candidate] = []
        self.benchmark_result = None
        self.documents: list[dict[str, Any]] = []

        #######################################################################
        # Retrieval Objects
        #######################################################################

        self.bm25 = None
        self.faiss_index = None
        self.candidate_ids: list[str] = []

        #######################################################################
        # Components
        #######################################################################

        # Loading

        self.loader = Loader()
        self.cleaner = Cleaner()

        # Parsing

        self.parser = CandidateParser()

        # Preprocessing

        self.normalizer = Normalizer()
        self.extractor = Extractor()
        self.feature_builder = FeatureBuilder()

        # Retrieval

        self.document_builder = DocumentBuilder()
        self.index_builder = IndexBuilder()

        self.bm25_retriever = BM25Retriever()
        self.dense_retriever = DenseRetriever()
        self.fusion = Fusion()

        # Ranking

        self.cross_encoder = CrossEncoderRanker()

        self.feature_scorer = FeatureScorer()


        self.final_score_fusion = FinalScoreFusion()

        self.ranking_engine = RankingEngine()

        # Reasoning

        self.evidence_collector = EvidenceCollector()

        self.evidence_analyzer = EvidenceAnalyzer()

        self.reason_generator = ReasonGenerator()

        # Evaluation

        self.benchmark = Benchmark()

        # Submission

        self.submission_generator = SubmissionGenerator()

            ###########################################################################
    # Loading
    ###########################################################################

    def _load(self) -> None:
        """
        Load datasets from disk.
        """

        self.raw_candidates = self.loader.load_candidates(
            self.candidate_file
        )

        job_data = self.loader.load_job_description(
        self.job_file
)

        if "raw_text" in job_data:

            self.job = self.job_parser.parse(
                job_data["raw_text"]
            )

        else:

            self.job = JobDescription.model_validate(
                job_data
            )

    ###########################################################################
    # Preprocessing
    ###########################################################################

    def _preprocess(self) -> None:
        """
        Clean, parse, normalize, and enrich candidates.
        """

        #######################################################################
        # Clean raw records
        #######################################################################

        cleaned_records = self.cleaner.clean(
            self.raw_candidates
        )

        #######################################################################
        # Parse Candidates
        #######################################################################

        candidates: list[Candidate] = []

        for record in cleaned_records:

            candidate = self.parser.parse(
                record
            )

            candidates.append(
                candidate
            )

        #######################################################################
        # Normalize
        #######################################################################

        for candidate in candidates:

            self.normalizer.normalize(
                candidate
            )

        #######################################################################
        # Keyword / Technology Extraction
        #######################################################################

        for candidate in candidates:

            self.extractor.extract(
                candidate
            )

        #######################################################################
        # Feature Engineering
        #######################################################################

        for candidate in candidates:

            self.feature_builder.build(
                candidate
            )

        #######################################################################
        # Store
        #######################################################################

        self.candidates = candidates
        ###########################################################################
    # Retrieval
    ###########################################################################

    def _retrieve(self) -> None:
        """
        Retrieve the most relevant candidates.
        """

        if self.job is None:
            raise RuntimeError(
                "Job description has not been loaded."
            )

        #######################################################################
        # Build Retrieval Documents
        #######################################################################

        self.documents = [
            self.document_builder.build(candidate)
            for candidate in self.candidates
        ]

        #######################################################################
        # Build Indexes
        #######################################################################

        (
            bm25_index,
            faiss_index,
            candidate_ids,
        ) = self.index_builder.build(
            self.documents
        )

        #######################################################################
        # Build Query
        #######################################################################

        query = self.job.to_text()

        #######################################################################
        # Sparse Retrieval
        #######################################################################

        bm25_results = self.bm25_retriever.retrieve(
            query=query,
            bm25=bm25_index,
            candidate_ids=candidate_ids,
        )

        #######################################################################
        # Dense Retrieval
        #######################################################################

        dense_results = self.dense_retriever.retrieve(
            query=query,
            faiss_index=faiss_index,
            candidate_ids=candidate_ids,
        )

        #######################################################################
        # Reciprocal Rank Fusion
        #######################################################################

        fused_results = self.fusion.fuse(
            bm25_results,
            dense_results,
        )

        #######################################################################
        # Candidate Lookup
        #######################################################################

        candidate_lookup = {
            candidate.candidate_id: candidate
            for candidate in self.candidates
        }

        #######################################################################
        # Replace Candidate Pool
        #######################################################################

        retrieved_candidates: list[Candidate] = []

        for candidate_id, retrieval_score in fused_results:

            candidate = candidate_lookup[candidate_id]

            candidate.scores.retrieval_score = retrieval_score

            retrieved_candidates.append(candidate)

        self.candidates = retrieved_candidates

        ###########################################################################
    # Ranking
    ###########################################################################

    def _rank(
        self,
    ) -> None:
        """
        Rank retrieved candidates.
        """

        if self.job is None:
            raise RuntimeError(
                "Job description has not been loaded."
            )

    #######################################################################
    # Build Job Text
    #######################################################################

        job_text = self.job.to_text()

    #######################################################################
    # Cross Encoder
    #######################################################################

        candidate_documents = [

            self.document_builder.build(
                candidate
            )["text"]

            for candidate in self.candidates
        ]

        semantic_scores = self.cross_encoder.score_batch(
            job_description=job_text,
            candidate_documents=candidate_documents,
        )

    #######################################################################
    # Store Semantic Scores
    #######################################################################

        for candidate, score in zip(
            self.candidates,
            semantic_scores,
        ):

            candidate.scores.semantic_score = score

    #######################################################################
    # Feature Scoring
    #######################################################################

        for candidate in self.candidates:

            self.feature_scorer.score(
               candidate,
            )

    #######################################################################
    # Final Score Fusion
    #######################################################################

        self.final_score_fusion.score_all(
            self.candidates,
        )

    #######################################################################
    # Final Ranking
    #######################################################################

        self.candidates = self.ranking_engine.rank(
            self.candidates,
        )

       
        ###########################################################################
    # Reasoning
    ###########################################################################

    def _reason(self) -> None:
        """
        Generate explainable hiring reasons.
        """

        if self.job is None:
            raise RuntimeError(
                "Job description has not been loaded."
            )

        for candidate in self.candidates:

        #######################################################################
        # Collect Evidence
        #######################################################################

            evidence = self.evidence_collector.collect(
                candidate,
                self.job,
            )

        #######################################################################
        # Analyze Evidence
        #######################################################################

            evidence = self.evidence_analyzer.analyze(
                evidence,
            )
 
        #######################################################################
        # Store
        #######################################################################

            candidate.evidence = evidence

        #######################################################################
        # Generate Explanation
        #######################################################################

            self.reason_generator.generate(
              candidate,
        )  
    
    ###########################################################################
    # Submission
    ###########################################################################

    def _submit(self) -> None:
        """
        Generate submission CSV.
        """

        output_path = (
            self.output_directory
            / "submission.csv"
        )

        self.submission_generator.generate(
            candidates=self.candidates,
            output_path=output_path,
        )

    ###########################################################################
    # Run Pipeline
    ###########################################################################

    def run(self) -> None:
        """
        Execute the Athena pipeline.
        """

        #######################################################################
        # Pipeline Timer
        #######################################################################

        self.benchmark.start_pipeline()

        #######################################################################
        # Load
        #######################################################################

        self._load()

        #######################################################################
        # Preprocessing
        #######################################################################

        self.benchmark.start_preprocessing()

        self._preprocess()

        self.benchmark.stop_preprocessing()

        #######################################################################
        # Retrieval
        #######################################################################

        self.benchmark.start_retrieval()

        self._retrieve()

        self.benchmark.stop_retrieval()

        #######################################################################
        # Ranking
        #######################################################################

        self.benchmark.start_ranking()

        self._rank()

        self.benchmark.stop_ranking()

        #######################################################################
        # Reasoning
        #######################################################################

        self.benchmark.start_reasoning()

        self._reason()

        self.benchmark.stop_reasoning()

        #######################################################################
        # Submission
        #######################################################################

        self._submit()

        #######################################################################
        # Benchmark
        #######################################################################

        self.benchmark_result = (
            self.benchmark.stop_pipeline()
        )
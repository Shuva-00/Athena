from src.config import settings

print("========== ATHENA CONFIG TEST ==========\n")

print(settings.project.name)
print(settings.project.version)

print(settings.environment.mode)

print(settings.models.embedding.model_name)
print(settings.models.cross_encoder.model_name)

print(settings.retrieval.bm25.top_k)
print(settings.retrieval.dense.top_k)
print(settings.retrieval.fusion.final_top_k)

print(settings.ranking.ranking.final_top_k)
print(settings.ranking.cross_encoder.batch_size)

###############################################################################
# Weight Configuration
###############################################################################

print(settings.weights.fusion.cross_encoder)
print(settings.weights.fusion.feature_score)

print(settings.weights.feature_scoring.skill.matching)
print(settings.weights.feature_scoring.skill.confidence)
print(settings.weights.feature_scoring.skill.duration)
print(settings.weights.feature_scoring.skill.endorsement)
print(settings.weights.feature_scoring.skill.semantic)

print(settings.weights.feature_scoring.experience.relevance)
print(settings.weights.feature_scoring.experience.stability)
print(settings.weights.feature_scoring.experience.leadership)
print(settings.weights.feature_scoring.experience.semantic)

print(settings.weights.normalization.duration_cap_months)
print(settings.weights.normalization.endorsement_cap)
print(settings.weights.fusion.cross_encoder)

print(settings.features.thresholds.minimum_strong_skill_match)

print(settings.paths.input.candidates)
print(settings.paths.output.submission_csv)

print(settings.logging.logger.name)
print(settings.logging.logger.level)

print("\nConfiguration loaded successfully.")
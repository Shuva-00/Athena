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

print(settings.weights.features.skill_match)
print(settings.weights.fusion.cross_encoder)

print(settings.features.thresholds.minimum_strong_skill_match)

print(settings.paths.input.candidates)
print(settings.paths.output.submission_csv)

print(settings.logging.logger.name)
print(settings.logging.logger.level)

print("\nConfiguration loaded successfully.")
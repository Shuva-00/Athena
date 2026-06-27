from src.config import settings

print(settings.project.name)
print(settings.project.version)

print(settings.environment.mode)

print(settings.models.embedding.model_name)
print(settings.models.cross_encoder.model_name)

print(settings.retrieval.bm25.top_k)
print(settings.retrieval.dense.top_k)

print(settings.weights.features.skill_match)

print(settings.paths.input.candidates)
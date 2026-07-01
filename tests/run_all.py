import subprocess
import sys

TESTS = [
    "test_domain_models.py",
    "test_config.py",
    "-m tests.test_skill_pipeline",
    "-m tests.test_experience_pipeline",
    "-m tests.test_education_pipeline",
    "-m tests.test_certification_pipeline",
    "-m tests.test_signal_pipeline",
    "-m tests.test_integrity_pipeline",
    "-m tests.test_feature_fusion",
    "-m tests.test_engine_ranking",
]

for test in TESTS:
    if test.startswith("-m"):
        args = [sys.executable] + test.split()
    else:
        args = [sys.executable, test]

    print(f"Running: {' '.join(args)}")
    subprocess.run(args, check=True)

print("\nAll tests passed.")
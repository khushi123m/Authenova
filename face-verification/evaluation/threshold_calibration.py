import numpy as np


def classify(similarity, threshold):
    return similarity >= threshold


same_person_scores = [
    1.0000,
    # Add more genuine-pair scores here
]

different_person_scores = [
    0.5355,
    # Add more impostor-pair scores here
]


thresholds = np.arange(0.50, 0.96, 0.05)

print("\n===== THRESHOLD CALIBRATION =====")

for threshold in thresholds:
    false_accepts = sum(
        classify(score, threshold)
        for score in different_person_scores
    )

    false_rejects = sum(
        not classify(score, threshold)
        for score in same_person_scores
    )

    print(
        f"Threshold: {threshold:.2f} | "
        f"False Accepts: {false_accepts} | "
        f"False Rejects: {false_rejects}"
    )
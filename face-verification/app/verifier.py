import numpy as np


def cosine_similarity(embedding1, embedding2):
    """
    Calculate cosine similarity between two face embeddings.
    """

    vector1 = np.array(embedding1)
    vector2 = np.array(embedding2)

    similarity = np.dot(vector1, vector2) / (
        np.linalg.norm(vector1) * np.linalg.norm(vector2)
    )

    return float(similarity)


def verify_faces(embedding1, embedding2, threshold=0.70):
    """
    Compare two face embeddings and return verification result.
    """

    similarity = cosine_similarity(embedding1, embedding2)

    if similarity >= threshold:
        result = "PASS"
    else:
        result = "FAIL"

    return similarity, result
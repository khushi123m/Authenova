from app.embedder import generate_embedding
from app.verifier import verify_faces


def verify_images(reference_image, test_image, threshold=0.70):
    """
    Verify whether two images belong to the same person.

    Returns:
        Dictionary containing verification result.
    """

    if not reference_image:
        raise ValueError("Reference image path is required.")

    if not test_image:
        raise ValueError("Test image path is required.")

    try:
        reference_embedding = generate_embedding(reference_image)
        test_embedding = generate_embedding(test_image)

        similarity, result = verify_faces(
            reference_embedding,
            test_embedding,
            threshold
        )

        return {
            "verified": result == "PASS",
            "similarity": round(similarity, 4),
            "threshold": threshold,
            "result": result
        }

    except Exception as error:
        return {
            "verified": False,
            "similarity": None,
            "threshold": threshold,
            "result": "ERROR",
            "error": str(error)
        }
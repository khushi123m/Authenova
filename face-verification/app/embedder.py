from deepface import DeepFace


def generate_embedding(image_path):
    """
    Generate a face embedding for an image.

    Args:
        image_path: Path to the face image.

    Returns:
        A list containing the face embedding.
    """

    result = DeepFace.represent(
        img_path=image_path,
        model_name="Facenet",
        enforce_detection=True
    )

    return result[0]["embedding"]
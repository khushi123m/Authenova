import numpy as np
from PIL import Image
from io import BytesIO

from keras_facenet import FaceNet


# Load FaceNet model once when the application starts
embedder = FaceNet()


def generate_embedding(image_data):
    """
    Generate a face embedding from image bytes.

    Args:
        image_data: Raw image bytes.

    Returns:
        NumPy array containing the face embedding.

    Raises:
        ValueError: If no face is detected.
    """

    try:
        # -----------------------------------------
        # 1. Convert uploaded bytes to PIL image
        # -----------------------------------------
        image = Image.open(BytesIO(image_data)).convert("RGB")

        # -----------------------------------------
        # 2. Convert PIL image to NumPy array
        # -----------------------------------------
        image_array = np.asarray(image)

        # -----------------------------------------
        # 3. Detect face and generate embedding
        # -----------------------------------------
        embeddings = embedder.extract(
            image_array,
            threshold=0.70
        )

        # -----------------------------------------
        # 4. Check whether a face was detected
        # -----------------------------------------
        if not embeddings:
            raise ValueError("No face detected in image.")

        # -----------------------------------------
        # 5. Use the first detected face
        # -----------------------------------------
        embedding = embeddings[0]["embedding"]

        return np.asarray(embedding, dtype=np.float32)

    except ValueError:
        raise

    except Exception as e:
        raise ValueError(
            f"Unable to process image: {str(e)}"
        )
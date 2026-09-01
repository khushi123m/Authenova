
import numpy as np
from PIL import Image
from io import BytesIO

from keras_facenet import FaceNet


# Load the FaceNet model once when the application starts
embedder = FaceNet()


def generate_embedding(image_data):
    """
    Generate a face embedding from image bytes.

    Args:
        image_data: Image bytes.

    Returns:
        NumPy array containing the face embedding.

    Raises:
        ValueError: If no face is detected.
    """

    try:
        # Convert bytes into a PIL image
        image = Image.open(BytesIO(image_data)).convert("RGB")

        # Convert PIL image to NumPy array
        image_array = np.asarray(image)

        # Generate embeddings
        embeddings = embedder.extract(image_array, threshold=0.95)

        # No face detected
        if not embeddings:
            raise ValueError("No face detected in image.")

        # Use the first detected face
        embedding = embeddings[0]["embedding"]

        return np.asarray(embedding, dtype=np.float32)

    except ValueError:
        raise

    except Exception as e:
        raise ValueError(f"Unable to process image: {str(e)}")


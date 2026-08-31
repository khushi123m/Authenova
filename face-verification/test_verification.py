from app.embedder import generate_embedding
from app.verifier import verify_faces


reference_image = "test_images/face_image.png"
test_image = "test_images/different_face.jpg"

print("Generating reference embedding...")
reference_embedding = generate_embedding(reference_image)

print("Generating test embedding...")
test_embedding = generate_embedding(test_image)

similarity, result = verify_faces(
    reference_embedding,
    test_embedding
)

print()
print("===== FACE VERIFICATION =====")
print("Similarity:", similarity)
print("Result:", result)
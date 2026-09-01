from app.embedder import generate_embedding
from app.verifier import cosine_similarity


reference = "test_images/face_image.png"
different = "test_images/different_face.png"


print("Generating reference embedding...")
reference_embedding = generate_embedding(reference)

print("Generating same-person embedding...")
same_embedding = generate_embedding(reference)

print("Generating different-person embedding...")
different_embedding = generate_embedding(different)


same_score = cosine_similarity(
    reference_embedding,
    same_embedding
)

different_score = cosine_similarity(
    reference_embedding,
    different_embedding
)


print("\n===== THRESHOLD EVALUATION =====")
print(f"Same-person similarity:      {same_score:.4f}")
print(f"Different-person similarity: {different_score:.4f}")
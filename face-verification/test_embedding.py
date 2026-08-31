from app.embedder import generate_embedding


image_path = "test_images/detected_face_1.jpg"

embedding = generate_embedding(image_path)

print("Embedding generated successfully!")
print("Embedding length:", len(embedding))
print("First 5 values:", embedding[:5])
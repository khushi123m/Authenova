from app.verifier import cosine_similarity, verify_faces


def test_same_embedding():
    embedding = [1.0, 2.0, 3.0]

    similarity, result = verify_faces(
        embedding,
        embedding,
        threshold=0.70
    )

    assert similarity > 0.99
    assert result == "PASS"


def test_different_embeddings():
    embedding1 = [1.0, 0.0, 0.0]
    embedding2 = [0.0, 1.0, 0.0]

    similarity, result = verify_faces(
        embedding1,
        embedding2,
        threshold=0.70
    )

    assert similarity < 0.70
    assert result == "FAIL"


def test_cosine_similarity():
    embedding1 = [1.0, 0.0]
    embedding2 = [1.0, 0.0]

    similarity = cosine_similarity(
        embedding1,
        embedding2
    )

    assert similarity > 0.99
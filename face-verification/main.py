import json

result = {
    "face_detected": True,
    "document_face_detected": True,
    "presented_face_detected": True,
    "similarity_score": 0.92,
    "verification": "pass"
}

json_result = json.dumps(result)

print(json_result)
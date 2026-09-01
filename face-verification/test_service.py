import json

from app.service import verify_images


reference_image = "test_images/face_image.png"
test_image = "test_images/different_face.jpg"


result = verify_images(
    reference_image,
    test_image
)


print("===== VERIFICATION RESULT =====")
print(json.dumps(result, indent=4))
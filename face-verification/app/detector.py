import cv2


FACE_CASCADE = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


def detect_faces(image_path):
    """
    Detect faces in an image.

    Returns:
        image: original image
        faces: list of face bounding boxes
    """

    image = cv2.imread(image_path)

    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = FACE_CASCADE.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(50, 50)
    )

    return image, list(faces)


def crop_face(image, face):
    """
    Crop one detected face from the image.
    """

    x, y, width, height = face

    face_image = image[y:y + height, x:x + width]

    return face_image


if __name__ == "__main__":

    image_path = input("Enter image path: ")

    try:
        image, faces = detect_faces(image_path)

        print(f"Faces detected: {len(faces)}")

        for i, face in enumerate(faces, start=1):

            print(f"Face {i}: {face}")

            cropped_face = crop_face(image, face)

            output_path = f"test_images/detected_face_{i}.jpg"

            cv2.imwrite(output_path, cropped_face)

            print(f"Saved: {output_path}")

    except ValueError as error:
        print(f"Error: {error}")
import cv2
import pytesseract
from pytesseract import Output


def extract_text_and_confidence(image_path):
    image = cv2.imread(image_path)

    extracted_text = pytesseract.image_to_string(image)

    data = pytesseract.image_to_data(image, output_type=Output.DICT)

    confidences = []
    for i in range(len(data["text"])):
        word = data["text"][i]
        confidence = data["conf"][i]
        if word.strip():
            confidences.append(confidence)

    average_confidence = round(sum(confidences) / len(confidences) / 100, 2)

    return extracted_text, average_confidence


if __name__ == "__main__":
    text, confidence = extract_text_and_confidence("../../../../data/samples/documents/test_document.png")
    print("--- RAW TEXT ---")
    print(text)
    print("--- CONFIDENCE ---")
    print(confidence)
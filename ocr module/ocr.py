import cv2
import pytesseract
from pytesseract import Output

image = cv2.imread("test_document.png")

extracted_text = pytesseract.image_to_string(image)

print("--- RAW TEXT TESSERACT FOUND ---")
print(extracted_text)

data = pytesseract.image_to_data(image, output_type=Output.DICT)

confidences = []   # <-- NEW: empty bucket to collect confidence numbers

print("\n--- WORD-LEVEL DATA ---")
for i in range(len(data["text"])):
    word = data["text"][i]
    confidence = data["conf"][i]
    if word.strip():
        print(f"word: {word!r}   confidence: {confidence}")
        confidences.append(confidence)   # <-- NEW: save this number into the bucket

print("\n--- ALL COLLECTED CONFIDENCES ---")
print(confidences)
average_confidence = sum(confidences) / len(confidences)
average_confidence = round(average_confidence / 100, 2)

print("\n--- AVERAGE CONFIDENCE ---")
print(average_confidence)


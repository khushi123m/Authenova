import cv2
import pytesseract

# Load the image from disk into memory as a grid of pixel numbers.
image = cv2.imread("test_document.png")

# Hand that image over to Tesseract and get back whatever text it found.
extracted_text = pytesseract.image_to_string(image)

print("--- RAW TEXT TESSERACT FOUND ---")
print(extracted_text)
from pytesseract import Output

data = pytesseract.image_to_data(image, output_type=Output.DICT)

print("\n--- WORD-LEVEL DATA ---")
for i in range(len(data["text"])):
    word = data["text"][i]
    confidence = data["conf"][i]
    if word.strip():  # skip empty entries (gaps between words)
        print(f"word: {word!r}   confidence: {confidence}")

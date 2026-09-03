import json
import re
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


def extract_passport_number(text):
    match = re.search(r"\b[A-Z]\d{7}\b", text)

    if match:
        return match.group()
    else:
        return None

def extract_name(text):
    match = re.search(r"NAME:\s*(.+)", text)

    if match:
        return match.group(1).strip()
    return None

def extract_dob(text):
    match = re.search(r"DATE OF BIRTH\s+(\d{2}/\d{2}/\d{4})", text)

    if match:
        return match.group(1)
    return None


def extract_expiry(text):
    match = re.search(r"DATE OF EXPIRY\s+(\d{2}/\d{2}/\d{4})", text)

    if match:
        return match.group(1)
    return None

def extract_nationality(text):
    match = re.search(r"NATIONALITY[:\s]+([A-Z]+)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return None

def extract_document_type(text):
    if re.search(r"\bPASSPORT\b", text, re.IGNORECASE):
        return "PASSPORT"
    return "UNKNOWN"

def extract_document(image_path):
    text, confidence = extract_text_and_confidence(image_path)

    passport_number = extract_passport_number(text)
    name = extract_name(text)
    dob = extract_dob(text)
    expiry = extract_expiry(text)
    document_type = extract_document_type(text)

    result = {
        "document_type": document_type,
        "name": name,
        "passport_number": passport_number,
        "date_of_birth": dob,
        "date_of_expiry": expiry,
        "ocr_confidence": confidence
    }

    return result

if __name__ == "__main__":
    text, confidence = extract_text_and_confidence(
        "../../../../data/samples/documents/test_document.png"
    )

    print("--- RAW TEXT ---")
    print(text)

    print("--- CONFIDENCE ---")
    print(confidence)

    passport_number = extract_passport_number(text)

    print("--- PASSPORT NUMBER ---")
    print(passport_number)

    name = extract_name(text)

    print("--- NAME ---")
    print(name)

    dob = extract_dob(text)

    print("--- DATE OF BIRTH ---")
    print(dob)

    expiry = extract_expiry(text)

    print("--- DATE OF EXPIRY ---")
    print(expiry)

    document_type = extract_document_type(text)

    print("--- DOCUMENT TYPE ---")
    print(document_type)

    result = {
        "document_type": document_type,
        "name": name,
        "passport_number": passport_number,
        "date_of_birth": dob,
        "date_of_expiry": expiry,
        "ocr_confidence": confidence
    }

    print(json.dumps(result, indent=4))
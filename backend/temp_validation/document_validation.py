import datetime
import re
def check_expiry(expiry_text):
    expiry_date=datetime.datetime.strptime(expiry_text,"%Y-%m-%d").date()
    today=datetime.date.today()

    if today < expiry_date:
     return {"status":"PASS", "reason":f"Document is valid upto {expiry_date}."}
    else:
        return {"status":"FAIL", "reason":f"Document is expired on {expiry_date}."}

def check_passport_format(passport_number):
   pattern=r"^[A-Z]\d{7}$"

   if re.fullmatch(pattern,passport_number):
      return {"status":"PASS", "reason":f"passport format number is valid"}
   else:
      return {"status":"FAIL", "reason":f"passport format number is invalid"}

def check_aadhaar_format(aadhaar_number):
   pattern=r"^\d{12}$"

   if re.fullmatch(pattern,aadhaar_number):
      return {"status":"PASS", "reason":f"Aadhaar number is valid"}
   else:
      return{"status":"FAIL", "reason":f"Aadhaar number is invald"}

def check_document_type(document_type):
    allowed_types = ["passport", "visa", "aadhaar", "permit"]
    normalized_type = document_type.lower()

    if normalized_type in allowed_types:
        return {"status": "PASS", "reason": f"'{document_type}' is a recognized document type."}
    else:
        return {"status": "FAIL", "reason": f"'{document_type}' is not a recognized document type."}

def check_name(name):
    if name.strip() == "":
        return {"status": "FAIL", "reason": "Name field is empty or unreadable."}
    else:
        return {"status": "PASS", "reason": f"Name '{name}' extracted successfully."}

def check_dob(dob_text):
    dob = datetime.datetime.strptime(dob_text, "%Y-%m-%d").date()
    today = datetime.date.today()

    if dob >= today:
        return {"status": "FAIL", "reason": f"Date of birth {dob} is not in the past."}
    else:
        return {"status": "PASS", "reason": f"Date of birth {dob} is valid."}

def check_nationality(nationality):
    if nationality.strip() == "":
        return {"status": "FAIL", "reason": "Nationality field is empty or unreadable."}
    else:
        return {"status": "PASS", "reason": f"Nationality '{nationality}' extracted successfully."}

def calculate_validation_risk(validation_report):
    total_fields = len(validation_report)
    failed_fields = 0

    for field_name in validation_report:
        if validation_report[field_name]["status"] == "FAIL":
            failed_fields = failed_fields + 1

    risk_score = (failed_fields / total_fields) * 100
    return risk_score

def calculate_tampering_risk(tampering_score):
    risk_score = round(tampering_score * 100, 2)

    if risk_score < 30:
        reason = f"Low tampering risk ({risk_score:.0f}% probability of digital editing)."
    elif risk_score < 70:
        reason = f"Moderate tampering risk ({risk_score:.0f}% probability of digital editing)."
    else:
        reason = f"High tampering risk ({risk_score:.0f}% probability of digital editing)."

    return {"risk_score": risk_score, "reason": reason}

def calculate_face_risk(similarity_score):
    risk_score = round(100 - (similarity_score * 100), 2)

    if risk_score < 30:
        reason = f"Low face-mismatch risk ({risk_score:.0f}% risk, faces closely match)."
    elif risk_score < 70:
        reason = f"Moderate face-mismatch risk ({risk_score:.0f}% risk, partial match)."
    else:
        reason = f"High face-mismatch risk ({risk_score:.0f}% risk, faces do not match well)."

    return {"risk_score": risk_score, "reason": reason}

def validate_document(document):
    report = {}
    if "document_type" in document:
        report["document_type"] = check_document_type(document["document_type"])
    else:
        report["document_type"] = {"status": "FAIL", "reason": "Document type is missing."}

    if "name" in document:
        report["name"] = check_name(document["name"])
    else:
        report["name"] = {"status": "FAIL", "reason": "Name is missing."}

    if "nationality" in document:
        report["nationality"] = check_nationality(document["nationality"])
    else:
        report["nationality"] = {"status": "FAIL", "reason": "Nationality is missing."}

    if "date_of_birth" in document:
        report["date_of_birth"] = check_dob(document["date_of_birth"])
    else:
        report["date_of_birth"] = {"status": "FAIL", "reason": "Date of birth is missing."}

    if "expiry_date" in document:
        report["expiry_date"] = check_expiry(document["expiry_date"])
    else:
        report["expiry_date"] = {"status": "FAIL", "reason": "Expiry date is missing."}

     # ID number check depends on document type
    doc_type = document.get("document_type", "").lower()
    if doc_type == "passport":
        if "passport_number" in document:
            report["passport_number"] = check_passport_format(document["passport_number"])
        else:
            report["passport_number"] = {"status": "FAIL", "reason": "Passport number is missing."}

    elif doc_type == "aadhaar":
        if "aadhaar_number" in document:
            report["id_number"] = check_aadhaar_format(document["aadhaar_number"])
        else:
            report["id_number"] = {"status": "FAIL", "reason": "Aadhaar number is missing."}

    else:
        report["id_number"] = {"status": "FAIL", "reason": f"No ID format check available for document type '{doc_type}'."}


   
    return report


sample_document = {
    "document_type": "aadhaar",
    "name": "TEST USER",
    "nationality": "Indian",
    "date_of_birth": "2000-01-15",
    "aadhaar_number": "123456781234",
    "expiry_date": "2030-05-10"
}

sample_report = validate_document(sample_document)
print(sample_report)
print(calculate_validation_risk(sample_report))

print(calculate_tampering_risk(0.15))
print(calculate_tampering_risk(0.55))
print(calculate_tampering_risk(0.90))

print(calculate_face_risk(0.95))   # very high similarity — what risk level do you expect?
print(calculate_face_risk(0.60))   # moderate similarity
print(calculate_face_risk(0.20))   # low similarity — what risk level do you expect?







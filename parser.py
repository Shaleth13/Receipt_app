# parser.py

import os
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import re

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".txt": #handling various file types
        with open(file_path, 'r') as f:
            return f.read()
    elif ext == ".pdf":
        pages = convert_from_path(file_path)
        return "\n".join(pytesseract.image_to_string(p) for p in pages)
    elif ext in [".jpg", ".jpeg", ".png"]:
        return pytesseract.image_to_string(Image.open(file_path))
    else:
        return "Unsupported file type"

def extract_fields(text): #extracting the details from the features mentioned in the receipt like vendor, date, amount and category
    vendor = text.strip().split("\n")[0]

    date_match = re.search(r'\d{2}[/-]\d{2}[/-]\d{4}', text)
    amount_match = re.search(
        r'(₹|Rs\.?|INR)?\s?\d{1,3}(?:,\d{3})*(?:\.\d{2})|Total\s*[:\-]?\s?\d+[.,]?\d*',
        text,
        re.IGNORECASE
    )

    return {
        "vendor": vendor.strip(),
        "date": date_match.group() if date_match else "N/A",
        "amount": amount_match.group() if amount_match else "N/A",
        "category": "General"
    }

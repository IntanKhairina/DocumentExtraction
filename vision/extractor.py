import pypdf
from pytesseract import pytesseract
from PIL import Image
import io

def extract_text_from_pdf(file_path: str) -> str:
    """Extract text from PDF"""
    try:
        reader = pypdf.PdfReader(file_path)
        text = "\n".join([page.extract_text() for page in reader.pages])
        return text if text.strip() else None
    except:
        return None

def extract_text_from_image(file_path: str) -> str:
    """Fallback: OCR from image"""
    try:
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)
    except:
        return None

def extract_text(file_path: str, file_type: str) -> str:
    """Route to right extractor"""
    if file_type == "pdf":
        text = extract_text_from_pdf(file_path)
    else:  # jpg, png
        text = extract_text_from_image(file_path)
    
    return text or "EXTRACTION_FAILED"
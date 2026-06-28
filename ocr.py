import os

import fitz
import pdfplumber
from PIL import Image
import pytesseract


IMAGE_FOLDER = "sample_receipts"


def extract_text_from_image(image_path, languages="eng"):
    """Extract OCR text from an image using local Tesseract.

    Args:
        image_path: Path to an image file.
        languages: Tesseract language codes, for example ``eng`` or
            ``eng+hin`` when Hindi data is installed locally.

    Returns:
        OCR text as a string.
    """
    image = Image.open(image_path)
    return pytesseract.image_to_string(image, lang=languages)


def extract_text_from_processed_image(image, languages="eng"):
    """Extract OCR text from a preprocessed OpenCV image array."""
    return pytesseract.image_to_string(image, lang=languages)


def extract_text_from_pdf(pdf_path, languages="eng"):
    """Extract text from a PDF using local tools.

    Embedded text is extracted with pdfplumber first. Pages without embedded
    text are rendered locally with PyMuPDF and passed to Tesseract.
    """
    page_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text.append(page.extract_text() or "")

    if any(text.strip() for text in page_text):
        return "\n".join(page_text)

    document = fitz.open(pdf_path)
    rendered_text = []
    for page in document:
        pixmap = page.get_pixmap(dpi=200)
        image = Image.frombytes(
            "RGB",
            [pixmap.width, pixmap.height],
            pixmap.samples,
        )
        rendered_text.append(pytesseract.image_to_string(image, lang=languages))
    return "\n".join(rendered_text)


def read_receipt_folder(folder_path=IMAGE_FOLDER, languages="eng"):
    """Extract text from every image in a folder.

    Args:
        folder_path: Directory containing receipt image files.
        languages: Tesseract language code string.

    Returns:
        A dictionary mapping file names to extracted text.
    """
    results = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith((".png", ".jpg", ".jpeg")):
            image_path = os.path.join(folder_path, filename)
            results[filename] = extract_text_from_image(image_path, languages)
    return results


if __name__ == "__main__":
    for filename, text in read_receipt_folder().items():
        print("=" * 50)
        print(f"Reading: {filename}")
        print(text)
        print("=" * 50)

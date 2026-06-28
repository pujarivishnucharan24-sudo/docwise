"""Streamlit interface for DocWise AI."""

from __future__ import annotations

from pathlib import Path

import streamlit as st

from database import list_receipts, save_receipt
from export import export_receipts_to_csv, export_receipts_to_json
from image_processing import preprocess_image
from ocr import extract_text_from_pdf, extract_text_from_processed_image
from parser import parse_receipt_text


UPLOAD_DIR = Path("uploads")
REPORT_DIR = Path("reports")


def process_upload(uploaded_file, languages):
    """Run OCR, parsing, and persistence for one uploaded file."""
    UPLOAD_DIR.mkdir(exist_ok=True)
    file_path = UPLOAD_DIR / uploaded_file.name
    file_path.write_bytes(uploaded_file.getbuffer())

    if file_path.suffix.lower() == ".pdf":
        text = extract_text_from_pdf(file_path, languages=languages)
    else:
        processed_image = preprocess_image(str(file_path))
        text = extract_text_from_processed_image(processed_image, languages=languages)

    receipt = parse_receipt_text(text)
    receipt_id = save_receipt(receipt)
    receipt["id"] = receipt_id
    return receipt


def main():
    """Render the DocWise AI Streamlit app."""
    st.set_page_config(page_title="DocWise AI", layout="wide")
    st.title("DocWise AI")

    languages = st.text_input("Tesseract languages", value="eng")
    uploaded_file = st.file_uploader(
        "Upload receipt image or PDF",
        type=["png", "jpg", "jpeg", "pdf"],
    )

    if uploaded_file and st.button("Process receipt"):
        receipt = process_upload(uploaded_file, languages)
        st.success(f"Saved receipt #{receipt['id']}")
        st.json(receipt)

    receipts = list_receipts()
    st.subheader("Stored expenses")
    st.dataframe(receipts, use_container_width=True)

    col_csv, col_json = st.columns(2)
    with col_csv:
        if st.button("Export CSV"):
            output_path = export_receipts_to_csv(receipts, REPORT_DIR / "receipts.csv")
            st.success(f"Exported {output_path}")
    with col_json:
        if st.button("Export JSON"):
            output_path = export_receipts_to_json(receipts, REPORT_DIR / "receipts.json")
            st.success(f"Exported {output_path}")


if __name__ == "__main__":
    main()

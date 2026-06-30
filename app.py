import pytesseract
from pytesseract import TesseractNotFoundError

try:
    text = pytesseract.image_to_string(image)
except TesseractNotFoundError:
    import streamlit as st

    st.error(
        "Tesseract OCR is not installed on this deployment. "
        "Deploy this app on Render or install the Tesseract binary."
    )
    st.stop()

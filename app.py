"""DocWise Streamlit OCR app."""

from PIL import Image
import pytesseract
import streamlit as st
from pytesseract import TesseractNotFoundError


def extract_text(image: Image.Image) -> str:
    """Extract text from an uploaded image."""
    try:
        return pytesseract.image_to_string(image)
    except TesseractNotFoundError:
        return (
            "Tesseract OCR is not installed or not found. "
            "Please install Tesseract and try again."
        )


def main() -> None:
    """Run the Streamlit app."""
    st.title("DocWise")
    st.write("Upload an image to extract text using OCR.")

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["png", "jpg", "jpeg"],
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded image", use_container_width=True)

        text = extract_text(image)
        st.subheader("Extracted Text")
        st.text_area("OCR Output", text, height=300)


if __name__ == "__main__":
    main()

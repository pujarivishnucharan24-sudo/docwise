import cv2


def preprocess_image(image_path):
    """Preprocess a receipt image for OCR.

    Args:
        image_path: Path to a receipt, invoice, or bill image.

    Returns:
        A thresholded OpenCV image array suitable for Tesseract OCR.

    Raises:
        FileNotFoundError: If OpenCV cannot read the image.
    """
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Unable to read image: {image_path}")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    processed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    return processed


if __name__ == "__main__":
    image_path = "sample_receipts/receipt1.jpg"
    processed = preprocess_image(image_path)
    cv2.imshow("Processed Image", processed)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

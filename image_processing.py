import cv2

def preprocess_image(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Reduce noise
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply thresholding
    processed = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )[1]

    return processed


# Test the function
if __name__ == "__main__":
    image_path = "sample_receipts/receipt1.jpg"

    processed = preprocess_image(image_path)

    cv2.imshow("Processed Image", processed)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
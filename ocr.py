import os
from PIL import Image
import pytesseract

# Path to the folder containing receipt images
IMAGE_FOLDER = "sample_receipts"

# Process all image files
for filename in os.listdir(IMAGE_FOLDER):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        image_path = os.path.join(IMAGE_FOLDER, filename)

        print("=" * 50)
        print(f"Reading: {filename}")

        image = Image.open(image_path)

        text = pytesseract.image_to_string(image)

        print(text)
        print("=" * 50)

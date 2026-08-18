import cv2
import pytesseract
import os

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

def scan_image(filename):

    if not os.path.exists(filename):
        print("Image file not found.")
        return

    image = cv2.imread(filename)

    if image is None:
        print("Unable to read image.")
        return

    # Conv image to grayscale
    gray = cv2.cvtColor(
        image,
        cv2.COLOR_BGR2GRAY
    )

    # Remove noise
    gray = cv2.GaussianBlur(
        gray,
        (5, 5),
        0
    )

    # Convert to black and white
    _, threshold = cv2.threshold(
        gray,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    # Extract text
    text = pytesseract.image_to_string(threshold)

    print("\n" + "=" * 50)
    print("              OCR TEXT")
    print("=" * 50)

    if text.strip():

        print(text)

    else:

        print("No text detected.")

    # Save extracted text as txt formate
    output_file = "extracted_text.txt"

    with open(
        output_file,
        "w",
        encoding="utf-8") as file:

        file.write(text)

    print("=" * 50)
    print(f"Text saved to: {output_file}")

print("=" * 45)
print("          OCR TEXT SCANNER")
print("=" * 45)

filename = input("Enter image filename: ").strip()

scan_image(filename)
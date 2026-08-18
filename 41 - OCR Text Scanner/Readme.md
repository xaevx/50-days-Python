# OCR Text Scanner

A simple **OCR (Optical Character Recognition) Text Scanner** built with Python, OpenCV, and Tesseract OCR.

The program extracts text from an image and saves the detected text into a `.txt` file.

## Features

* Read text from images
* OCR text extraction
* Image preprocessing
* Grayscale conversion
* Noise reduction
* Image thresholding
* Save extracted text
* Generate a text file

## Requirements

Install the Python packages:

```bash
python -m pip install opencv-python pytesseract
```

You also need to install **Tesseract OCR** separately because `pytesseract` is only a Python interface for the Tesseract engine.

## Run the Project

*IMPORTANT* : Place an image in the project directory (I have already placed an image in the folder so you don't need to place it again)

```text
OCR-Text-Scanner/
│
├── OCR_Text_Scanner.py
├── test.jpg
└── Readme.md
```

Run:

```bash
python OCR_Text_Scanner.py
```

Enter the image filename:

```text
Enter image filename: test.jpg
```

The extracted text will be displayed in the terminal and saved as:

```text
extracted_text.txt
```

## How It Works

```text
Input Image
     ↓
OpenCV
     ↓
Grayscale Conversion
     ↓
Noise Reduction
     ↓
Thresholding
     ↓
Tesseract OCR
     ↓
Text Extraction
     ↓
Display Text
     ↓
Save as TXT
```

## Image Preprocessing

Before sending the image to Tesseract, the program performs several preprocessing steps.

### Grayscale

Converts the image from:

```text
Color → Grayscale
```

### Gaussian Blur

Reduces small amounts of image noise.

### Thresholding

Converts the image into a black-and-white representation to make text easier for OCR to recognize.

## Modules Used

* Python 3
* OpenCV
* Pytesseract
* Tesseract OCR

## What i learned

* Optical Character Recognition
* Computer Vision
* Image Processing
* OpenCV
* Image Preprocessing
* File Handling
* Text Extraction
* Functions
* Exception Handling

> **Note:** OCR accuracy depends heavily on image quality, font, lighting, orientation, and preprocessing.

---

⭐ Part of my **#50DaysOfPython** challenge.

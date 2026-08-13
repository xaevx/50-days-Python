# Face Detection

A real-time **Face Detection** application built with Python and OpenCV. The program uses a webcam to detect human faces and draws bounding boxes around them.

## Features

- Real-time webcam detection
- Detect multiple faces
- Draw bounding boxes
- Display number of detected faces
- Real-time processing
- Press `q` to exit

## Requirements

Install OpenCV:

```bash
pip install opencv-python
```

## Run the Project

```bash
python Face_Detection.py
```

Allow camera access when requested.

Press:

```text
q
```

to close the application.


## Modules Used

- Python 3
- OpenCV
- Haar Cascade Classifier
- Computer Vision

## How It Works

```text
Webcam
   ↓
Capture Frame
   ↓
Convert to Grayscale
   ↓
Haar Cascade
   ↓
Detect Faces
   ↓
Draw Bounding Boxes
   ↓
Display Frame
```

## What i learned

- Computer Vision
- OpenCV
- Image Processing
- Webcam Access
- Haar Cascade Classifier
- Grayscale Conversion
- Bounding Boxes
- Real-Time Processing
- Loops

> **Note:** This project only detects faces. It does not identify who the person is.

---

⭐ Part of my **#50DaysOfPython** challenge.
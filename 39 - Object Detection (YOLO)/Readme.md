# YOLO Object Detection

A real-time **Object Detection** application built with Python, OpenCV, and YOLO.

The program uses a webcam to detect and classify objects in real time using the **YOLO11 Nano** model.

## Features

* Real-time webcam detection
* Detect multiple objects
* Display object names
* Display confidence scores
* Draw bounding boxes
* Count detected objects
* Real-time processing
* Automatically downloads the YOLO model
* Press `q` to exit

## Requirements

Install the required packages:

```bash
python -m pip install ultralytics opencv-python
```

## Run the Project

```bash
python Object_Detection.py
```

On the first run, Ultralytics automatically downloads the YOLO model.

Press:

```text
q
```

to close the application.

> The `yolo11n.pt` model file is automatically downloaded when the program is run for the first time.

## How It Works

```text
Webcam
   ↓
Capture Frame
   ↓
Flip Frame
   ↓
YOLO Model
   ↓
Object Detection
   ↓
Bounding Boxes
   ↓
Class Prediction
   ↓
Confidence Score
   ↓
Display Results
```

## What YOLO Detects

Almost everything! It's amazing!

## Detection Output

Each detected object provides:

```text
Object Name
Confidence Score
Bounding Box
```

Example:

```text
person 0.94
laptop 0.87
cell phone 0.81
```

## Modules Used

* Python 3
* OpenCV
* Ultralytics
* YOLO
* Computer Vision

## What i learned

* Object Detection
* YOLO
* Computer Vision
* Deep Learning
* Bounding Boxes
* Confidence Scores
* Image Processing
* Real-Time Inference
* Model Loading
* Webcam Processing

> **Note:** This project uses a pretrained YOLO model and is intended for educational purposes.

---

⭐ Part of my **#50DaysOfPython** challenge.

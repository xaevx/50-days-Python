# Pose Detection

A real-time **Pose Detection** application built with Python, OpenCV, and MediaPipe.

The program uses a webcam to detect human body poses and track body landmarks in real time.

## Features

* Real-time webcam pose detection
* Detect human body poses
* Track body landmarks
* Draw pose skeleton
* Detect multiple poses
* Display number of detected poses
* Automatically downloads the required model
* Real-time processing
* Press `q` to exit

## Requirements

Install the required packages:

```bash
python -m pip install mediapipe opencv-python
```

## Run the Project

```bash
python Pose_Detection.py
```

On the first run, the program automatically downloads the MediaPipe **Pose Landmarker Lite** model.

Press:

```text
q
```

to close the application.

> The `pose_landmarker_lite.task` file is downloaded automatically when the program is run for the first time.

## Modules Used

* Python 3
* OpenCV
* MediaPipe Tasks
* Computer Vision

## How It Works

```text
Webcam
   ↓
Capture Frame
   ↓
Flip Frame
   ↓
Convert BGR → RGB
   ↓
MediaPipe Pose Landmarker
   ↓
Detect Human Pose
   ↓
Extract Body Landmarks
   ↓
Calculate Pixel Coordinates
   ↓
Draw Pose Skeleton
   ↓
Display Frame
```

## Pose Landmarks

The MediaPipe Pose Landmarker tracks major body landmarks including:

* Nose
* Eyes
* Ears
* Shoulders
* Elbows
* Wrists
* Hips
* Knees
* Ankles
* Feet

Each landmark contains positional information:

```text
x → Horizontal position
y → Vertical position
z → Depth information
```

## What i learned

* Computer Vision
* MediaPipe Tasks API
* OpenCV
* Webcam Processing
* Pose Landmark Detection
* Coordinate Systems
* Image Processing
* Real-Time Processing
* Model Management
* Functions
* Loops

> **Note:** This project detects body pose landmarks but does not identify people or classify activities.

---

⭐ Part of my **#50DaysOfPython** challenge.

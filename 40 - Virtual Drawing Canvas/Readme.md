# Virtual Drawing Canvas

A real-time **Virtual Drawing Canvas** built with Python, OpenCV, MediaPipe, and NumPy.

The application uses hand tracking to detect the user's **index finger** and uses its position as a virtual pen for drawing on the screen.

## Features

* Real-time hand tracking
* Index finger tracking
* Draw without touching the screen
* Virtual canvas
* Clear canvas
* Webcam support
* Real-time processing
* Keyboard controls

## Controls

| Control         | Action       |
| --------------- | ------------ |
| Index Finger    | Draw         |
| `C`             | Clear Canvas |
| `Q`             | Quit         |

## Requirements

Install the required packages:

```bash
python -m pip install mediapipe opencv-python numpy
```

## Run the Project

```bash
python Virtual_Drawing_Canvas.py
```

On the first run, the program automatically downloads the MediaPipe hand landmark model.

Move your **index finger** in front of the camera to draw.

> The `hand_landmarker.task` file is automatically downloaded by the program.

## How It Works

```text
Webcam
   ↓
Capture Frame
   ↓
MediaPipe Hand Tracking
   ↓
Detect Hand
   ↓
Find Index Finger
   ↓
Extract Landmark 8
   ↓
Convert Normalized Coordinates
   ↓
Track Previous Position
   ↓
Draw Line
   ↓
Display Canvas
```

## Index Finger Landmark

MediaPipe provides 21 landmarks for each hand.

The index finger tip is:

```text
Landmark 8
```

The landmark provides normalized coordinates:

```text
x → Horizontal Position
y → Vertical Position
z → Depth
```

These coordinates are converted into actual pixel coordinates:

```python
x = int(index_finger.x * width)
y = int(index_finger.y * height)
```

The program then connects the current position to the previous position using:

```python
cv2.line()
```

This creates the continuous drawing effect.

## Modules Used

* Python 3
* OpenCV
* MediaPipe
* NumPy
* Computer Vision

## What i learned

* Hand Tracking
* Computer Vision
* MediaPipe
* OpenCV
* NumPy
* Coordinate Conversion
* Drawing with OpenCV
* Real-Time Processing
* Webcam Processing
* Landmark Tracking

> **Note:** This is an educational project. Drawing is controlled using the index finger detected by the webcam.

---

⭐ Part of my **#50DaysOfPython** challenge.

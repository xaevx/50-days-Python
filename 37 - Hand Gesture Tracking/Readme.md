# Hand Gesture Tracking

A real-time **Hand Gesture Tracking** application built with Python, OpenCV, and MediaPipe.

The application uses a webcam to detect hands and track **21 landmarks** for each detected hand in real time.

## Features

- Real-time webcam tracking
- Detect up to 2 hands
- Track 21 landmarks per hand
- Draw hand skeleton
- Display detected hand count
- Real-time processing
- Automatically downloads the required model
- Press `q` to exit

## Requirements

Install the required packages:

```bash
python -m pip install mediapipe opencv-python
```

## Run the Project

```bash
python Hand_Gesture_Tracking.py
```

On the first run, the program automatically downloads the MediaPipe hand landmark model.
Why this file? The ".task" file is the trained AI model that MediaPipe uses to actually detect the hand.

Press:

```text
q
```

to close the application.

## Modules Used

- Python 3
- OpenCV
- MediaPipe Tasks
- Computer Vision

## How this Project Works

```text
Webcam
   ↓
Capture Frame
   ↓
Flip Frame
   ↓
Convert BGR → RGB
   ↓
MediaPipe Hand Landmarker
   ↓
Detect Hands
   ↓
Extract 21 Landmarks
   ↓
Calculate Pixel Coordinates
   ↓
Draw Hand Skeleton
   ↓
Display Frame
```

## Hand Landmarks

Each detected hand contains 21 landmarks:

```text
0  - Wrist

1  - Thumb CMC
2  - Thumb MCP
3  - Thumb IP
4  - Thumb Tip

5  - Index MCP
6  - Index PIP
7  - Index DIP
8  - Index Tip

9  - Middle MCP
10 - Middle PIP
11 - Middle DIP
12 - Middle Tip

13 - Ring MCP
14 - Ring PIP
15 - Ring DIP
16 - Ring Tip

17 - Pinky MCP
18 - Pinky PIP
19 - Pinky DIP
20 - Pinky Tip
```

## What i learned

- Computer Vision
- MediaPipe Tasks API
- OpenCV
- Webcam Processing
- Hand Landmark Detection
- Coordinate Systems
- Image Processing
- Real-Time Processing
- Model Management
- Loops
- Functions

> **Note:** This project tracks hand landmarks but does not yet classify gestures such as Thumbs Up, Victory, Open Palm, or Fist.

---

⭐ Part of my **#50DaysOfPython** challenge.
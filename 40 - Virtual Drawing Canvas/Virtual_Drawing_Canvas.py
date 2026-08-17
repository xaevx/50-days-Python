import cv2
import mediapipe as mp
import numpy as np
import urllib.request
import os

MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/"
    "hand_landmarker/hand_landmarker/float16/1/"
    "hand_landmarker.task"
)

MODEL_FILE = "hand_landmarker.task"

def download_model():

    if os.path.exists(MODEL_FILE):
        return

    print("Downloading hand tracking model...")

    try:

        urllib.request.urlretrieve(
            MODEL_URL,
            MODEL_FILE
        )

        print("Model downloaded successfully.")

    except Exception as error:

        print("Failed to download model.")
        print("Error:", error)
        exit()

download_model()

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=MODEL_FILE
    ),
    running_mode=VisionRunningMode.VIDEO,
    num_hands=1,
    min_hand_detection_confidence=0.5,
    min_hand_presence_confidence=0.5,
    min_tracking_confidence=0.5
)

camera = cv2.VideoCapture(0)

if not camera.isOpened():

    print("Unable to access the camera.")
    exit()

canvas = None

previous_x = None
previous_y = None

frame_timestamp = 0

print("Virtual Drawing Canvas Started")
print("Move your index finger to draw.")
print("Press 'c' to clear the canvas.")
print("Press 'q' to quit.")


with HandLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = camera.read()

        if not success:

            print("Unable to read camera frame.")
            break

        frame = cv2.flip(frame, 1)

        if canvas is None:

            canvas = np.zeros_like(frame)

        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb_frame
        )

        frame_timestamp += 1

        results = landmarker.detect_for_video(
            mp_image,
            frame_timestamp
        )

        if results.hand_landmarks:

            hand = results.hand_landmarks[0]

            # Index finger tip = landmark 8

            index_finger = hand[8]

            height, width, _ = frame.shape

            x = int(index_finger.x * width)
            y = int(index_finger.y * height)


            cv2.circle(
                frame,
                (x, y),
                10,
                (0, 255, 0),
                -1
            )

            if previous_x is not None:

                cv2.line(
                    canvas,
                    (previous_x, previous_y),
                    (x, y),
                    (255, 255, 255),
                    5
                )

            previous_x = x
            previous_y = y

        else:

            previous_x = None
            previous_y = None

        # Combine camera frame and drawing canvas

        frame = cv2.add(
            frame,
            canvas
        )

        cv2.putText(
            frame,
            "C = Clear | Q = Quit",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.imshow(
            "Virtual Drawing Canvas",
            frame
        )

        key = cv2.waitKey(1) & 0xFF

        if key == ord("c"):

            canvas = np.zeros_like(frame)

            previous_x = None
            previous_y = None

        elif key == ord("q"):

            break

camera.release()
cv2.destroyAllWindows()
import cv2
import mediapipe as mp
import urllib.request
import os

MODEL_URL = (
    "https://storage.googleapis.com/mediapipe-models/"
    "pose_landmarker/pose_landmarker_lite/float16/1/"
    "pose_landmarker_lite.task"
)

MODEL_FILE = "pose_landmarker_lite.task"


def download_model():

    if os.path.exists(MODEL_FILE):
        return

    print("Downloading pose detection model...")

    try:

        urllib.request.urlretrieve(
            MODEL_URL,
            MODEL_FILE
        )

        print("Model downloaded successfully.")

    except Exception as error:

        print("Failed to download the model.")
        print("Error:", error)
        exit()


download_model()


BaseOptions = mp.tasks.BaseOptions
PoseLandmarker = mp.tasks.vision.PoseLandmarker
PoseLandmarkerOptions = mp.tasks.vision.PoseLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode


options = PoseLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path=MODEL_FILE
    ),
    running_mode=VisionRunningMode.VIDEO,
    num_poses=2,
    min_pose_detection_confidence=0.5,
    min_pose_presence_confidence=0.5,
    min_tracking_confidence=0.5
)


camera = cv2.VideoCapture(0)


if not camera.isOpened():

    print("Unable to access the camera.")
    exit()


print("Pose Detection Started")
print("Press 'q' to quit.")


frame_timestamp = 0


with PoseLandmarker.create_from_options(options) as landmarker:

    while True:

        success, frame = camera.read()

        if not success:

            print("Unable to read camera frame.")
            break

        frame = cv2.flip(frame, 1)

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

        pose_count = len(results.pose_landmarks)

        height, width, _ = frame.shape


        for pose_landmarks in results.pose_landmarks:

            # Draw landmarks

            for landmark in pose_landmarks:

                x = int(landmark.x * width)
                y = int(landmark.y * height)

                cv2.circle(
                    frame,
                    (x, y),
                    4,
                    (0, 255, 0),
                    -1
                )


            # Body connections

            connections = [

                (11, 12),

                (11, 13),
                (13, 15),

                (12, 14),
                (14, 16),

                (11, 23),
                (12, 24),

                (23, 24),

                (23, 25),
                (25, 27),

                (24, 26),
                (26, 28),

                (27, 29),
                (27, 31),

                (28, 30),
                (28, 32)

            ]


            for start, end in connections:

                x1 = int(
                    pose_landmarks[start].x * width
                )

                y1 = int(
                    pose_landmarks[start].y * height
                )

                x2 = int(
                    pose_landmarks[end].x * width
                )

                y2 = int(
                    pose_landmarks[end].y * height
                )


                cv2.line(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )


        # Display pose count

        cv2.putText(
            frame,
            f"Poses Detected: {pose_count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )


        # Display camera frame

        cv2.imshow(
            "Pose Detection",
            frame
        )


        # Quit with Q

        if cv2.waitKey(1) & 0xFF == ord("q"):

            break


camera.release()
cv2.destroyAllWindows()
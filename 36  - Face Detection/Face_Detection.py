import cv2


face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)


camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to access the camera.")
    exit()


print("Face Detection Initialized.")
print("Press 'q' to quit.")


while True:

    success, frame = camera.read()

    if not success:
        print("Unable to read camera frame, Check your camera.")
        break

    gray_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = face_cascade.detectMultiScale(
        gray_frame,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    for x, y, width, height in faces:

        cv2.rectangle(
            frame,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            "Face",
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2
        )

    cv2.putText(
        frame,
        f"Faces Detected: {len(faces)}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow(
        "Face Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


camera.release()
cv2.destroyAllWindows()
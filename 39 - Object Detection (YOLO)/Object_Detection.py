import cv2
from ultralytics import YOLO

MODEL_NAME = "yolo11n.pt"

model = YOLO(MODEL_NAME)

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Unable to access the camera.")
    exit()


print("YOLO Object Detection Started")
print("Press 'q' to quit.")


while True:

    success, frame = camera.read()

    if not success:
        print("Unable to read camera frame.")
        break

    frame = cv2.flip(frame, 1)

    results = model(
        frame,
        conf=0.5,
        verbose=False
    )

    detected_objects = 0

    for result in results:

        boxes = result.boxes

        detected_objects = len(boxes)

        for box in boxes:

            x1, y1, x2, y2 = box.xyxy[0].tolist()

            x1 = int(x1)
            y1 = int(y1)
            x2 = int(x2)
            y2 = int(y2)

            confidence = float(box.conf[0])

            class_id = int(box.cls[0])

            class_name = model.names[class_id]

            label = f"{class_name} {confidence:.2f}"

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (0, 255, 0),
                2
            )

            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.putText(
        frame,
        f"Objects Detected: {detected_objects}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )


    cv2.imshow(
        "YOLO Object Detection",
        frame
    )


    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()
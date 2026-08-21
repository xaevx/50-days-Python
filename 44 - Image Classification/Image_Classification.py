import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import (preprocess_input, decode_predictions)
from tensorflow.keras.utils import load_img, img_to_array

MODEL = MobileNetV2(weights="imagenet")

def classify_image(image_path):

    try:
        image = load_img(
            image_path,
            target_size=(224, 224)
        )

    except Exception as error:

        print("Unable to load image.")
        print("Error:", error)
        return

    # Converts image to array
    image_array = img_to_array(
        image
    )

    # Adds batch dimension
    image_array = tf.expand_dims(
        image_array,
        axis=0
    )

    # Preprocesses image
    image_array = preprocess_input(
        image_array
    )

    # Makes prediction
    predictions = MODEL.predict(
        image_array,
        verbose=0
    )

    # Get top 5 predictions
    results = decode_predictions(
        predictions,
        top=5
    )[0]

    print("\n" + "=" * 50)
    print("           IMAGE CLASSIFICATION")
    print("=" * 50)

    print(f"\nImage: {image_path}")

    print("\nTop Predictions:")
    print("-" * 50)

    for rank, (_, label, confidence) in enumerate(
        results,
        start=1
    ):

        percentage = confidence * 100

        print(
            f"{rank}. {label:<25} "
            f"{percentage:.2f}%"
        )

    best_label = results[0][1]
    best_confidence = results[0][2] * 100

    print("\n" + "-" * 50)

    print(
        f"Prediction: {best_label}"
    )

    print(
        f"Confidence: {best_confidence:.2f}%"
    )

    print("=" * 50)

print("=" * 45)
print("       IMAGE CLASSIFICATION")
print("=" * 45)

image_path = input(
    "Enter image path: "
).strip()

if not image_path:

    print("Please provide an image path.")

else:

    classify_image(
        image_path
    )
# Image Classification

A simple **Image Classification** application built with Python and TensorFlow that analyzes an image and predicts what category it belongs to.

The project uses **MobileNetV2**, a pretrained deep learning model trained on the ImageNet dataset.

## Features

- Image classification
- Pretrained deep learning model
- Predict image categories
- Display confidence scores
- Show top 5 predictions
- Image preprocessing
- No custom model training required

## Requirements

Install TensorFlow:

```bash
python -m pip install tensorflow
```

## Run the Project

```bash
python Image_Classification.py
```

Enter the image path when prompted:

```text
Enter image path: animal2.jpg
```

The program will analyze the image and display the top predictions.

Example:

```text
Top Predictions:
--------------------------------------------------
1. schipperke                31.96%
2. kelpie                    21.54%
3. Border_collie             9.65%
4. collie                    1.88%
5. groenendael               1.31%

--------------------------------------------------
Prediction: schipperke
Confidence: 31.96%
```

## How It Works

```text
Input Image
     ↓
Load Image
     ↓
Resize to 224 × 224
     ↓
Convert Image to Array
     ↓
Preprocess Image
     ↓
MobileNetV2
     ↓
ImageNet Prediction
     ↓
Top 5 Predictions
     ↓
Display Results
```

## Model Used

The project uses:

```text
MobileNetV2
```

with pretrained ImageNet weights:

```python
MobileNetV2(weights="imagenet")
```

The model can classify images into **1000 ImageNet categories**.

Examples include:

```text
Dog
Cat
Car
Bird
Elephant
Fish
Aircraft
Furniture
Sports Equipment
Food
```

## Confidence Score

The model provides a probability score for each predicted class.

For example:

```text
golden_retriever → 87.42%
```

The prediction with the highest confidence is selected as the primary result.

## Classification vs Object Detection

**Image Classification** answers:

```text
"What is this image?"
```

Example:

```text
Image → Dog
```

**Object Detection** answers:

```text
"What objects are present and where are they?"
```

Example:

```text
Image
 ├── Dog → Bounding Box
 ├── Person → Bounding Box
 └── Ball → Bounding Box
```

Day 39 used **YOLO Object Detection**, while Day 44 focuses on **Image Classification**.

## Modules Used

- Python 3
- TensorFlow
- Keras
- MobileNetV2
- ImageNet
- Deep Learning

## What i learned

- Image Classification
- Deep Learning
- Convolutional Neural Networks
- TensorFlow
- Keras
- MobileNetV2
- Transfer Learning
- Image Preprocessing
- Model Inference
- Confidence Scores
- Top-K Predictions
- Computer Vision

> **Note:** This project uses a pretrained MobileNetV2 model and does not train a custom model.

---

⭐ Part of my **#50DaysOfPython** challenge.
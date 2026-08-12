# Spam Detection

A simple **Spam Detection Machine Learning project** built with Python. The program learns to classify text messages as either **Spam** or **Ham (Not Spam)**.

The project uses **TF-IDF** for text feature extraction and **Multinomial Naive Bayes** for classification.

## Features

- Detect Spam Messages
- Classify Normal Messages
- Machine Learning Model
- TF-IDF Text Vectorization
- Model Accuracy
- Test Custom Messages
- CSV Dataset

## Requirements

Install the required libraries:

```bash
pip install pandas scikit-learn
```

## Run the Project

Make sure these files are in the same folder:

```text
Spam-Detection/
│
├── spam_detection.py
├── spam_dataset.csv
└── README.md
```

Run:

```bash
python Spam_Detection.py
```

## How It Works

The system follows these steps:

```text
CSV Dataset
     ↓
Clean Text
     ↓
Train/Test Split
     ↓
TF-IDF Vectorization
     ↓
Naive Bayes Model
     ↓
Train Model
     ↓
Predict Message
     ↓
Spam / Not Spam
```

## Machine Learning Pipeline

### 1. Dataset

The dataset contains two columns:

```text
label,message
```

Example:

```text
spam,"Congratulations! You won a prize!"
ham,"Are we meeting today?"
```

### 2. TF-IDF

TF-IDF converts text into numerical features that the machine learning model can understand.

### 3. Naive Bayes

The project uses **Multinomial Naive Bayes**, a commonly used algorithm for text classification.

### 4. Prediction

The trained model analyzes a new message and predicts:

```text
spam
```

or

```text
ham
```

## Modules Used

- Python 3
- Pandas
- Scikit-learn
- TF-IDF
- Multinomial Naive Bayes

## What i learned

- Machine Learning
- Natural Language Processing
- Text Classification
- TF-IDF
- Naive Bayes
- Train/Test Split
- Model Evaluation
- CSV Data Processing
- Functions

> **Note:** This is an educational project. A production spam filter would require a much larger and more diverse dataset.

---

⭐ Part of my **#50DaysOfPython** challenge.
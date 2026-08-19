# Sentiment Analysis

A simple **Sentiment Analysis** application built with Python that analyzes text and determines whether the sentiment is **Positive, Negative, or Neutral**.

The project uses **VADER (Valence Aware Dictionary and sEntiment Reasoner)** for natural language processing.

## Features

- Positive sentiment detection
- Negative sentiment detection
- Neutral sentiment detection
- Sentiment scores
- Compound sentiment score
- Analyze custom text
-  Analyze multiple messages

## Requirements

Install VADER:

```bash
python -m pip install vaderSentiment
```

## Run the Project

```bash
python Sentiment_Analysis.py
```

Enter any sentence when prompted:

```text
Enter text: I really enjoyed this movie!

Sentiment : Positive 😊
```

Type:

```text
exit
```

to close the application.

## How It Works

```text
User Text
    ↓
VADER Sentiment Analyzer
    ↓
Token & Context Analysis
    ↓
Sentiment Scores
    ↓
Compound Score
    ↓
Positive / Negative / Neutral
```

## Sentiment Scores

VADER provides four main scores:

```text
Positive → pos
Negative → neg
Neutral  → neu
Compound → compound
```

The **compound score** ranges from:

```text
-1 → Very Negative
 0 → Neutral
+1 → Very Positive
```

The program uses these thresholds:

```text
Compound >= 0.05  → Positive

Compound <= -0.05 → Negative

Otherwise          → Neutral
```

## Modules Used

- Python 3
- VADER
- Natural Language Processing

## What i learned

- Natural Language Processing
- Sentiment Analysis
- Text Processing
- Dictionaries
- Functions
- Conditional Statements
- Loops
- User Input
- Score Interpretation

> **Note:** VADER is a rule-based sentiment analyzer and is not a custom-trained machine learning model.

---

⭐ Part of my **#50DaysOfPython** challenge.

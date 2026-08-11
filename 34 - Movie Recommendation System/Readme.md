# Movie Recommendation System

A simple **Movie Recommendation System** built with Python that recommends movies based on the similarity of their descriptions.

The project uses **TF-IDF** and **Cosine Similarity** to compare movies and generate recommendations.

## Features

- Search for a movie
- Content-based recommendations
- TF-IDF text processing
- Cosine similarity
- Top 5 similar movies
- CSV-based movie dataset
- Input validation

## Requirements

Install the required libraries:

```bash
pip install pandas scikit-learn
```

## Run the Project

Make sure these files are in the same directory:

```text
Movie-Recommendation-System/
│
├── movie_recommendation.py
├── movies.csv
└── README.md
```

Run:

```bash
python Movie_Recommendation_System.py
```

## How It Works

1. The program loads movie information from `movies.csv`.
2. Movie descriptions are converted into numerical vectors using **TF-IDF**.
3. The program calculates similarity between every movie using **Cosine Similarity**.
4. Enter a movie title.
5. The system finds movies with the highest similarity scores.
6. The top 5 recommendations are displayed.

## Example

```text
Enter Movie Name: Interstellar

MOVIES SIMILAR TO INTERSTELLAR

1. The Martian
2. Gravity
3. ...
```

## Modules Used

- Python 3
- Pandas
- Scikit-learn
- TF-IDF
- Cosine Similarity

## What i learned

- Data Processing
- CSV File Handling
- Pandas DataFrames
- Natural Language Processing
- TF-IDF
- Cosine Similarity
- Machine Learning
- Functions
- Loops

> **Note:** This is a basic educational recommendation system. Recommendations are based only on the movie descriptions provided in the dataset.

---

⭐ Part of my **#50DaysOfPython** challenge.
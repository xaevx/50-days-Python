import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def load_movies(filename):

    try:
        movies = pd.read_csv(filename)

        if "title" not in movies.columns or "description" not in movies.columns:
            print("CSV must contain 'title' and 'description' columns.")
            return None

        return movies

    except FileNotFoundError:
        print("Movie file not found.")
        return None

    except Exception as error:
        print("Error:", error)
        return None


def create_recommendations(movies):

    movies["description"] = movies["description"].fillna("")

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(movies["description"])

    similarity_matrix = cosine_similarity(tfidf_matrix)

    return similarity_matrix


def recommend(movie_name, movies, similarity_matrix):

    matches = movies[
        movies["title"].str.lower() == movie_name.lower()
    ]

    if matches.empty:
        print("\nMovie not found.")
        return

    movie_index = matches.index[0]

    similarity_scores = list(
        enumerate(similarity_matrix[movie_index])
    )

    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    print("\n" + "=" * 50)
    print(f"     MOVIES SIMILAR TO {movies.loc[movie_index, 'title'].upper()}")
    print("=" * 50)

    count = 0

    for index, score in similarity_scores:

        if index == movie_index:
            continue

        print(
            f"\n{count + 1}. {movies.iloc[index]['title']}"
        )

        print(
            f"   Similarity Score: {score:.2f}"
        )

        count += 1

        if count == 5:
            break

movies = load_movies("movies.csv")

if movies is not None:

    similarity_matrix = create_recommendations(movies)

    while True:

        print("\n" + "=" * 40)
        print("     MOVIE RECOMMENDATION SYSTEM")
        print("=" * 40)

        movie_name = input(
            "Enter Movie Name (or 'exit'): "
        ).strip()

        if movie_name.lower() == "exit":
            print("Goodbye!")
            break

        recommend(
            movie_name,
            movies,
            similarity_matrix
        )
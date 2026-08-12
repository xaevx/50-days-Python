import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


def load_data(filename):

    try:
        data = pd.read_csv(filename)

        if "message" not in data.columns or "label" not in data.columns:
            print("CSV must contain 'message' and 'label' columns.")
            return None

        return data

    except FileNotFoundError:
        print("Dataset file not found.")
        return None

    except Exception as error:
        print("Error:", error)
        return None


def train_model(data):

    messages = data["message"]
    labels = data["label"]

    X_train, X_test, y_train, y_test = train_test_split(
        messages,
        labels,
        test_size=0.2,
        random_state=42
    )

    vectorizer = TfidfVectorizer(
        lowercase=True,
        stop_words="english"
    )

    X_train = vectorizer.fit_transform(X_train)
    X_test = vectorizer.transform(X_test)

    model = MultinomialNB()

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

    return model, vectorizer


def check_message(model, vectorizer):

    message = input("\nEnter a message to check: ").strip()

    if not message:
        print("Message cannot be empty.")
        return

    message_vector = vectorizer.transform([message])

    prediction = model.predict(message_vector)[0]

    print("\n" + "=" * 40)

    if prediction == "spam":
        print("This is a SPAM MESSAGE.")
    else:
        print("This is NOT a SPAM MESSAGE.")

    print("=" * 40)


data = load_data("Spam_Dataset.csv")

if data is not None:

    model, vectorizer = train_model(data)

    while True:

        print("\n" + "=" * 40)
        print("        SPAM DETECTION")
        print("=" * 40)

        print("1. Check Message")
        print("0. Exit")

        choice = input("\nSelect Option: ").strip()

        if choice == "1":
            check_message(model, vectorizer)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")
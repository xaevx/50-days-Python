from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):

    scores = analyzer.polarity_scores(text)

    compound = scores["compound"]

    if compound >= 0.05:
        sentiment = "Positive 😊"

    elif compound <= -0.05:
        sentiment = "Negative 😞"

    else:
        sentiment = "Neutral 😐"

    print("\n" + "=" * 45)
    print("         SENTIMENT ANALYSIS")
    print("=" * 45)

    print(f"\nText      : {text}")
    print(f"Positive  : {scores['pos']:.2f}")
    print(f"Negative  : {scores['neg']:.2f}")
    print(f"Neutral   : {scores['neu']:.2f}")
    print(f"Compound  : {compound:.2f}")
    print(f"\nSentiment : {sentiment}")

while True:

    print("\n" + "=" * 40)
    print("       SENTIMENT ANALYZER")
    print("=" * 40)

    text = input(
        "Enter text (or 'exit'): "
    ).strip()

    if text.lower() == "exit":
        print("Goodbye!")
        break

    if not text:
        print("Please enter some text.")
        continue

    analyze_sentiment(text)
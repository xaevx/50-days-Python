import requests

API_KEY = "Your_API_Key"  # Get your API key from https://newsapi.org/
BASE_URL = "https://newsapi.org/v2/top-headlines"


def fetch_news(country):

    params = {
        "country": country,
        "apiKey": API_KEY
    }

    try:

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data["status"] != "ok":
            print("\nUnable to fetch the news.")
            return

        articles = data["articles"]

        if not articles:
            print("\nNo news found.")
            return

        print("\n" + "=" * 50)
        print("         TOP HEADLINES")
        print("=" * 50)

        for index, article in enumerate(articles[:10], start=1):

            print(f"\n{index}. {article['title']}")

            if article["source"]["name"]:
                print(f"Source : {article['source']['name']}")

            if article["publishedAt"]:
                print(f"Published : {article['publishedAt'][:10]}")

            print("-" * 50)

    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")

    except Exception as error:
        print("Error:", error)


while True:

    print("\n" + "=" * 40)
    print("         NEWS FETCHER")
    print("=" * 40)

    country = input("Enter your Country Code (e.g. us, in, gb) or 'exit': ").lower()

    if country == "exit":
        print("Goodbye!")
        break

    fetch_news(country)
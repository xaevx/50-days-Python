import requests
from bs4 import BeautifulSoup


def scrape_website(url):

    try:

        response = requests.get(url)

        if response.status_code != 200:
            print("Failed to access the website.")
            return

        soup = BeautifulSoup(response.text, "html.parser")

        print("\n" + "=" * 50)
        print("          WEB SCRAPER")
        print("=" * 50)

        print(f"\nPage Title : {soup.title.string}")

        print("\nHeadings:\n")

        headings = soup.find_all(["h1", "h2", "h3"])

        if headings:

            for index, heading in enumerate(headings, start=1):
                print(f"{index}. {heading.get_text(strip=True)}")

        else:
            print("No headings found.")

    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")

    except requests.exceptions.MissingSchema:
        print("Please enter a valid URL (include https://).")

    except Exception as error:
        print("Error:", error)


while True:

    print("\n" + "=" * 45)
    print("          WEB SCRAPER")
    print("=" * 45)

    url = input("Enter Website URL (or 'exit'): ").strip()

    if url.lower() == "exit":
        print("Goodbye!")
        break

    scrape_website(url)
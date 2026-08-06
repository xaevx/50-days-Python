import requests

BASE_URL = "https://api.github.com/users/"


def view_profile(username):

    try:

        response = requests.get(BASE_URL + username)

        if response.status_code == 404:
            print("\n❌ User not found.")
            return

        data = response.json()

        print("\n" + "=" * 50)
        print("        GITHUB PROFILE")
        print("=" * 50)

        print(f"◻ Name           : {data.get('name')}")
        print(f"◻ Username       : {data.get('login')}")
        print(f"◻ Bio            : {data.get('bio')}")
        print(f"◻ Location       : {data.get('location')}")
        print(f"◻ Company        : {data.get('company')}")
        print(f"◻ Public Repos   : {data.get('public_repos')}")
        print(f"◻ Followers      : {data.get('followers')}")
        print(f"◻ Following      : {data.get('following')}")
        print(f"◻ Profile URL    : {data.get('html_url')}")
        print(f"◻ Created On     : {data.get('created_at')[:10]}")

    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")

    except Exception as error:
        print("Error:", error)


while True:

    print("\n" + "=" * 45)
    print("      GITHUB PROFILE VIEWER")
    print("=" * 45)

    username = input("Enter GitHub Username (or 'exit'): ").strip()

    if username.lower() == "exit":
        print("Goodbye!")
        break

    view_profile(username)
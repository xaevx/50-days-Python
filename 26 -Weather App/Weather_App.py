import requests

API_KEY = "Your_API_Key" # Generate API from https://www.weatherapi.com/
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city):

    params = {
        "key": API_KEY,
        "q": city
    }

    try:

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            print("\n❌", data["error"]["message"])
            return

        location = data["location"]
        current = data["current"]

        print("\n" + "=" * 45)
        print(f"      WEATHER IN {location['name'].upper()}")
        print("=" * 45)

        print(f"Country      : {location['country']}")
        print(f"Temperature  : {current['temp_c']} °C")
        print(f"Feels Like   : {current['feelslike_c']} °C")
        print(f"Humidity     : {current['humidity']}%")
        print(f"Wind Speed   : {current['wind_kph']} km/h")
        print(f"Condition     : {current['condition']['text']}")

    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")

    except Exception as error:
        print("Error:", error)


while True:

    print("\n" + "=" * 45)
    print("          WEATHER APP")
    print("=" * 45)

    city = input("Enter City Name (or 'exit'): ").strip()

    if city.lower() == "exit":
        print("Goodbye!")
        break

    get_weather(city)
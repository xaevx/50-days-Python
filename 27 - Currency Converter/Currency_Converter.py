import requests

BASE_URL = "https://open.er-api.com/v6/latest/"


def convert_currency(from_currency, to_currency, amount):

    try:

        response = requests.get(BASE_URL + from_currency.upper())
        data = response.json()

        if data["result"] != "success":
            print("Invalid currency code.")
            return

        rates = data["rates"]

        if to_currency.upper() not in rates:
            print("Target currency not found.")
            return

        converted = amount * rates[to_currency.upper()]

        print("\n" + "=" * 45)
        print("       CURRENCY CONVERTER")
        print("=" * 45)
        print(f"{amount:.2f} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")

    except requests.exceptions.ConnectionError:
        print("No Internet Connection.")

    except Exception as error:
        print("Error:", error)


while True:

    print("\n" + "=" * 40)
    print("      CURRENCY CONVERTER")
    print("=" * 40)

    from_currency = input("From Currency (e.g. USD): ").strip()

    if from_currency.lower() == "exit":
        print("Goodbye!")
        break

    to_currency = input("To Currency (e.g. INR): ").strip()

    try:

        amount = float(input("Amount: "))

        if amount <= 0:
            print("Amount must be greater than zero.")
            continue

        convert_currency(from_currency, to_currency, amount)

    except ValueError:
        print("Please enter a valid amount.")
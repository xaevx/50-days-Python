# pyrefly: ignore [missing-import]
import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_data(ticker, period):

    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period=period)

        if data.empty:
            print("No stock data found.")
            return None

        return data

    except Exception as error:
        print("Error:", error)
        return None

def analyze_stock(data, ticker):

    current_price = data["Close"].iloc[-1]
    highest_price = data["High"].max()
    lowest_price = data["Low"].min()

    first_price = data["Close"].iloc[0]

    change = current_price - first_price
    percentage_change = (change / first_price) * 100

    print("\n" + "=" * 50)
    print(f"       STOCK PRICE ANALYZER - {ticker.upper()}")
    print("=" * 50)

    print(f"\nCurrent Price : ${current_price:.2f}")
    print(f"Highest Price : ${highest_price:.2f}")
    print(f"Lowest Price  : ${lowest_price:.2f}")

    print(f"\nPrice Change  : ${change:.2f}")
    print(f"Change        : {percentage_change:.2f}%")

    if percentage_change > 0:
        print("Trend         : 📈 Positive")
    elif percentage_change < 0:
        print("Trend         : 📉 Negative")
    else:
        print("Trend         : ➡️ Neutral")


def show_chart(data, ticker):

    plt.figure(figsize=(10, 6))

    plt.plot(data.index, data["Close"])

    plt.title(f"{ticker.upper()} Stock Price")
    plt.xlabel("Date")
    plt.ylabel("Price")

    plt.grid(True)
    plt.tight_layout()
    plt.show()

while True:

    print("\n" + "=" * 45)
    print("         STOCK PRICE ANALYZER")
    print("=" * 45)

    ticker = input("Enter Stock Ticker (or 'exit'): ").strip()

    if ticker.lower() == "exit":
        print("Goodbye!")
        break

    print("\nSelect Period:")
    print("1. 1 Month")
    print("2. 3 Months")
    print("3. 6 Months")
    print("4. 1 Year")
    print("5. 5 Years")

    try:

        choice = int(input("Select Option: "))

        periods = {
            1: "1mo",
            2: "3mo",
            3: "6mo",
            4: "1y",
            5: "5y"
        }

        if choice not in periods:
            print("Invalid option.")
            continue

        data = get_stock_data(ticker, periods[choice])

        if data is not None:
            analyze_stock(data, ticker)
            show_chart(data, ticker)

    except ValueError:
        print("Please enter a valid number.")
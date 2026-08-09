import pandas as pd
import matplotlib.pyplot as plt

def load_data(filename):
    try:
        return pd.read_csv(filename)

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as error:
        print("Error:", error)
        return None

def create_dashboard(data):

    print("\n" + "=" * 50)
    print("        DATA VISUALIZATION DASHBOARD")
    print("=" * 50)

    print(f"\nTotal Records : {len(data)}")
    print(f"Columns         : {len(data.columns)}")

    print("\nAvailable Columns:")
    for column in data.columns:
        print(f"- {column}")

    numeric_columns = data.select_dtypes(include="number").columns

    if len(numeric_columns) == 0:
        print("\nNo numerical columns available for visualization.")
        return

    column = input(
        "\nEnter numerical column to visualize: "
    ).strip()

    if column not in numeric_columns:
        print("Invalid column.")
        return

    print("\nChoose Chart Type:")
    print("1. Bar Chart")
    print("2. Line Chart")
    print("3. Histogram")

    try:
        choice = int(input("Select Option: "))

        plt.figure(figsize=(10, 6))

        if choice == 1:
            data[column].value_counts().plot(kind="bar")
            plt.title(f"{column} - Bar Chart")
            plt.xlabel(column)
            plt.ylabel("Count")

        elif choice == 2:
            data[column].plot(kind="line")
            plt.title(f"{column} - Line Chart")
            plt.xlabel("Record")
            plt.ylabel(column)

        elif choice == 3:
            data[column].plot(kind="hist", bins=10)
            plt.title(f"{column} - Distribution")
            plt.xlabel(column)
            plt.ylabel("Frequency")

        else:
            print("Invalid option.")
            return

        plt.tight_layout()
        plt.show()

    except ValueError:
        print("Please enter a valid option.")

filename = input("Enter CSV file name: ").strip()

data = load_data(filename)

if data is not None:
    create_dashboard(data)
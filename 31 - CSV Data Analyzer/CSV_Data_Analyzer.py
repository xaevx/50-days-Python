import pandas as pd

def load_data(filename):

    try:
        data = pd.read_csv(filename)
        return data

    except FileNotFoundError:
        print("File not found.")
        return None

    except Exception as error:
        print("Error:", error)
        return None

def analyze_data(data):

    print("\n" + "=" * 50)
    print("            CSV DATA ANALYZER")
    print("=" * 50)

    print(f"\nRows    : {data.shape[0]}")
    print(f"Columns : {data.shape[1]}")

    print("\nColumns:")
    for column in data.columns:
        print(f"- {column}")

    print("\nFirst 5 Rows:")
    print(data.head())

    print("\nMissing Values:")
    print(data.isnull().sum())

    numeric_data = data.select_dtypes(include="number")

    if not numeric_data.empty:

        print("\nNumerical Statistics:")
        print(numeric_data.describe())

    else:
        print("\nNo numerical columns found.")

filename = input("Enter CSV file name: ").strip()

data = load_data(filename)

if data is not None:
    analyze_data(data)
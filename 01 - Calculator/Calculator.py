import math

history = []


def calculate(choice, a, b=None):

    if choice == 1:
        return a + b
    elif choice == 2:
        return a - b
    elif choice == 3:
        return a * b
    elif choice == 4:
        return a / b
    elif choice == 5:
        return a ** b
    elif choice == 6:
        return a % b
    elif choice == 7:
        return a // b
    elif choice == 8:
        return math.sqrt(a)
    elif choice == 9:
        return (a / 100) * b

while True:

    print("\n" + "=" * 45)
    print("         SMART PYTHON CALCULATOR")
    print("=" * 45)

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Floor Division")
    print("8. Square Root")
    print("9. Percentage")
    print("10. History")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option : "))

        if choice == 0:
            print("\nGoodbye!")
            break

        elif choice == 10:

            print("\nCalculation History\n")

            if len(history) == 0:
                print("No calculations yet.")

            else:
                for item in history:
                    print(item)

            continue

        elif choice == 8:

            num = float(input("Enter Number : "))

            answer = calculate(choice, num)

            history.append(f"√{num} = {answer}")

            print("Answer :", answer)

        elif choice == 9:

            percent = float(input("Percentage : "))
            number = float(input("Of Number : "))

            answer = calculate(choice, percent, number)

            history.append(f"{percent}% of {number} = {answer}")

            print("Answer :", answer)

        else:

            num1 = float(input("First Number : "))
            num2 = float(input("Second Number : "))

            answer = calculate(choice, num1, num2)

            operations = {
                1: "+",
                2: "-",
                3: "*",
                4: "/",
                5: "^",
                6: "%",
                7: "//"
            }

            history.append(
                f"{num1} {operations[choice]} {num2} = {answer}"
            )

            print("Answer :", answer)

    except ZeroDivisionError:

        print("Cannot divide by zero.")

    except ValueError:

        print("Invalid Input.")

    except Exception as error:

        print("Unexpected Error:", error)
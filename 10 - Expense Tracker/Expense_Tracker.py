expenses = []


def add_expense():

    name = input("Expense Name : ").strip().title()

    try:
        amount = float(input("Amount (₹): "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("✅ Expense added successfully.")

    except ValueError:
        print("Invalid amount.")


def view_expenses():

    if not expenses:
        print("\n📂 No expenses recorded.")
        return

    print("\n========== EXPENSES ==========")

    total = 0

    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} - ₹{expense['amount']:.2f}")
        total += expense["amount"]

    print("-" * 30)
    print(f"Total Expense : ₹{total:.2f}")


def delete_expense():

    view_expenses()

    if not expenses:
        return

    try:
        number = int(input("\nEnter expense number to delete: "))

        if 1 <= number <= len(expenses):
            removed = expenses.pop(number - 1)
            print(f"🗑️ '{removed['name']}' deleted.")
        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\nEXPENSE TRACKER\n")

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. View Total Expense")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option: "))

        if choice == 1:
            add_expense()

        elif choice == 2:
            view_expenses()

        elif choice == 3:
            delete_expense()

        elif choice == 4:

            total = sum(expense["amount"] for expense in expenses)
            print(f"\n💰 Total Expense : ₹{total:.2f}")

        elif choice == 0:
            print("\nGoodbye!")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")
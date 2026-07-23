class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return

        self.balance += amount
        print(f"₹{amount:.2f} deposited successfully.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return

        if amount > self.balance:
            print("Insufficient balance.")
            return

        self.balance -= amount
        print(f"₹{amount:.2f} withdrawn successfully.")

    def check_balance(self):
        print(f"\nCurrent Balance : ₹{self.balance:.2f}")

    def account_details(self):

        print("\n========== ACCOUNT DETAILS ==========")
        print(f"Account Holder : {self.name}")
        print(f"Account Number : {self.account_number}")
        print(f"Balance        : ₹{self.balance:.2f}")


name = input("Enter Account Holder Name: ").strip().title()
account_number = input("Enter Account Number: ").strip()

account = BankAccount(name, account_number)

while True:

    print("\n" + "=" * 45)
    print("      BANK ACCOUNT SIMULATOR")
    print("=" * 45)

    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Account Details")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option: "))

        if choice == 1:

            amount = float(input("Enter Amount: ₹"))
            account.deposit(amount)

        elif choice == 2:

            amount = float(input("Enter Amount: ₹"))
            account.withdraw(amount)

        elif choice == 3:

            account.check_balance()

        elif choice == 4:

            account.account_details()

        elif choice == 0:

            print("\nThank you for using the Bank Account Simulator!")
            break

        else:

            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")
import random
import string

passwords = {}


def generate_password(length=12):

    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def add_password():

    account = input("Account Name : ").strip().title()

    if not account:
        print("Account name cannot be empty")
        return

    choice = input("Generate Password? (y/n): ").lower()

    if choice == "y":
        password = generate_password()
    else:
        password = input("Enter Password : ")

    passwords[account] = password

    print("Password saved successfully.")


def view_accounts():

    if not passwords:
        print("\nNo saved accounts.")
        return

    print("\n========== SAVED PASSWORDS ==========")

    for account, password in passwords.items():
        print(f"{account} : {password}")


def search_password():

    account = input("Enter Account Name : ").strip().title()

    if account in passwords:
        print(f"\nPassword : {passwords[account]}")
    else:
        print("Account not found.")


def delete_password():

    account = input("Enter Account Name : ").strip().title()

    if account in passwords:
        del passwords[account]
        print("Password deleted.")
    else:
        print("Account not found.")


while True:

    print("\n" + "=" * 40)
    print("      PASSWORD MANAGER")
    print("=" * 40)

    print("1. Add Password")
    print("2. View Passwords")
    print("3. Search Password")
    print("4. Delete Password")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option: "))

        if choice == 1:
            add_password()

        elif choice == 2:
            view_accounts()

        elif choice == 3:
            search_password()

        elif choice == 4:
            delete_password()

        elif choice == 0:
            print("\nGoodbye!")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")
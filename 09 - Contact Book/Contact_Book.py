contacts = {}


def show_contacts():

    if not contacts:
        print("\n📂 No contacts found.")
        return

    print("\n========== CONTACT BOOK ==========")

    for name, phone in contacts.items():
        print(f"Name : {name}")
        print(f"Phone: {phone}")
        print("-" * 25)


while True:

    print("\nCONTACT BOOK\n")

    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option: "))

        if choice == 1:

            name = input("Enter Name: ").strip().title()
            phone = input("Enter Phone Number: ").strip()

            if name and phone:
                contacts[name] = phone
                print("✅ Contact added successfully.")
            else:
                print("Name and phone number cannot be empty.")

        elif choice == 2:

            show_contacts()

        elif choice == 3:

            name = input("Enter Name to Search: ").strip().title()

            if name in contacts:
                print("\nContact Found")
                print(f"Name : {name}")
                print(f"Phone: {contacts[name]}")
            else:
                print("❌ Contact not found.")

        elif choice == 4:

            name = input("Enter Name to Delete: ").strip().title()

            if name in contacts:
                del contacts[name]
                print("🗑️ Contact deleted successfully.")
            else:
                print("❌ Contact not found.")

        elif choice == 0:

            print("\nGoodbye!")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")
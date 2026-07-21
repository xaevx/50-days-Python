books = {}


def add_book():

    title = input("Enter Book Title: ").strip().title()

    if title in books:
        print("Book already exists.")
        return

    author = input("Enter Author Name: ").strip().title()

    books[title] = {
        "author": author,
        "available": True
    }

    print("Book added successfully.")


def view_books():

    if not books:
        print("\nNo books available.")
        return

    print("\n========== LIBRARY ==========")

    for title, details in books.items():

        status = "Available" if details["available"] else "Issued"

        print(f"\nTitle  : {title}")
        print(f"Author : {details['author']}")
        print(f"Status : {status}")


def issue_book():

    title = input("Enter Book Title: ").strip().title()

    if title not in books:
        print("Book not found.")
        return

    if books[title]["available"]:
        books[title]["available"] = False
        print("Book issued successfully.")
    else:
        print("Book is already issued.")


def return_book():

    title = input("Enter Book Title: ").strip().title()

    if title not in books:
        print("Book not found.")
        return

    if not books[title]["available"]:
        books[title]["available"] = True
        print("Book returned successfully.")
    else:
        print("Book is already available.")


def remove_book():

    title = input("Enter Book Title: ").strip().title()

    if title in books:
        del books[title]
        print("Book removed successfully.")
    else:
        print("Book not found.")


while True:

    print("\n" + "=" * 45)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Remove Book")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option: "))

        if choice == 1:
            add_book()

        elif choice == 2:
            view_books()

        elif choice == 3:
            issue_book()

        elif choice == 4:
            return_book()

        elif choice == 5:
            remove_book()

        elif choice == 0:
            print("\nGoodbye!")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")
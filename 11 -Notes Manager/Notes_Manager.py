notes = []


def add_note():

    note = input("Enter Note: ").strip()

    if note:
        notes.append(note)
        print("✅ Note added successfully.")
    else:
        print("Note cannot be empty.")


def view_notes():

    if not notes:
        print("\n❌ No notes available.")
        return

    print("\nMy Notes\n")

    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")


def delete_note():

    view_notes()

    if not notes:
        return

    try:
        number = int(input("\nEnter note number to delete: "))

        if 1 <= number <= len(notes):
            removed = notes.pop(number - 1)
            print(f"🗑️ '{removed}' deleted successfully.")
        else:
            print("Invalid note number.")

    except ValueError:
        print("Please enter a valid number.")


while True:

    print("\n" + "=" * 40)
    print("         NOTES MANAGER")
    print("=" * 40)

    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Clear All Notes")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option: "))

        if choice == 1:
            add_note()

        elif choice == 2:
            view_notes()

        elif choice == 3:
            delete_note()

        elif choice == 4:

            notes.clear()
            print("🧹 All notes cleared.")

        elif choice == 0:

            print("\nGoodbye!")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")
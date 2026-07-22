students = {}


def add_student():

    roll_no = input("Enter Roll Number: ").strip()

    if roll_no in students:
        print("Student already exists.")
        return

    name = input("Enter Student Name: ").strip().title()
    department = input("Enter Department: ").strip().upper()

    try:
        marks = float(input("Enter Marks: "))

        students[roll_no] = {
            "name": name,
            "department": department,
            "marks": marks
        }

        print("Student added successfully.")

    except ValueError:
        print("Invalid marks.")


def view_students():

    if not students:
        print("\nNo student records found.")
        return

    print("\n========== STUDENT RECORDS ==========")

    for roll_no, details in students.items():

        print(f"\nRoll No    : {roll_no}")
        print(f"Name       : {details['name']}")
        print(f"Department : {details['department']}")
        print(f"Marks      : {details['marks']}")


def search_student():

    roll_no = input("Enter Roll Number: ").strip()

    if roll_no in students:

        student = students[roll_no]

        print("\nStudent Found")
        print(f"Roll No    : {roll_no}")
        print(f"Name       : {student['name']}")
        print(f"Department : {student['department']}")
        print(f"Marks      : {student['marks']}")

    else:
        print("Student not found.")


def update_marks():

    roll_no = input("Enter Roll Number: ").strip()

    if roll_no not in students:
        print("Student not found.")
        return

    try:
        marks = float(input("Enter New Marks: "))
        students[roll_no]["marks"] = marks
        print("Marks updated successfully.")

    except ValueError:
        print("Invalid marks.")


def delete_student():

    roll_no = input("Enter Roll Number: ").strip()

    if roll_no in students:
        del students[roll_no]
        print("Student record deleted.")
    else:
        print("Student not found.")


while True:

    print("\n" + "=" * 45)
    print("     STUDENT MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("0. Exit")

    try:

        choice = int(input("\nSelect Option: "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            search_student()

        elif choice == 4:
            update_marks()

        elif choice == 5:
            delete_student()

        elif choice == 0:
            print("\nGoodbye!")
            break

        else:
            print("Invalid option.")

    except ValueError:
        print("Please enter a valid number.")
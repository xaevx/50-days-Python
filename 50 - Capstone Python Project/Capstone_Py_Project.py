import os
import sqlite3
from datetime import datetime

try:
    from groq import Groq
except ImportError:
    Groq = None

DATABASE = "capstone.db"

GROQ_MODEL = os.environ.get("GROQ_MODEL", "openai/gpt-oss-20b")

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

def connect_database():
    return sqlite3.connect(DATABASE)

def create_database():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT,
            email TEXT
        )
    """)

    connection.commit()
    connection.close()

def add_task():
    title = input("Task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tasks
        (title, completed, created_at)
        VALUES (?, ?, ?)
    """, (
        title,
        0,
        datetime.now().isoformat()
    ))

    connection.commit()
    connection.close()

    print("Task added successfully.")

def list_tasks():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, completed, created_at
        FROM tasks
        ORDER BY id DESC
    """)

    tasks = cursor.fetchall()
    connection.close()

    if not tasks:
        print("No tasks found.")
        return

    print("\nTASKS")
    print("-" * 50)

    for task in tasks:
        task_id, title, completed, created_at = task
        status = "✓" if completed else " "

        print(f"{task_id}. [{status}] {title}")

def complete_task():
    list_tasks()

    try:
        task_id = int(input("\nTask ID to complete: "))

    except ValueError:
        print("Invalid task ID.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tasks
        SET completed = 1
        WHERE id = ?
    """, (task_id,))

    connection.commit()

    if cursor.rowcount == 0:
        print("Task not found.")

    else:
        print("Task marked as completed.")

    connection.close()

def add_note():
    title = input("Note title: ").strip()

    if not title:
        print("Title cannot be empty.")
        return

    content = input("Note content: ").strip()

    if not content:
        print("Note cannot be empty.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO notes
        (title, content, created_at)
        VALUES (?, ?, ?)
    """, (
        title,
        content,
        datetime.now().isoformat()
    ))

    connection.commit()
    connection.close()

    print("Note saved successfully.")

def list_notes():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, title, content, created_at
        FROM notes
        ORDER BY id DESC
    """)

    notes = cursor.fetchall()
    connection.close()

    if not notes:
        print("No notes found.")
        return

    print("\nNOTES")
    print("-" * 50)

    for note in notes:
        note_id, title, content, created_at = note

        print(f"\n{note_id}. {title}")

        print(content)

        print(f"Created: {created_at}")

def add_expense():
    category = input("Category: ").strip()

    try:
        amount = float(input("Amount: "))

    except ValueError:
        print("Please enter a valid amount.")
        return

    description = input("Description: ").strip()

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO expenses
        (category, amount, description, created_at)
        VALUES (?, ?, ?, ?)
    """, (
        category,
        amount,
        description,
        datetime.now().isoformat()
    ))

    connection.commit()
    connection.close()

    print("Expense added successfully.")

def expense_summary():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            COUNT(*),
            COALESCE(SUM(amount), 0)
        FROM expenses
    """)

    count, total = cursor.fetchone()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
        ORDER BY SUM(amount) DESC
    """)

    categories = cursor.fetchall()
    connection.close()

    print("\nEXPENSE SUMMARY")
    print("-" * 50)

    print(f"Transactions: {count}")

    print(f"Total Spent: ₹{total:,.2f}")

    if categories:
        print("\nBy Category:")

        for category, amount in categories:
            print(f"{category}: ₹{amount:,.2f}")

def add_contact():
    name = input("Name: ").strip()

    phone = input("Phone: ").strip()

    email = input("Email: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO contacts
        (name, phone, email)
        VALUES (?, ?, ?)
    """, (
        name,
        phone,
        email
    ))

    connection.commit()
    connection.close()

    print("Contact added successfully.")

def list_contacts():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, phone, email
        FROM contacts
        ORDER BY name
    """)

    contacts = cursor.fetchall()
    connection.close()

    if not contacts:
        print("No contacts found.")
        return

    print("\nCONTACTS")
    print("-" * 50)

    for contact in contacts:
        contact_id, name, phone, email = contact

        print(f"{contact_id}. {name}")

        print(f"   Phone: {phone}")

        print(f"   Email: {email}")

def ask_ai():
    if Groq is None:
        print("Groq package is not installed.")

        print("Install it using:")

        print("python -m pip install groq")

        return

    if not GROQ_API_KEY:
        print("GROQ_API_KEY was not found.")

        print("Set your API key before using the AI assistant.")

        return

    user_input = input("\nAsk the AI: ").strip()

    if not user_input:
        return

    try:
        client = Groq(
            api_key=GROQ_API_KEY
        )

        response = client.chat.completions.create(
            model=GROQ_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful personal AI assistant. "
                        "Give clear and concise answers."
                    )
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.7,
            max_tokens=500
        )

        answer = (
            response
            .choices[0]
            .message
            .content
        )

        print(f"\nAI: {answer}")

    except Exception as error:
        print(f"\nAI Error: {error}")

def dashboard():
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM tasks")

    total_tasks = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM tasks WHERE completed = 1")

    completed_tasks = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM notes")

    total_notes = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM contacts")

    total_contacts = cursor.fetchone()[0]

    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM expenses")

    total_expenses = cursor.fetchone()[0]

    connection.close()

    pending_tasks = (
        total_tasks - completed_tasks
    )

    print("\n")
    print("=" * 55)
    print("                  DASHBOARD")
    print("=" * 55)

    print(f"Total Tasks       : {total_tasks}")

    print(f"Completed Tasks   : {completed_tasks}")

    print(f"Pending Tasks     : {pending_tasks}")

    print(f"Total Notes       : {total_notes}")

    print(f"Total Contacts    : {total_contacts}")

    print(f"Total Expenses    : ₹{total_expenses:,.2f}")

def main():
    create_database()

    while True:
        print("\n")
        print("=" * 55)
        print("            PYTHON CAPSTONE PROJECT")
        print("=" * 55)

        print("""
1. Dashboard

2. Add Task
3. View Tasks
4. Complete Task

5. Add Note
6. View Notes

7. Add Expense
8. Expense Summary

9. Add Contact
10. View Contacts

11. Ask AI Assistant

0. Exit
""")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            dashboard()

        elif choice == "2":
            add_task()

        elif choice == "3":
            list_tasks()

        elif choice == "4":
            complete_task()

        elif choice == "5":
            add_note()

        elif choice == "6":
            list_notes()

        elif choice == "7":
            add_expense()

        elif choice == "8":
            expense_summary()

        elif choice == "9":
            add_contact()

        elif choice == "10":
            list_contacts()

        elif choice == "11":
            ask_ai()

        elif choice == "0":
            print("\nThank you for using the Capstone Project!")

            break

        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
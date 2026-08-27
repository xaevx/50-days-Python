# Capstone Python Project

A complete **Personal Productivity & AI Assistant** built with Python as the final project of the **50 Days of Python** challenge.

The application combines multiple concepts learned throughout the challenge into a single command-line application.

It includes task management, notes, expense tracking, contacts, an AI assistant, SQLite database storage, and a personal dashboard.

## Features

- Personal dashboard
- Task management
- Add tasks
- View tasks
- Complete tasks
- Notes manager
- Add notes
- View notes
- Expense tracker
- Expense summaries
- Category-based expense analysis
- Contact book
- Add contacts
- View contacts
- AI assistant
- Persistent SQLite database
- Error handling
- Menu-driven CLI
- Modular Python functions

## Requirements

Python 3.10 or newer is recommended.

Install the Groq Python SDK:

```bash
python -m pip install groq
```

SQLite is included with Python, so it does not need to be installed separately.

## AI API Setup

The AI Assistant uses the Groq API.

Set your API key as an environment variable.

### Windows PowerShell

```powershell
$env:GROQ_API_KEY="YOUR_GROQ_API_KEY"
```

The project uses:

```text
openai/gpt-oss-20b
```

by default.

You can change the model with:

```powershell
$env:GROQ_MODEL="openai/gpt-oss-120b"
```

Verify the API key:

```powershell
python -c "import os; print(bool(os.getenv('GROQ_API_KEY')))"
```

Expected output:

```text
True
```

## Security

Never put your API key directly inside the Python source code.

Do not use:

```python
GROQ_API_KEY = "your-secret-key"
```

Use:

```python
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
```

Never upload your API key to GitHub.

If an API key is accidentally exposed, revoke or regenerate it immediately.

## Run the Project

Run:

```bash
python Capstone_Py_Project.py
```

The `capstone.db` file is automatically generated when the program runs.

## Modules Used

- Python 3
- SQLite3
- Groq
- os
- datetime

## Concepts

This project combines many concepts from the previous projects.

### Core Python

- Variables
- Data types
- Strings
- Lists
- Dictionaries
- Functions
- Loops
- Conditional statements
- Exception handling

### Intermediate Python

- Modules
- Imports
- Environment variables
- Database operations
- SQL queries
- CRUD operations
- Modular functions

### Advanced Concepts

- API integration
- AI API integration
- Persistent storage
- Application architecture
- Data aggregation
- Environment-based configuration

## CRUD Operations

The application demonstrates CRUD concepts.

```text
CREATE
  ↓
Add Tasks
Add Notes
Add Expenses
Add Contacts

READ
  ↓
View Tasks
View Notes
View Expenses
View Contacts

UPDATE
  ↓
Complete Tasks

DELETE
  ↓
Can be implemented as a future improvement
```

## What I Learned

- Building complete Python applications
- Project structure
- Modular programming
- SQLite
- SQL
- CRUD operations
- Data persistence
- API integration
- AI integration
- Environment variables
- Error handling
- User input validation
- Application architecture
- Database design
- Command-line interfaces
- Combining multiple Python concepts

## From CLI to Full Application

The project demonstrates how small Python programs can gradually become larger systems.

```text
Python Fundamentals
        ↓
CLI Applications
        ↓
File & Data Management
        ↓
Databases
        ↓
APIs
        ↓
AI
        ↓
Automation
        ↓
Full Application
```

## Learning Goal

The purpose of the capstone is not to create the biggest possible application.

The goal is to demonstrate that the concepts learned throughout the 50-day challenge can be combined into one working system.

```text
Python
   +
SQLite
   +
SQL
   +
APIs
   +
AI
   +
Application Logic
   +
Data Management
   =
Capstone Project
```

## Project Status

**Status:** Completed

**Difficulty:** Advanced

**Category:** Python / AI / Database / Automation / Application Development

---

⭐ Part of my **#50DaysOfPython** challenge.

## Final Milestone

**50 Days. 50 Projects. 1 Capstone.**

From basic Python syntax to APIs, databases, computer vision, AI, automation, and application development.

The real project was learning how to build things instead of merely reading about them.



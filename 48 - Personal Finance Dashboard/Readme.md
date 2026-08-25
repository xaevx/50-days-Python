# Personal Finance Dashboard

A full-featured **Personal Finance Dashboard** built with Python that allows users to track income, expenses, savings, and spending habits through an interactive web interface.

The project uses **Streamlit** for the dashboard, **SQLite** for persistent data storage, **Pandas** for data analysis, and **Plotly** for data visualization.

## Features

- Add income transactions
- Add expense transactions
- Categorize transactions
- Store transactions permanently
- Calculate total income
- Calculate total expenses
- Calculate current balance
- Calculate savings rate
- View transaction history
- Delete transactions
- Filter and analyze spending data
- Expense category visualization
- Income vs expense visualization
- Interactive dashboard
- SQLite database
- Interactive charts

## Requirements

Install the required packages:

```bash
python -m pip install streamlit pandas plotly
```

SQLite is included with Python, so no additional installation is required for the database.

## Run the Project

Run the Streamlit application:

```bash
streamlit run Personal_Finance_Dashboard.py #Not "python Personal_Finance_Dashboard.py"
```

The dashboard will open in your browser.

If it does not open automatically, Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

## Database

The project uses **SQLite** to store transactions.

The database file is automatically created:

```text
finance.db
```

The database contains a `transactions` table.

## Modules Used

- Python 3
- Streamlit
- Pandas
- Plotly
- SQLite

## What i learned

- Building web applications with Python
- Streamlit
- SQLite databases
- CRUD operations
- Data persistence
- Pandas DataFrames
- Data aggregation
- Financial calculations
- Data visualization
- Plotly
- Interactive dashboards
- Database queries
- User input handling

---

⭐ Part of my **#50DaysOfPython** challenge.
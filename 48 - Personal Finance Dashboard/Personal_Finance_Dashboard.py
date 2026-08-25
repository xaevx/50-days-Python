import sqlite3
from datetime import date

import pandas as pd
import plotly.express as px
import streamlit as st

DATABASE = "finance.db"

def create_database():

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transaction_date TEXT NOT NULL,
            transaction_type TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    """)

    connection.commit()
    connection.close()

def add_transaction(transaction_date, transaction_type, category, amount, description):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO transactions
        (
            transaction_date,
            transaction_type,
            category,
            amount,
            description
        )
        VALUES (?, ?, ?, ?, ?)
    """, (transaction_date,transaction_type,category,amount,description))

    connection.commit()
    connection.close()

def get_transactions():

    connection = sqlite3.connect(DATABASE)

    query = """
        SELECT
            id,
            transaction_date,
            transaction_type,
            category,
            amount,
            description
        FROM transactions
        ORDER BY transaction_date DESC, id DESC
    """
    dataframe = pd.read_sql_query(query,connection)

    connection.close()

    return dataframe

def delete_transaction(transaction_id):

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("DELETE FROM transactions WHERE id = ?",(transaction_id,))

    connection.commit()
    connection.close()

st.set_page_config(
    page_title="Personal Finance Dashboard",
    page_icon="💰",
    layout="wide"
)

create_database()

st.title("💰 Personal Finance Dashboard")

st.write("Track your income, expenses, savings, and spending habits.")

dataframe = get_transactions()

st.sidebar.header("Add Transaction")

with st.sidebar.form("transaction_form"):

    transaction_type = st.selectbox("Type", ["Income", "Expense"])

    transaction_date = st.date_input("Date", value=date.today())

    category = st.selectbox("Category", [
            "Salary",
            "Food",
            "Transport",
            "Shopping",
            "Bills",
            "Entertainment",
            "Education",
            "Health",
            "Investment",
            "Other"
        ]
    )

    amount = st.number_input(
        "Amount", min_value=0.01, step=100.0)

    description = st.text_input("Description")
    submitted = st.form_submit_button("Add Transaction")

    if submitted:

        add_transaction(
            str(transaction_date),
            transaction_type,
            category,
            amount,
            description
        )

        st.success("Transaction added successfully!")

        st.rerun()

if dataframe.empty:

    st.info(
        "No transactions available. "
        "Add your first transaction from the sidebar."
    )

    st.stop()

total_income = dataframe.loc[dataframe["transaction_type"] == "Income", "amount"].sum()

total_expenses = dataframe.loc[dataframe["transaction_type"] == "Expense", "amount"].sum()

balance = total_income - total_expenses

savings_rate = ((balance / total_income) * 100
    if total_income > 0
    else 0
)

column1, column2, column3, column4 = st.columns(4)

column1.metric("Total Income",f"₹{total_income:,.2f}")
column2.metric("Total Expenses", f"₹{total_expenses:,.2f}")
column3.metric("Balance", f"₹{balance:,.2f}")

column4.metric("Savings Rate",f"{savings_rate:.2f}%")

st.divider()

expense_data = dataframe[dataframe["transaction_type"] == "Expense"]

if not expense_data.empty:

    category_expenses = (
        expense_data
        .groupby("category")["amount"]
        .sum()
        .reset_index()
        .sort_values(
            "amount",
            ascending=False
        )
    )


    column1, column2 = st.columns(2)

    with column1:

        st.subheader("Expenses by Category")

        figure = px.pie(
            category_expenses,
            names="category",
            values="amount",
            title="Spending Distribution"
        )

        st.plotly_chart(figure, use_container_width=True)

    with column2:

        st.subheader("Category Spending")

        figure = px.bar(
            category_expenses,
            x="category",
            y="amount",
            title="Expenses by Category"
        )

        st.plotly_chart(figure, use_container_width=True)

st.subheader("Income vs Expenses")

comparison_data = pd.DataFrame({
    "Type": ["Income", "Expenses"],
    "Amount": [total_income, total_expenses]
})

figure = px.bar(
    comparison_data,
    x="Type",
    y="Amount",
    title="Income vs Expenses",
    text_auto=".2f"
)

st.plotly_chart(figure, use_container_width=True)

st.subheader("Transaction History")

display_data = dataframe.copy()

display_data["amount"] = display_data["amount"].map(lambda value: f"₹{value:,.2f}")

st.dataframe(
    display_data,
    use_container_width=True,
    hide_index=True
)

st.subheader("Delete Transaction")

transaction_ids = dataframe["id"].tolist()

selected_id = st.selectbox("Select Transaction ID", transaction_ids)

if st.button("Delete Selected Transaction"):
    delete_transaction(selected_id)

    st.success("Transaction deleted.")

    st.rerun()

st.divider()

st.caption("Personal Finance Dashboard | "
"Day 48 - #50DaysOfPython"
)
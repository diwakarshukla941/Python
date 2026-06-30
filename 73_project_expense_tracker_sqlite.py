# =========================================================
# FILE: 73_project_expense_tracker_sqlite.py
# PROJECT: EXPENSE TRACKER WITH SQLITE
# =========================================================
#
# Skills Used:
# - sqlite3
# - functions
# - data modeling
# - CRUD operations
# - aggregation
#

import sqlite3
from pathlib import Path


DB_FILE = Path("expenses.db")


def connect():
    return sqlite3.connect(DB_FILE)


def setup_database():
    with connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                category TEXT NOT NULL,
                amount REAL NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def add_expense(title, category, amount):
    with connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO expenses (title, category, amount)
            VALUES (?, ?, ?)
            """,
            (title, category, amount)
        )
        return cursor.lastrowid


def list_expenses():
    with connect() as connection:
        cursor = connection.execute(
            """
            SELECT id, title, category, amount, created_at
            FROM expenses
            ORDER BY id DESC
            """
        )
        return cursor.fetchall()


def total_by_category():
    with connect() as connection:
        cursor = connection.execute(
            """
            SELECT category, SUM(amount)
            FROM expenses
            GROUP BY category
            ORDER BY SUM(amount) DESC
            """
        )
        return cursor.fetchall()


def demo():
    setup_database()
    add_expense("Coffee", "food", 120)
    add_expense("Book", "education", 499)

    print("Expenses:")
    for expense in list_expenses():
        print(expense)

    print("Totals:")
    for category, total in total_by_category():
        print(category, total)


if __name__ == "__main__":
    demo()

# =========================================================
# PRACTICE TASKS
# =========================================================
#
# 1. Add update_expense().
# 2. Add delete_expense().
# 3. Add monthly reports.
# 4. Add budgets by category.
# 5. Add a CLI menu.
#
# =========================================================
# END OF 73_project_expense_tracker_sqlite.py
# =========================================================

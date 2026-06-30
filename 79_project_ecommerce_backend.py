# =========================================================
# FILE: 79_project_ecommerce_backend.py
# PROJECT: MINI E-COMMERCE BACKEND
# =========================================================
#
# Skills Used:
# - sqlite3
# - functions
# - transactions
# - data modeling
# - backend workflows
#

import sqlite3
from pathlib import Path


DB_FILE = Path("ecommerce.db")


def connect():
    return sqlite3.connect(DB_FILE)


def setup_database():
    with connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                stock INTEGER NOT NULL
            )
            """
        )
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                total REAL NOT NULL,
                created_at TEXT DEFAULT CURRENT_TIMESTAMP
            )
            """
        )


def add_product(name, price, stock):
    with connect() as connection:
        cursor = connection.execute(
            """
            INSERT INTO products (name, price, stock)
            VALUES (?, ?, ?)
            """,
            (name, price, stock)
        )
        return cursor.lastrowid


def get_product(product_id):
    with connect() as connection:
        cursor = connection.execute(
            """
            SELECT id, name, price, stock
            FROM products
            WHERE id = ?
            """,
            (product_id,)
        )
        return cursor.fetchone()


def create_order(product_id, quantity):
    with connect() as connection:
        product = connection.execute(
            """
            SELECT id, name, price, stock
            FROM products
            WHERE id = ?
            """,
            (product_id,)
        ).fetchone()

        if product is None:
            raise ValueError("Product not found")

        _, _, price, stock = product

        if quantity > stock:
            raise ValueError("Not enough stock")

        total = price * quantity

        connection.execute(
            """
            UPDATE products
            SET stock = stock - ?
            WHERE id = ?
            """,
            (quantity, product_id)
        )
        connection.execute(
            """
            INSERT INTO orders (product_id, quantity, total)
            VALUES (?, ?, ?)
            """,
            (product_id, quantity, total)
        )

        return total


def demo():
    setup_database()
    product_id = add_product("Python Book", 499, 10)
    total = create_order(product_id, 2)
    print("Order total:", total)
    print("Product after order:", get_product(product_id))


if __name__ == "__main__":
    demo()

# =========================================================
# PRACTICE TASKS
# =========================================================
#
# 1. Add users table.
# 2. Add cart table.
# 3. Add order items table.
# 4. Add product search.
# 5. Add API endpoints using FastAPI later.
#
# =========================================================
# END OF 79_project_ecommerce_backend.py
# =========================================================

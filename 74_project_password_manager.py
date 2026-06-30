# =========================================================
# FILE: 74_project_password_manager.py
# PROJECT: EDUCATIONAL PASSWORD MANAGER
# =========================================================
#
# Skills Used:
# - sqlite3
# - secrets
# - hashlib
# - functions
# - basic security thinking
#
# Note:
# This is for learning. A production password manager needs
# real encryption, careful key handling, and security review.
#

import hashlib
import secrets
import sqlite3
import string
from pathlib import Path


DB_FILE = Path("password_vault.db")


def connect():
    return sqlite3.connect(DB_FILE)


def setup_database():
    with connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT NOT NULL UNIQUE,
                username TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )
            """
        )


def generate_password(length=16):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(characters) for _ in range(length))


def hash_password(password):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def save_password(service, username, password):
    with connect() as connection:
        connection.execute(
            """
            INSERT OR REPLACE INTO passwords
            (service, username, password_hash)
            VALUES (?, ?, ?)
            """,
            (service, username, hash_password(password))
        )


def get_services():
    with connect() as connection:
        cursor = connection.execute(
            """
            SELECT service, username
            FROM passwords
            ORDER BY service
            """
        )
        return cursor.fetchall()


def demo():
    setup_database()
    password = generate_password()
    save_password("github", "diwakar", password)

    print("Generated password:", password)
    print("Saved services:")
    for service in get_services():
        print(service)


if __name__ == "__main__":
    demo()

# =========================================================
# PRACTICE TASKS
# =========================================================
#
# 1. Add password verification.
# 2. Add master password login.
# 3. Replace hashes with encryption for stored passwords.
# 4. Add delete_service().
# 5. Add password strength checks.
#
# =========================================================
# END OF 74_project_password_manager.py
# =========================================================

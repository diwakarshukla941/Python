# =========================================================
# FILE: 78_project_auth_system_sqlite.py
# PROJECT: AUTH SYSTEM WITH SQLITE
# =========================================================
#
# Skills Used:
# - sqlite3
# - hashlib.pbkdf2_hmac
# - secrets
# - validation
# - backend auth flow
#

import hashlib
import secrets
import sqlite3
from pathlib import Path


DB_FILE = Path("auth_system.db")


def connect():
    return sqlite3.connect(DB_FILE)


def setup_database():
    with connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                salt TEXT NOT NULL,
                password_hash TEXT NOT NULL
            )
            """
        )


def hash_password(password, salt):
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        bytes.fromhex(salt),
        100_000
    )
    return password_hash.hex()


def register_user(username, password):
    salt = secrets.token_hex(16)
    password_hash = hash_password(password, salt)

    with connect() as connection:
        connection.execute(
            """
            INSERT INTO users (username, salt, password_hash)
            VALUES (?, ?, ?)
            """,
            (username, salt, password_hash)
        )


def login_user(username, password):
    with connect() as connection:
        cursor = connection.execute(
            """
            SELECT salt, password_hash
            FROM users
            WHERE username = ?
            """,
            (username,)
        )
        row = cursor.fetchone()

    if row is None:
        return False

    salt, saved_hash = row
    return hash_password(password, salt) == saved_hash


def demo():
    setup_database()

    try:
        register_user("admin", "python123")
    except sqlite3.IntegrityError:
        pass

    print(login_user("admin", "python123"))
    print(login_user("admin", "wrong"))


if __name__ == "__main__":
    demo()

# =========================================================
# PRACTICE TASKS
# =========================================================
#
# 1. Add email field.
# 2. Add password strength validation.
# 3. Add change password.
# 4. Add sessions or tokens.
# 5. Connect this auth logic to an HTTP API.
#
# =========================================================
# END OF 78_project_auth_system_sqlite.py
# =========================================================

# =========================================================
# FILE: 80_project_final_backend_app.py
# PROJECT: FINAL BACKEND-STYLE APP
# =========================================================
#
# Skills Used:
# - sqlite3
# - http.server
# - JSON
# - routing
# - validation
# - backend architecture
#
# Run:
# python 80_project_final_backend_app.py
# Visit:
# http://localhost:8080/health
# http://localhost:8080/tasks
#

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sqlite3
from pathlib import Path


DB_FILE = Path("final_backend_app.db")


def connect():
    return sqlite3.connect(DB_FILE)


def setup_database():
    with connect() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0
            )
            """
        )
        connection.execute(
            """
            INSERT INTO tasks (title, done)
            SELECT ?, ?
            WHERE NOT EXISTS (SELECT 1 FROM tasks)
            """,
            ("Build final Python project", 0)
        )


def list_tasks():
    with connect() as connection:
        cursor = connection.execute(
            """
            SELECT id, title, done
            FROM tasks
            ORDER BY id
            """
        )
        return [
            {
                "id": row[0],
                "title": row[1],
                "done": bool(row[2])
            }
            for row in cursor.fetchall()
        ]


def send_json(handler, data, status=200):
    body = json.dumps(data, indent=2).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            send_json(self, {"status": "ok"})
            return

        if self.path == "/tasks":
            send_json(self, list_tasks())
            return

        send_json(self, {"error": "Not found"}, status=404)

    def log_message(self, format, *args):
        return


def run_server(host="localhost", port=8080):
    setup_database()
    server = HTTPServer((host, port), AppHandler)
    print(f"Final app running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()

# =========================================================
# FINAL PRACTICE TASKS
# =========================================================
#
# 1. Add POST /tasks.
# 2. Add PATCH /tasks/{id}.
# 3. Add DELETE /tasks/{id}.
# 4. Add authentication.
# 5. Convert this to FastAPI after learning frameworks.
# 6. Add pytest tests.
# 7. Add project folders: app/, tests/, config/.
# 8. Add a README.
#
# =========================================================
# END OF 80_project_final_backend_app.py
# =========================================================

# =========================================================
# FILE: 77_project_blog_api_http_server.py
# PROJECT: MINI BLOG API USING STANDARD LIBRARY
# =========================================================
#
# Skills Used:
# - http.server
# - JSON
# - classes
# - routing basics
# - backend thinking
#
# Run:
# python 77_project_blog_api_http_server.py
# Then visit:
# http://localhost:8000/posts
#

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


POSTS = [
    {
        "id": 1,
        "title": "Learning Python",
        "content": "Python is great for backend development."
    }
]


def json_response(handler, data, status=200):
    body = json.dumps(data).encode("utf-8")
    handler.send_response(status)
    handler.send_header("Content-Type", "application/json")
    handler.send_header("Content-Length", str(len(body)))
    handler.end_headers()
    handler.wfile.write(body)


class BlogHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/posts":
            json_response(self, POSTS)
            return

        json_response(self, {"error": "Not found"}, status=404)

    def log_message(self, format, *args):
        return


def run_server(host="localhost", port=8000):
    server = HTTPServer((host, port), BlogHandler)
    print(f"Blog API running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    run_server()

# =========================================================
# PRACTICE TASKS
# =========================================================
#
# 1. Add GET /posts/1.
# 2. Add POST /posts.
# 3. Store posts in SQLite.
# 4. Add validation.
# 5. Add error responses.
#
# =========================================================
# END OF 77_project_blog_api_http_server.py
# =========================================================

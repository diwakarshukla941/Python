# =========================================================
# FILE: 76_project_api_client.py
# PROJECT: API CLIENT
# =========================================================
#
# Skills Used:
# - urllib
# - JSON
# - exceptions
# - functions
# - API response handling
#
# This uses the standard library so no package install is needed.
#

import json
from urllib.error import URLError
from urllib.request import urlopen


def fetch_json(url, timeout=10):
    try:
        with urlopen(url, timeout=timeout) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)
    except URLError as error:
        print("Network error:", error)
        return None
    except json.JSONDecodeError:
        print("Invalid JSON response")
        return None


def extract_post_titles(posts):
    return [
        post["title"]
        for post in posts
        if "title" in post
    ]


def demo_without_network():
    posts = [
        {"id": 1, "title": "Learn Python"},
        {"id": 2, "title": "Build APIs"},
    ]

    print(extract_post_titles(posts))


def demo_with_network():
    url = "https://jsonplaceholder.typicode.com/posts"
    posts = fetch_json(url)

    if posts:
        for title in extract_post_titles(posts[:5]):
            print(title)


if __name__ == "__main__":
    demo_without_network()

# =========================================================
# PRACTICE TASKS
# =========================================================
#
# 1. Call demo_with_network() when internet is available.
# 2. Add query parameters.
# 3. Add POST request support.
# 4. Add retry logic.
# 5. Save API results to JSON.
#
# =========================================================
# END OF 76_project_api_client.py
# =========================================================

# =========================================================
# FILE: 71_project_cli_todo.py
# PROJECT: CLI TODO APP
# =========================================================
#
# Skills Used:
# - Lists and dictionaries
# - Functions
# - File handling
# - JSON
# - Basic CLI structure
#
# Run:
# python 71_project_cli_todo.py
#

from pathlib import Path
import json


DATA_FILE = Path("todo_data.json")


def load_tasks():
    if not DATA_FILE.exists():
        return []

    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def save_tasks(tasks):
    DATA_FILE.write_text(
        json.dumps(tasks, indent=4),
        encoding="utf-8"
    )


def add_task(title):
    tasks = load_tasks()

    task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)
    return task


def list_tasks():
    return load_tasks()


def mark_done(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            return task

    return None


def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [
        task
        for task in tasks
        if task["id"] != task_id
    ]

    save_tasks(updated_tasks)
    return len(tasks) != len(updated_tasks)


def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for task in tasks:
        status = "Done" if task["done"] else "Pending"
        print(f'{task["id"]}. [{status}] {task["title"]}')


def demo():
    print("CLI Todo App Demo")
    add_task("Learn exceptions")
    add_task("Build a Python project")
    mark_done(1)
    display_tasks(list_tasks())


if __name__ == "__main__":
    demo()

# =========================================================
# PRACTICE TASKS
# =========================================================
#
# 1. Add an update_task() function.
# 2. Add priority: low, medium, high.
# 3. Add due dates.
# 4. Add command-line arguments using argparse.
# 5. Prevent duplicate task titles.
#
# =========================================================
# END OF 71_project_cli_todo.py
# =========================================================

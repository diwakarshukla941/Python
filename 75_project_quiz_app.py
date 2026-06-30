# =========================================================
# FILE: 75_project_quiz_app.py
# PROJECT: QUIZ APP
# =========================================================
#
# Skills Used:
# - lists
# - dictionaries
# - functions
# - loops
# - scoring
#


QUESTIONS = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "def", "function", "lambda"],
        "answer": "def"
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["list", "tuple", "dict", "set"],
        "answer": "dict"
    },
    {
        "question": "Which module is used for SQLite?",
        "options": ["sqlite", "sqlite3", "database", "sql"],
        "answer": "sqlite3"
    },
]


def check_answer(question, selected_option):
    return selected_option == question["answer"]


def calculate_score(questions, answers):
    score = 0

    for question, answer in zip(questions, answers):
        if check_answer(question, answer):
            score += 1

    return score


def display_result(score, total):
    print(f"Score: {score}/{total}")

    if score == total:
        print("Excellent")
    elif score >= total / 2:
        print("Good")
    else:
        print("Keep practicing")


def demo():
    sample_answers = ["def", "dict", "sqlite3"]
    score = calculate_score(QUESTIONS, sample_answers)
    display_result(score, len(QUESTIONS))


if __name__ == "__main__":
    demo()

# =========================================================
# PRACTICE TASKS
# =========================================================
#
# 1. Take answers using input().
# 2. Shuffle questions.
# 3. Store questions in JSON.
# 4. Add difficulty levels.
# 5. Save scores to a file.
#
# =========================================================
# END OF 75_project_quiz_app.py
# =========================================================

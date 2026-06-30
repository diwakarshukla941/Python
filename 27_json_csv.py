# ========================================================
# FILE: 27_json_csv.py
# ========================================================

# PART 1
# ========================================================
# PYTHON JSON & CSV
# ========================================================

# INDEX
#
# 1. What is JSON?
# 2. json.dumps()
# 3. json.loads()
# 4. JSON Files
# 5. CSV Files
# 6. csv.reader
# 7. csv.DictReader
# 8. Practical Examples
#
# ========================================================
# 1. WHAT IS JSON CSV?
# ========================================================

# Json Csv is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# BASIC EXAMPLE
# ========================================================

topic = "Json Csv"
print(topic)
print(type(topic))

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. WHAT IS JSON?
# ========================================================

# What is JSON? is part of the foundation of Json Csv.
# Read the comments first, then run the small example.

# ========================================================
# 4. JSON.DUMPS()
# ========================================================

# json.dumps() is part of the foundation of Json Csv.
# Read the comments first, then run the small example.

# ========================================================
# 5. JSON.LOADS()
# ========================================================

# json.loads() is part of the foundation of Json Csv.
# Read the comments first, then run the small example.

# ========================================================
# FUNCTION EXAMPLE
# ========================================================

def explain_json_csv():
    return "Json Csv is important in Python."

print(explain_json_csv())

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# PRACTICAL EXAMPLE
# ========================================================

items = ["concept", "example", "practice"]

for index, item in enumerate(items, start=1):
    print(index, "Json Csv", item)

# ========================================================
# COMMON BEGINNER MISTAKES
# ========================================================

# Mistake 1
# Trying to memorize syntax without running examples.
#
# Mistake 2
# Skipping small examples and jumping directly to projects.
#
# Mistake 3
# Not reading error messages carefully.

# ========================================================
# FILE: 27_json_csv.py
# ========================================================

# PART 2
# ========================================================
# PYTHON JSON & CSV - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. What is JSON?
# 2. json.dumps()
# 3. json.loads()
# 4. JSON Files
# 5. CSV Files
# 6. csv.reader
# 7. csv.DictReader
# 8. Practical Examples
#
# ========================================================
# 8. JSON FILES
# ========================================================

# This section focuses on json files.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

def display(value):
    print("Value:", value)

display("Python")

# ========================================================
# 9. CSV FILES
# ========================================================

# This section focuses on csv files.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# 10. CSV.READER
# ========================================================

# This section focuses on csv.reader.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

data = {
    "name": "Python",
    "level": "Beginner to Advanced"
}

print(data["name"])
print(data.get("level"))

# ========================================================
# REAL-WORLD NOTES
# ========================================================

# In real projects, Json Csv should be used with clean names,
# small functions, clear error handling, and simple structure.
# Do not make code clever when readable code is enough.

# ========================================================
# MORE PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# DATA PROCESSING EXAMPLE
# ========================================================

records = [
    {"name": "Amit", "score": 85},
    {"name": "Rahul", "score": 92},
    {"name": "Rohan", "score": 76},
]

passed = [record for record in records if record["score"] >= 80]
print(passed)

# ========================================================
# COMMON BEGINNER MISTAKES
# ========================================================

# Mistake 1
# Writing code that works only for one hard-coded value.
#
# Mistake 2
# Ignoring naming and formatting.
#
# Mistake 3
# Not testing edge cases.

# ========================================================
# FILE: 27_json_csv.py
# ========================================================

# PART 3
# ========================================================
# PYTHON JSON & CSV - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. What is JSON?
# 2. json.dumps()
# 3. json.loads()
# 4. JSON Files
# 5. CSV Files
# 6. csv.reader
# 7. csv.DictReader
# 8. Practical Examples
#
# ========================================================
# 14. CSV.DICTREADER
# ========================================================

# csv.DictReader helps connect Json Csv to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. PRACTICAL EXAMPLES
# ========================================================

# Practical Examples helps connect Json Csv to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# REAL-WORLD PRACTICE
# ========================================================

# ========================================================
# MINI BACKEND-STYLE EXAMPLE
# ========================================================

def validate_required(data, required_fields):
    missing = []

    for field in required_fields:
        if field not in data or data[field] in ("", None):
            missing.append(field)

    return missing

user = {
    "name": "Diwakar",
    "email": "diwakar@example.com"
}

print(validate_required(user, ["name", "email", "password"]))

# ========================================================
# INTERVIEW QUESTIONS
# ========================================================

# Q1. What is Json Csv?
# Answer:
# Json Csv is a Python topic used to write better programs.
#
# Q2. Why is Json Csv useful?
# Answer:
# It improves readability, maintainability, and problem solving.
#
# Q3. What is a common beginner mistake?
# Answer:
# Using syntax without understanding the concept.
#
# Q4. How should you practice it?
# Answer:
# Write small examples, then apply it in a real project.
#
# Q5. Where is it used in backend development?
# Answer:
# In validation, data processing, project structure, APIs,
# database code, testing, configuration, and debugging.

# ========================================================
# QUICK REVISION
# ========================================================

# - Json Csv is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 27_json_csv.py
# ========================================================


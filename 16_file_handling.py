# ========================================================
# FILE: 16_file_handling.py
# ========================================================

# PART 1
# ========================================================
# PYTHON FILE HANDLING
# ========================================================

# INDEX
#
# 1. What is File Handling?
# 2. Opening Files
# 3. Reading Files
# 4. Writing Files
# 5. Appending Files
# 6. with Statement
# 7. File Paths
# 8. Practical Examples
#
# ========================================================
# 1. WHAT IS FILE HANDLING?
# ========================================================

# File Handling is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# WRITE TEXT FILE
# ========================================================

from pathlib import Path

path = Path("sample_notes.txt")
path.write_text("Learning Python file handling", encoding="utf-8")
print(path.exists())
path.unlink()

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. WHAT IS FILE HANDLING?
# ========================================================

# What is File Handling? is part of the foundation of File Handling.
# Read the comments first, then run the small example.

# ========================================================
# 4. OPENING FILES
# ========================================================

# Opening Files is part of the foundation of File Handling.
# Read the comments first, then run the small example.

# ========================================================
# 5. READING FILES
# ========================================================

# Reading Files is part of the foundation of File Handling.
# Read the comments first, then run the small example.

# ========================================================
# READ LINES
# ========================================================

lines = ["Python\n", "Files\n", "Practice\n"]
print([line.strip() for line in lines])

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# WITH STATEMENT
# ========================================================

from pathlib import Path

path = Path("temporary_file.txt")
with path.open("w", encoding="utf-8") as file:
    file.write("Hello")
print(path.read_text(encoding="utf-8"))
path.unlink()

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
# FILE: 16_file_handling.py
# ========================================================

# PART 2
# ========================================================
# PYTHON FILE HANDLING - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. What is File Handling?
# 2. Opening Files
# 3. Reading Files
# 4. Writing Files
# 5. Appending Files
# 6. with Statement
# 7. File Paths
# 8. Practical Examples
#
# ========================================================
# 8. WRITING FILES
# ========================================================

# This section focuses on writing files.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# 9. APPENDING FILES
# ========================================================

# This section focuses on appending files.
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
# 10. WITH STATEMENT
# ========================================================

# This section focuses on with statement.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

def display(value):
    print("Value:", value)

display("Python")

# ========================================================
# REAL-WORLD NOTES
# ========================================================

# In real projects, File Handling should be used with clean names,
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
# FILE: 16_file_handling.py
# ========================================================

# PART 3
# ========================================================
# PYTHON FILE HANDLING - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. What is File Handling?
# 2. Opening Files
# 3. Reading Files
# 4. Writing Files
# 5. Appending Files
# 6. with Statement
# 7. File Paths
# 8. Practical Examples
#
# ========================================================
# 14. FILE PATHS
# ========================================================

# File Paths helps connect File Handling to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. PRACTICAL EXAMPLES
# ========================================================

# Practical Examples helps connect File Handling to practical Python.
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

# Q1. What is File Handling?
# Answer:
# File Handling is a Python topic used to write better programs.
#
# Q2. Why is File Handling useful?
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

# - File Handling is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 16_file_handling.py
# ========================================================


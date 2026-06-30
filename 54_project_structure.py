# ========================================================
# FILE: 54_project_structure.py
# ========================================================

# PART 1
# ========================================================
# PYTHON PROJECT STRUCTURE
# ========================================================

# INDEX
#
# 1. Why Structure Matters
# 2. Flat Layout
# 3. src Layout
# 4. Packages
# 5. Tests Folder
# 6. Config Files
# 7. Documentation
# 8. Backend Structure
#
# ========================================================
# 1. WHAT IS PROJECT STRUCTURE?
# ========================================================

# Project Structure is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# BASIC EXAMPLE
# ========================================================

topic = "Project Structure"
print(topic)
print(type(topic))

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. WHY STRUCTURE MATTERS
# ========================================================

# Why Structure Matters is part of the foundation of Project Structure.
# Read the comments first, then run the small example.

# ========================================================
# 4. FLAT LAYOUT
# ========================================================

# Flat Layout is part of the foundation of Project Structure.
# Read the comments first, then run the small example.

# ========================================================
# 5. SRC LAYOUT
# ========================================================

# src Layout is part of the foundation of Project Structure.
# Read the comments first, then run the small example.

# ========================================================
# FUNCTION EXAMPLE
# ========================================================

def explain_project_structure():
    return "Project Structure is important in Python."

print(explain_project_structure())

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# PRACTICAL EXAMPLE
# ========================================================

items = ["concept", "example", "practice"]

for index, item in enumerate(items, start=1):
    print(index, "Project Structure", item)

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
# FILE: 54_project_structure.py
# ========================================================

# PART 2
# ========================================================
# PYTHON PROJECT STRUCTURE - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. Why Structure Matters
# 2. Flat Layout
# 3. src Layout
# 4. Packages
# 5. Tests Folder
# 6. Config Files
# 7. Documentation
# 8. Backend Structure
#
# ========================================================
# 8. PACKAGES
# ========================================================

# This section focuses on packages.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

def display(value):
    print("Value:", value)

display("Python")

# ========================================================
# 9. TESTS FOLDER
# ========================================================

# This section focuses on tests folder.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# 10. CONFIG FILES
# ========================================================

# This section focuses on config files.
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

# In real projects, Project Structure should be used with clean names,
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
# FILE: 54_project_structure.py
# ========================================================

# PART 3
# ========================================================
# PYTHON PROJECT STRUCTURE - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. Why Structure Matters
# 2. Flat Layout
# 3. src Layout
# 4. Packages
# 5. Tests Folder
# 6. Config Files
# 7. Documentation
# 8. Backend Structure
#
# ========================================================
# 14. DOCUMENTATION
# ========================================================

# Documentation helps connect Project Structure to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. BACKEND STRUCTURE
# ========================================================

# Backend Structure helps connect Project Structure to practical Python.
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

# Q1. What is Project Structure?
# Answer:
# Project Structure is a Python topic used to write better programs.
#
# Q2. Why is Project Structure useful?
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

# - Project Structure is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 54_project_structure.py
# ========================================================


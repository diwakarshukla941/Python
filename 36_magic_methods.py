# ========================================================
# FILE: 36_magic_methods.py
# ========================================================

# PART 1
# ========================================================
# PYTHON MAGIC METHODS
# ========================================================

# INDEX
#
# 1. What are Magic Methods?
# 2. __init__
# 3. __str__
# 4. __repr__
# 5. __len__
# 6. __eq__
# 7. Operator Methods
# 8. Practical Examples
#
# ========================================================
# 1. WHAT IS MAGIC METHODS?
# ========================================================

# Magic Methods is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# BASIC EXAMPLE
# ========================================================

topic = "Magic Methods"
print(topic)
print(type(topic))

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. WHAT ARE MAGIC METHODS?
# ========================================================

# What are Magic Methods? is part of the foundation of Magic Methods.
# Read the comments first, then run the small example.

# ========================================================
# 4. __INIT__
# ========================================================

# __init__ is part of the foundation of Magic Methods.
# Read the comments first, then run the small example.

# ========================================================
# 5. __STR__
# ========================================================

# __str__ is part of the foundation of Magic Methods.
# Read the comments first, then run the small example.

# ========================================================
# FUNCTION EXAMPLE
# ========================================================

def explain_magic_methods():
    return "Magic Methods is important in Python."

print(explain_magic_methods())

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# PRACTICAL EXAMPLE
# ========================================================

items = ["concept", "example", "practice"]

for index, item in enumerate(items, start=1):
    print(index, "Magic Methods", item)

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
# FILE: 36_magic_methods.py
# ========================================================

# PART 2
# ========================================================
# PYTHON MAGIC METHODS - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. What are Magic Methods?
# 2. __init__
# 3. __str__
# 4. __repr__
# 5. __len__
# 6. __eq__
# 7. Operator Methods
# 8. Practical Examples
#
# ========================================================
# 8. __REPR__
# ========================================================

# This section focuses on __repr__.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

def display(value):
    print("Value:", value)

display("Python")

# ========================================================
# 9. __LEN__
# ========================================================

# This section focuses on __len__.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# 10. __EQ__
# ========================================================

# This section focuses on __eq__.
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

# In real projects, Magic Methods should be used with clean names,
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
# FILE: 36_magic_methods.py
# ========================================================

# PART 3
# ========================================================
# PYTHON MAGIC METHODS - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. What are Magic Methods?
# 2. __init__
# 3. __str__
# 4. __repr__
# 5. __len__
# 6. __eq__
# 7. Operator Methods
# 8. Practical Examples
#
# ========================================================
# 14. OPERATOR METHODS
# ========================================================

# Operator Methods helps connect Magic Methods to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. PRACTICAL EXAMPLES
# ========================================================

# Practical Examples helps connect Magic Methods to practical Python.
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

# Q1. What is Magic Methods?
# Answer:
# Magic Methods is a Python topic used to write better programs.
#
# Q2. Why is Magic Methods useful?
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

# - Magic Methods is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 36_magic_methods.py
# ========================================================


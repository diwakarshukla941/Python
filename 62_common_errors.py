# ========================================================
# FILE: 62_common_errors.py
# ========================================================

# PART 1
# ========================================================
# PYTHON COMMON ERRORS
# ========================================================

# INDEX
#
# 1. SyntaxError
# 2. NameError
# 3. TypeError
# 4. ValueError
# 5. IndexError
# 6. KeyError
# 7. AttributeError
# 8. Debugging Tips
#
# ========================================================
# 1. WHAT IS COMMON ERRORS?
# ========================================================

# Common Errors is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# BASIC EXAMPLE
# ========================================================

topic = "Common Errors"
print(topic)
print(type(topic))

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. SYNTAXERROR
# ========================================================

# SyntaxError is part of the foundation of Common Errors.
# Read the comments first, then run the small example.

# ========================================================
# 4. NAMEERROR
# ========================================================

# NameError is part of the foundation of Common Errors.
# Read the comments first, then run the small example.

# ========================================================
# 5. TYPEERROR
# ========================================================

# TypeError is part of the foundation of Common Errors.
# Read the comments first, then run the small example.

# ========================================================
# FUNCTION EXAMPLE
# ========================================================

def explain_common_errors():
    return "Common Errors is important in Python."

print(explain_common_errors())

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# PRACTICAL EXAMPLE
# ========================================================

items = ["concept", "example", "practice"]

for index, item in enumerate(items, start=1):
    print(index, "Common Errors", item)

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
# FILE: 62_common_errors.py
# ========================================================

# PART 2
# ========================================================
# PYTHON COMMON ERRORS - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. SyntaxError
# 2. NameError
# 3. TypeError
# 4. ValueError
# 5. IndexError
# 6. KeyError
# 7. AttributeError
# 8. Debugging Tips
#
# ========================================================
# 8. VALUEERROR
# ========================================================

# This section focuses on valueerror.
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
# 9. INDEXERROR
# ========================================================

# This section focuses on indexerror.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

def display(value):
    print("Value:", value)

display("Python")

# ========================================================
# 10. KEYERROR
# ========================================================

# This section focuses on keyerror.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# REAL-WORLD NOTES
# ========================================================

# In real projects, Common Errors should be used with clean names,
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
# FILE: 62_common_errors.py
# ========================================================

# PART 3
# ========================================================
# PYTHON COMMON ERRORS - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. SyntaxError
# 2. NameError
# 3. TypeError
# 4. ValueError
# 5. IndexError
# 6. KeyError
# 7. AttributeError
# 8. Debugging Tips
#
# ========================================================
# 14. ATTRIBUTEERROR
# ========================================================

# AttributeError helps connect Common Errors to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. DEBUGGING TIPS
# ========================================================

# Debugging Tips helps connect Common Errors to practical Python.
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

# Q1. What is Common Errors?
# Answer:
# Common Errors is a Python topic used to write better programs.
#
# Q2. Why is Common Errors useful?
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

# - Common Errors is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 62_common_errors.py
# ========================================================


# ========================================================
# FILE: 15_exceptions.py
# ========================================================

# PART 1
# ========================================================
# PYTHON EXCEPTIONS
# ========================================================

# INDEX
#
# 1. What are Exceptions?
# 2. Why Exception Handling?
# 3. try-except
# 4. Multiple Exceptions
# 5. else and finally
# 6. raise
# 7. Custom Exceptions
# 8. Best Practices
#
# ========================================================
# 1. WHAT IS EXCEPTIONS?
# ========================================================

# Exceptions is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# BASIC try-except
# ========================================================

try:
    number = int("10")
    print(number)
except ValueError:
    print("Invalid number")

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. WHAT ARE EXCEPTIONS?
# ========================================================

# What are Exceptions? is part of the foundation of Exceptions.
# Read the comments first, then run the small example.

# ========================================================
# 4. WHY EXCEPTION HANDLING?
# ========================================================

# Why Exception Handling? is part of the foundation of Exceptions.
# Read the comments first, then run the small example.

# ========================================================
# 5. TRY-EXCEPT
# ========================================================

# try-except is part of the foundation of Exceptions.
# Read the comments first, then run the small example.

# ========================================================
# MULTIPLE EXCEPTIONS
# ========================================================

values = [10, 0]

try:
    result = values[0] / values[1]
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except IndexError:
    print("Invalid index")

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# CUSTOM EXCEPTION
# ========================================================

class InvalidAgeError(Exception):
    pass

age = 15

if age < 18:
    print("InvalidAgeError would be raised here")

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
# FILE: 15_exceptions.py
# ========================================================

# PART 2
# ========================================================
# PYTHON EXCEPTIONS - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. What are Exceptions?
# 2. Why Exception Handling?
# 3. try-except
# 4. Multiple Exceptions
# 5. else and finally
# 6. raise
# 7. Custom Exceptions
# 8. Best Practices
#
# ========================================================
# 8. MULTIPLE EXCEPTIONS
# ========================================================

# This section focuses on multiple exceptions.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

def display(value):
    print("Value:", value)

display("Python")

# ========================================================
# 9. ELSE AND FINALLY
# ========================================================

# This section focuses on else and finally.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# 10. RAISE
# ========================================================

# This section focuses on raise.
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

# In real projects, Exceptions should be used with clean names,
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
# FILE: 15_exceptions.py
# ========================================================

# PART 3
# ========================================================
# PYTHON EXCEPTIONS - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. What are Exceptions?
# 2. Why Exception Handling?
# 3. try-except
# 4. Multiple Exceptions
# 5. else and finally
# 6. raise
# 7. Custom Exceptions
# 8. Best Practices
#
# ========================================================
# 14. CUSTOM EXCEPTIONS
# ========================================================

# Custom Exceptions helps connect Exceptions to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. BEST PRACTICES
# ========================================================

# Best Practices helps connect Exceptions to practical Python.
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

# Q1. What is Exceptions?
# Answer:
# Exceptions is a Python topic used to write better programs.
#
# Q2. Why is Exceptions useful?
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

# - Exceptions is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 15_exceptions.py
# ========================================================


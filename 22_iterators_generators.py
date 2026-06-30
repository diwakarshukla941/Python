# ========================================================
# FILE: 22_iterators_generators.py
# ========================================================

# PART 1
# ========================================================
# PYTHON ITERATORS & GENERATORS
# ========================================================

# INDEX
#
# 1. Iterable vs Iterator
# 2. iter()
# 3. next()
# 4. Custom Iterators
# 5. Generators
# 6. yield
# 7. Generator Expressions
# 8. Memory Efficiency
#
# ========================================================
# 1. WHAT IS ITERATORS GENERATORS?
# ========================================================

# Iterators Generators is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# BASIC EXAMPLE
# ========================================================

topic = "Iterators Generators"
print(topic)
print(type(topic))

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. ITERABLE VS ITERATOR
# ========================================================

# Iterable vs Iterator is part of the foundation of Iterators Generators.
# Read the comments first, then run the small example.

# ========================================================
# 4. ITER()
# ========================================================

# iter() is part of the foundation of Iterators Generators.
# Read the comments first, then run the small example.

# ========================================================
# 5. NEXT()
# ========================================================

# next() is part of the foundation of Iterators Generators.
# Read the comments first, then run the small example.

# ========================================================
# FUNCTION EXAMPLE
# ========================================================

def explain_iterators_generators():
    return "Iterators Generators is important in Python."

print(explain_iterators_generators())

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# PRACTICAL EXAMPLE
# ========================================================

items = ["concept", "example", "practice"]

for index, item in enumerate(items, start=1):
    print(index, "Iterators Generators", item)

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
# FILE: 22_iterators_generators.py
# ========================================================

# PART 2
# ========================================================
# PYTHON ITERATORS & GENERATORS - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. Iterable vs Iterator
# 2. iter()
# 3. next()
# 4. Custom Iterators
# 5. Generators
# 6. yield
# 7. Generator Expressions
# 8. Memory Efficiency
#
# ========================================================
# 8. CUSTOM ITERATORS
# ========================================================

# This section focuses on custom iterators.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# 9. GENERATORS
# ========================================================

# This section focuses on generators.
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
# 10. YIELD
# ========================================================

# This section focuses on yield.
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

# In real projects, Iterators Generators should be used with clean names,
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
# FILE: 22_iterators_generators.py
# ========================================================

# PART 3
# ========================================================
# PYTHON ITERATORS & GENERATORS - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. Iterable vs Iterator
# 2. iter()
# 3. next()
# 4. Custom Iterators
# 5. Generators
# 6. yield
# 7. Generator Expressions
# 8. Memory Efficiency
#
# ========================================================
# 14. GENERATOR EXPRESSIONS
# ========================================================

# Generator Expressions helps connect Iterators Generators to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. MEMORY EFFICIENCY
# ========================================================

# Memory Efficiency helps connect Iterators Generators to practical Python.
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

# Q1. What is Iterators Generators?
# Answer:
# Iterators Generators is a Python topic used to write better programs.
#
# Q2. Why is Iterators Generators useful?
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

# - Iterators Generators is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 22_iterators_generators.py
# ========================================================


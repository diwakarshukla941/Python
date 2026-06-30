# ========================================================
# FILE: 19_polymorphism.py
# ========================================================

# PART 1
# ========================================================
# PYTHON POLYMORPHISM
# ========================================================

# INDEX
#
# 1. What is Polymorphism?
# 2. Duck Typing
# 3. Method Overriding
# 4. Operator Overloading
# 5. Function Polymorphism
# 6. Class Polymorphism
# 7. Practical Examples
# 8. Interview Questions
#
# ========================================================
# 1. WHAT IS POLYMORPHISM?
# ========================================================

# Polymorphism is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# DUCK TYPING
# ========================================================

class EmailSender:
    def send(self):
        print("Email sent")

class SmsSender:
    def send(self):
        print("SMS sent")

def notify(sender):
    sender.send()

notify(EmailSender())
notify(SmsSender())

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. WHAT IS POLYMORPHISM?
# ========================================================

# What is Polymorphism? is part of the foundation of Polymorphism.
# Read the comments first, then run the small example.

# ========================================================
# 4. DUCK TYPING
# ========================================================

# Duck Typing is part of the foundation of Polymorphism.
# Read the comments first, then run the small example.

# ========================================================
# 5. METHOD OVERRIDING
# ========================================================

# Method Overriding is part of the foundation of Polymorphism.
# Read the comments first, then run the small example.

# ========================================================
# FUNCTION POLYMORPHISM
# ========================================================

print(len("Python"))
print(len([1, 2, 3]))
print(len({"a": 1, "b": 2}))

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# OPERATOR OVERLOADING
# ========================================================

class Price:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Price(self.amount + other.amount)

print((Price(10) + Price(20)).amount)

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
# FILE: 19_polymorphism.py
# ========================================================

# PART 2
# ========================================================
# PYTHON POLYMORPHISM - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. What is Polymorphism?
# 2. Duck Typing
# 3. Method Overriding
# 4. Operator Overloading
# 5. Function Polymorphism
# 6. Class Polymorphism
# 7. Practical Examples
# 8. Interview Questions
#
# ========================================================
# 8. OPERATOR OVERLOADING
# ========================================================

# This section focuses on operator overloading.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# 9. FUNCTION POLYMORPHISM
# ========================================================

# This section focuses on function polymorphism.
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
# 10. CLASS POLYMORPHISM
# ========================================================

# This section focuses on class polymorphism.
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

# In real projects, Polymorphism should be used with clean names,
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
# FILE: 19_polymorphism.py
# ========================================================

# PART 3
# ========================================================
# PYTHON POLYMORPHISM - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. What is Polymorphism?
# 2. Duck Typing
# 3. Method Overriding
# 4. Operator Overloading
# 5. Function Polymorphism
# 6. Class Polymorphism
# 7. Practical Examples
# 8. Interview Questions
#
# ========================================================
# 14. PRACTICAL EXAMPLES
# ========================================================

# Practical Examples helps connect Polymorphism to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. INTERVIEW QUESTIONS
# ========================================================

# Interview Questions helps connect Polymorphism to practical Python.
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

# Q1. What is Polymorphism?
# Answer:
# Polymorphism is a Python topic used to write better programs.
#
# Q2. Why is Polymorphism useful?
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

# - Polymorphism is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 19_polymorphism.py
# ========================================================


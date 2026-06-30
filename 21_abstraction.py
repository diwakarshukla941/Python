# ========================================================
# FILE: 21_abstraction.py
# ========================================================

# PART 1
# ========================================================
# PYTHON ABSTRACTION
# ========================================================

# INDEX
#
# 1. What is Abstraction?
# 2. Why Abstraction?
# 3. abc Module
# 4. Abstract Classes
# 5. Abstract Methods
# 6. Interfaces
# 7. Practical Examples
# 8. Best Practices
#
# ========================================================
# 1. WHAT IS ABSTRACTION?
# ========================================================

# Abstraction is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# ABSTRACT CLASS
# ========================================================

from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CardPayment(Payment):
    def pay(self, amount):
        print("Paid", amount)

CardPayment().pay(500)

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. WHAT IS ABSTRACTION?
# ========================================================

# What is Abstraction? is part of the foundation of Abstraction.
# Read the comments first, then run the small example.

# ========================================================
# 4. WHY ABSTRACTION?
# ========================================================

# Why Abstraction? is part of the foundation of Abstraction.
# Read the comments first, then run the small example.

# ========================================================
# 5. ABC MODULE
# ========================================================

# abc Module is part of the foundation of Abstraction.
# Read the comments first, then run the small example.

# ========================================================
# INTERFACE STYLE
# ========================================================

class Repository(ABC):
    @abstractmethod
    def save(self, data):
        pass

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# HIDING DETAILS
# ========================================================

def send_payment(payment, amount):
    payment.pay(amount)

send_payment(CardPayment(), 1000)

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
# FILE: 21_abstraction.py
# ========================================================

# PART 2
# ========================================================
# PYTHON ABSTRACTION - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. What is Abstraction?
# 2. Why Abstraction?
# 3. abc Module
# 4. Abstract Classes
# 5. Abstract Methods
# 6. Interfaces
# 7. Practical Examples
# 8. Best Practices
#
# ========================================================
# 8. ABSTRACT CLASSES
# ========================================================

# This section focuses on abstract classes.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

def display(value):
    print("Value:", value)

display("Python")

# ========================================================
# 9. ABSTRACT METHODS
# ========================================================

# This section focuses on abstract methods.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# 10. INTERFACES
# ========================================================

# This section focuses on interfaces.
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

# In real projects, Abstraction should be used with clean names,
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
# FILE: 21_abstraction.py
# ========================================================

# PART 3
# ========================================================
# PYTHON ABSTRACTION - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. What is Abstraction?
# 2. Why Abstraction?
# 3. abc Module
# 4. Abstract Classes
# 5. Abstract Methods
# 6. Interfaces
# 7. Practical Examples
# 8. Best Practices
#
# ========================================================
# 14. PRACTICAL EXAMPLES
# ========================================================

# Practical Examples helps connect Abstraction to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. BEST PRACTICES
# ========================================================

# Best Practices helps connect Abstraction to practical Python.
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

# Q1. What is Abstraction?
# Answer:
# Abstraction is a Python topic used to write better programs.
#
# Q2. Why is Abstraction useful?
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

# - Abstraction is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 21_abstraction.py
# ========================================================


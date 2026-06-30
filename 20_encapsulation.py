# ========================================================
# FILE: 20_encapsulation.py
# ========================================================

# PART 1
# ========================================================
# PYTHON ENCAPSULATION
# ========================================================

# INDEX
#
# 1. What is Encapsulation?
# 2. Public Members
# 3. Protected Members
# 4. Private Members
# 5. Getters and Setters
# 6. Properties
# 7. Validation
# 8. Practical Examples
#
# ========================================================
# 1. WHAT IS ENCAPSULATION?
# ========================================================

# Encapsulation is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# PRIVATE MEMBER
# ========================================================

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)
print(account.get_balance())

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. WHAT IS ENCAPSULATION?
# ========================================================

# What is Encapsulation? is part of the foundation of Encapsulation.
# Read the comments first, then run the small example.

# ========================================================
# 4. PUBLIC MEMBERS
# ========================================================

# Public Members is part of the foundation of Encapsulation.
# Read the comments first, then run the small example.

# ========================================================
# 5. PROTECTED MEMBERS
# ========================================================

# Protected Members is part of the foundation of Encapsulation.
# Read the comments first, then run the small example.

# ========================================================
# PROPERTY
# ========================================================

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

print(Product(100).price)

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# VALIDATION
# ========================================================

class User:
    def set_password(self, password):
        if len(password) < 8:
            print("Weak password")
        else:
            print("Password accepted")

User().set_password("python123")

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
# FILE: 20_encapsulation.py
# ========================================================

# PART 2
# ========================================================
# PYTHON ENCAPSULATION - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. What is Encapsulation?
# 2. Public Members
# 3. Protected Members
# 4. Private Members
# 5. Getters and Setters
# 6. Properties
# 7. Validation
# 8. Practical Examples
#
# ========================================================
# 8. PRIVATE MEMBERS
# ========================================================

# This section focuses on private members.
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
# 9. GETTERS AND SETTERS
# ========================================================

# This section focuses on getters and setters.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

def display(value):
    print("Value:", value)

display("Python")

# ========================================================
# 10. PROPERTIES
# ========================================================

# This section focuses on properties.
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

# In real projects, Encapsulation should be used with clean names,
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
# FILE: 20_encapsulation.py
# ========================================================

# PART 3
# ========================================================
# PYTHON ENCAPSULATION - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. What is Encapsulation?
# 2. Public Members
# 3. Protected Members
# 4. Private Members
# 5. Getters and Setters
# 6. Properties
# 7. Validation
# 8. Practical Examples
#
# ========================================================
# 14. VALIDATION
# ========================================================

# Validation helps connect Encapsulation to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. PRACTICAL EXAMPLES
# ========================================================

# Practical Examples helps connect Encapsulation to practical Python.
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

# Q1. What is Encapsulation?
# Answer:
# Encapsulation is a Python topic used to write better programs.
#
# Q2. Why is Encapsulation useful?
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

# - Encapsulation is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 20_encapsulation.py
# ========================================================


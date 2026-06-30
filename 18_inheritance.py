# ========================================================
# FILE: 18_inheritance.py
# ========================================================

# PART 1
# ========================================================
# PYTHON INHERITANCE
# ========================================================

# INDEX
#
# 1. What is Inheritance?
# 2. Parent and Child Classes
# 3. Single Inheritance
# 4. Multilevel Inheritance
# 5. Multiple Inheritance
# 6. super()
# 7. Method Overriding
# 8. Best Practices
#
# ========================================================
# 1. WHAT IS INHERITANCE?
# ========================================================

# Inheritance is an important Python topic.
# This file follows the same learning pattern:
# concept explanation, small examples, practical examples,
# common mistakes, interview questions, and quick revision.

# ========================================================
# SINGLE INHERITANCE
# ========================================================

class User:
    def login(self):
        print("User logged in")

class Admin(User):
    def delete_user(self):
        print("User deleted")

admin = Admin()
admin.login()
admin.delete_user()

# ========================================================
# 2. WHY THIS TOPIC MATTERS
# ========================================================

# A backend Python developer should understand this topic
# because it improves code quality, readability, debugging,
# project organization, and real-world problem solving.

# ========================================================
# 3. WHAT IS INHERITANCE?
# ========================================================

# What is Inheritance? is part of the foundation of Inheritance.
# Read the comments first, then run the small example.

# ========================================================
# 4. PARENT AND CHILD CLASSES
# ========================================================

# Parent and Child Classes is part of the foundation of Inheritance.
# Read the comments first, then run the small example.

# ========================================================
# 5. SINGLE INHERITANCE
# ========================================================

# Single Inheritance is part of the foundation of Inheritance.
# Read the comments first, then run the small example.

# ========================================================
# super()
# ========================================================

class Employee:
    def __init__(self, name):
        self.name = name

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

print(Developer("Diwakar", "Python").language)

# ========================================================
# PRACTICAL EXAMPLES
# ========================================================

# ========================================================
# OVERRIDING
# ========================================================

class Animal:
    def speak(self):
        print("Sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

Dog().speak()

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
# FILE: 18_inheritance.py
# ========================================================

# PART 2
# ========================================================
# PYTHON INHERITANCE - DEEPER CONCEPTS
# ========================================================

# INDEX
#
# 1. What is Inheritance?
# 2. Parent and Child Classes
# 3. Single Inheritance
# 4. Multilevel Inheritance
# 5. Multiple Inheritance
# 6. super()
# 7. Method Overriding
# 8. Best Practices
#
# ========================================================
# 8. MULTILEVEL INHERITANCE
# ========================================================

# This section focuses on multilevel inheritance.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

def display(value):
    print("Value:", value)

display("Python")

# ========================================================
# 9. MULTIPLE INHERITANCE
# ========================================================

# This section focuses on multiple inheritance.
# Use it to understand how the concept appears
# inside real programs.

# ========================================================
# SMALL DEMO
# ========================================================

numbers = [10, 20, 30]
for number in numbers:
    print(number)

# ========================================================
# 10. SUPER()
# ========================================================

# This section focuses on super().
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

# In real projects, Inheritance should be used with clean names,
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
# FILE: 18_inheritance.py
# ========================================================

# PART 3
# ========================================================
# PYTHON INHERITANCE - PRACTICE & REVISION
# ========================================================

# INDEX
#
# 1. What is Inheritance?
# 2. Parent and Child Classes
# 3. Single Inheritance
# 4. Multilevel Inheritance
# 5. Multiple Inheritance
# 6. super()
# 7. Method Overriding
# 8. Best Practices
#
# ========================================================
# 14. METHOD OVERRIDING
# ========================================================

# Method Overriding helps connect Inheritance to practical Python.
# Focus on the idea first, then practice the syntax.

# ========================================================
# 15. BEST PRACTICES
# ========================================================

# Best Practices helps connect Inheritance to practical Python.
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

# Q1. What is Inheritance?
# Answer:
# Inheritance is a Python topic used to write better programs.
#
# Q2. Why is Inheritance useful?
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

# - Inheritance is part of practical Python.
# - Learn the concept before memorizing syntax.
# - Practice with small examples.
# - Keep code readable.
# - Handle errors carefully.
# - Test edge cases.
# - Use meaningful names.
# - Prefer simple solutions.

# ========================================================
# END OF 18_inheritance.py
# ========================================================


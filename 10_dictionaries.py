# =========================================================
# FILE: 10_dictionaries.py
# PART 1
# =========================================================
#
# PYTHON DICTIONARIES
#
# INDEX
#
# 1. What is a Dictionary?
# 2. Why Dictionaries?
# 3. Creating Dictionaries
# 4. Dictionary Characteristics
# 5. Accessing Values
# 6. Adding & Updating Values
# 7. Dictionary Length
# 8. Membership Operators
#
# =========================================================
# 1. WHAT IS A DICTIONARY?
# =========================================================
#
# A dictionary is a mutable collection of key-value pairs.
#
# Syntax:
#
# dictionary = {
#     key1: value1,
#     key2: value2
# }
#
# Every key must be unique.
#

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

print(student)

print(type(student))

# Output
#
# {'name': 'Amit', 'age': 20, 'city': 'Mumbai'}
# <class 'dict'>

# =========================================================
# 2. WHY DICTIONARIES?
# =========================================================
#
# Lists store values by position.
#
# Dictionaries store values by key.
#

# Using List

student = [
    "Amit",
    20,
    "Mumbai"
]

print(student[0])

# What does index 0 represent?
#
# Not obvious.

# Using Dictionary

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

print(student["name"])

# Much more readable.

# =========================================================
# 3. CREATING DICTIONARIES
# =========================================================

# Empty Dictionary

student = {}

print(student)

# Dictionary with Data

employee = {
    "id": 101,
    "name": "Rahul",
    "salary": 50000
}

print(employee)

# =========================================================
# MIXED DATA TYPES
# =========================================================

data = {
    "name": "Python",
    "version": 3.12,
    "popular": True,
    "creator": None
}

print(data)

# =========================================================
# NESTED DICTIONARY
# =========================================================

student = {
    "name": "Amit",
    "marks": {
        "math": 90,
        "science": 95,
        "english": 88
    }
}

print(student)

# =========================================================
# USING dict()
# =========================================================

student = dict(
    name="Rahul",
    age=22,
    city="Delhi"
)

print(student)

# =========================================================
# FROM LIST OF TUPLES
# =========================================================

student = dict(
    [
        ("name", "Rohan"),
        ("age", 23)
    ]
)

print(student)

# =========================================================
# DUPLICATE KEYS
# =========================================================
#
# Duplicate keys are NOT allowed.
#
# The last value overwrites the previous one.
#

student = {
    "name": "Amit",
    "name": "Rahul"
}

print(student)

# Output
#
# {'name': 'Rahul'}

# =========================================================
# VALID KEY TYPES
# =========================================================
#
# Dictionary keys must be hashable.
#

data = {
    1: "Integer",
    3.14: "Float",
    True: "Boolean",
    "Python": "String",
    (1, 2): "Tuple"
}

print(data)

# =========================================================
# INVALID KEY TYPES
# =========================================================

# data = {
#     [1, 2]: "List"
# }

# TypeError

# Lists are mutable and cannot be keys.

# =========================================================
# 4. DICTIONARY CHARACTERISTICS
# =========================================================
#
# Dictionaries are:
#
# ✓ Mutable
# ✓ Dynamic
# ✓ Iterable
# ✓ Ordered (Python 3.7+)
# ✓ Key-Value Based
#
# Keys:
# -----
# Must be unique.
#
# Values:
# -------
# Can be duplicated.
#

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

print(student)

# =========================================================
# 5. ACCESSING VALUES
# =========================================================

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

print(student["name"])

print(student["age"])

print(student["city"])

# =========================================================
# KEY ERROR
# =========================================================

# print(student["salary"])

# KeyError

# =========================================================
# get()
# =========================================================
#
# Safe way to access values.
#

print(student.get("name"))

print(student.get("salary"))

# Output
#
# None

# =========================================================
# DEFAULT VALUE
# =========================================================

print(student.get("salary", 0))

print(student.get("country", "India"))

# =========================================================
# ACCESSING NESTED DICTIONARY
# =========================================================

student = {
    "name": "Amit",
    "marks": {
        "math": 90,
        "science": 95
    }
}

print(student["marks"])

print(student["marks"]["math"])

print(student["marks"]["science"])

# =========================================================
# 6. ADDING VALUES
# =========================================================

student = {
    "name": "Amit"
}

student["age"] = 20

print(student)

student["city"] = "Mumbai"

print(student)

# =========================================================
# UPDATING VALUES
# =========================================================

student["age"] = 25

print(student)

student["city"] = "Delhi"

print(student)

# =========================================================
# MULTIPLE UPDATES
# =========================================================

student.update(
    {
        "salary": 50000,
        "company": "OpenAI"
    }
)

print(student)

# =========================================================
# 7. DICTIONARY LENGTH
# =========================================================

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

print(len(student))

# =========================================================
# 8. MEMBERSHIP
# =========================================================
#
# Membership checks KEYS,
# not values.
#

student = {
    "name": "Amit",
    "age": 20
}

print("name" in student)

print("Amit" in student)

print("Amit" in student.values())

print("age" not in student)

# =========================================================
# ITERATING A DICTIONARY
# =========================================================

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

for key in student:
    print(key)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

employee = {
    "id": 101,
    "name": "Diwakar",
    "department": "Backend"
}

print(employee["name"])

employee["salary"] = 60000

print(employee)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Accessing a missing key.

student = {
    "name": "Amit"
}

# print(student["age"])

# KeyError

# Correct

print(student.get("age"))

# ---------------------------------------------------------

# Mistake 2
#
# Membership checks keys.

print("Amit" in student)

print("Amit" in student.values())

# ---------------------------------------------------------

# Mistake 3
#
# Using a mutable object as a key.

# data = {
#     [1, 2]: "List"
# }

# TypeError

# =========================================================
# FILE: 10_dictionaries.py
# PART 2
# =========================================================
#
# PYTHON DICTIONARIES
#
# INDEX
#
# 9. Dictionary Methods
# 10. Removing Items
# 11. Iterating Dictionaries
# 12. Nested Dictionaries
# 13. Copying Dictionaries
#
# =========================================================
# 9. DICTIONARY METHODS
# =========================================================

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

print(student)

# =========================================================
# keys()
# =========================================================
#
# Returns all dictionary keys.
#

print(student.keys())

print(list(student.keys()))

# =========================================================
# values()
# =========================================================
#
# Returns all dictionary values.
#

print(student.values())

print(list(student.values()))

# =========================================================
# items()
# =========================================================
#
# Returns key-value pairs.
#

print(student.items())

print(list(student.items()))

# =========================================================
# get()
# =========================================================

print(student.get("name"))

print(student.get("salary"))

print(student.get("salary", 0))

# =========================================================
# setdefault()
# =========================================================
#
# Returns the value if the key exists.
#
# Otherwise creates the key with
# the default value.
#

student.setdefault("country", "India")

print(student)

student.setdefault("age", 100)

print(student)

# =========================================================
# update()
# =========================================================
#
# Adds new keys or updates existing keys.
#

student.update(
    {
        "salary": 50000,
        "city": "Delhi"
    }
)

print(student)

# =========================================================
# fromkeys()
# =========================================================
#
# Creates a new dictionary.
#

keys = [
    "name",
    "age",
    "city"
]

new_student = dict.fromkeys(keys)

print(new_student)

new_student = dict.fromkeys(keys, "Unknown")

print(new_student)

# =========================================================
# 10. REMOVING ITEMS
# =========================================================

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai",
    "salary": 50000
}

# =========================================================
# pop()
# =========================================================
#
# Removes a key and returns its value.
#

removed = student.pop("salary")

print(removed)

print(student)

# =========================================================
# DEFAULT VALUE
# =========================================================

value = student.pop("country", "Not Found")

print(value)

# =========================================================
# popitem()
# =========================================================
#
# Removes the last inserted key-value pair.
#

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

item = student.popitem()

print(item)

print(student)

# =========================================================
# del
# =========================================================

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

del student["age"]

print(student)

# =========================================================
# clear()
# =========================================================

student.clear()

print(student)

# =========================================================
# 11. ITERATING DICTIONARIES
# =========================================================

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

# =========================================================
# Iterate Keys
# =========================================================

for key in student:
    print(key)

# =========================================================
# Iterate Values
# =========================================================

for value in student.values():
    print(value)

# =========================================================
# Iterate Items
# =========================================================

for item in student.items():
    print(item)

# =========================================================
# Key-Value Pair
# =========================================================

for key, value in student.items():
    print(key, ":", value)

# =========================================================
# enumerate()
# =========================================================

for index, item in enumerate(student.items()):
    print(index, item)

# =========================================================
# SORTING KEYS
# =========================================================

student = {
    "city": "Mumbai",
    "age": 20,
    "name": "Amit"
}

for key in sorted(student):
    print(key, student[key])

# =========================================================
# SORTING VALUES
# =========================================================

marks = {
    "Math": 90,
    "Science": 95,
    "English": 85
}

for value in sorted(marks.values()):
    print(value)

# =========================================================
# 12. NESTED DICTIONARIES
# =========================================================

students = {
    "student1": {
        "name": "Amit",
        "age": 20
    },
    "student2": {
        "name": "Rahul",
        "age": 21
    }
}

print(students)

# =========================================================
# ACCESSING NESTED VALUES
# =========================================================

print(students["student1"])

print(students["student1"]["name"])

print(students["student2"]["age"])

# =========================================================
# MODIFYING NESTED VALUES
# =========================================================

students["student1"]["age"] = 25

print(students)

# =========================================================
# ADDING NEW DATA
# =========================================================

students["student3"] = {
    "name": "Rohan",
    "age": 22
}

print(students)

# =========================================================
# ITERATING NESTED DICTIONARY
# =========================================================

for student_id, details in students.items():
    print(student_id)

    for key, value in details.items():
        print(key, ":", value)

    print()

# =========================================================
# 13. COPYING DICTIONARIES
# =========================================================

student = {
    "name": "Amit",
    "age": 20
}

# =========================================================
# copy()
# =========================================================

copy1 = student.copy()

print(copy1)

# =========================================================
# dict()
# =========================================================

copy2 = dict(student)

print(copy2)

# =========================================================
# ASSIGNMENT
# =========================================================

student1 = {
    "name": "Rahul"
}

student2 = student1

student2["age"] = 25

print(student1)

print(student2)

# =========================================================
# SHALLOW COPY
# =========================================================

student1 = {
    "name": "Amit"
}

student2 = student1.copy()

student2["age"] = 20

print(student1)

print(student2)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

employee = {
    "id": 101,
    "name": "Diwakar",
    "department": "Backend"
}

employee["salary"] = 70000

employee["city"] = "Mumbai"

print(employee)

# ---------------------------------------------------------

print(employee.keys())

print(employee.values())

print(employee.items())

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Using pop() on a missing key.

student = {
    "name": "Amit"
}

# student.pop("age")

# KeyError

# Correct

student.pop("age", None)

# ---------------------------------------------------------

# Mistake 2
#
# Confusing keys() and values().

print(student.keys())

print(student.values())

# ---------------------------------------------------------

# Mistake 3
#
# Assignment is not copying.

dict1 = {
    "name": "Amit"
}

dict2 = dict1

dict2["city"] = "Mumbai"

print(dict1)

# =========================================================
# FILE: 10_dictionaries.py
# PART 3
# =========================================================
#
# PYTHON DICTIONARIES
#
# INDEX
#
# 14. Dictionary Comprehension
# 15. Shallow Copy vs Deep Copy
# 16. Useful Built-in Functions
# 17. Practical Examples
# 18. Common Beginner Mistakes
# 19. Interview Questions
# 20. Quick Revision
#
# =========================================================
# 14. DICTIONARY COMPREHENSION
# =========================================================
#
# Dictionary comprehension provides a concise
# way to create dictionaries.
#
# Syntax:
#
# {
#     key: value
#     for item in iterable
# }
#

# =========================================================
# BASIC EXAMPLE
# =========================================================

numbers = {
    number: number ** 2
    for number in range(1, 6)
}

print(numbers)

# Output
#
# {
#     1:1,
#     2:4,
#     3:9,
#     4:16,
#     5:25
# }

# =========================================================
# SQUARES
# =========================================================

squares = {
    number: number ** 2
    for number in range(1, 11)
}

print(squares)

# =========================================================
# CUBES
# =========================================================

cubes = {
    number: number ** 3
    for number in range(1, 6)
}

print(cubes)

# =========================================================
# EVEN NUMBERS
# =========================================================

evens = {
    number: "Even"
    for number in range(10)
    if number % 2 == 0
}

print(evens)

# =========================================================
# ODD NUMBERS
# =========================================================

odds = {
    number: "Odd"
    for number in range(10)
    if number % 2 != 0
}

print(odds)

# =========================================================
# CONDITIONAL EXPRESSION
# =========================================================

numbers = {
    number:
    (
        "Even"
        if number % 2 == 0
        else "Odd"
    )
    for number in range(1, 6)
}

print(numbers)

# =========================================================
# LIST TO DICTIONARY
# =========================================================

names = [
    "Amit",
    "Rahul",
    "Rohan"
]

students = {
    index: name
    for index, name in enumerate(names, start=1)
}

print(students)

# =========================================================
# ZIP()
# =========================================================

subjects = [
    "Math",
    "Science",
    "English"
]

marks = [
    90,
    95,
    88
]

result = {
    subject: mark
    for subject, mark
    in zip(subjects, marks)
}

print(result)

# =========================================================
# STRING LENGTHS
# =========================================================

words = [
    "Python",
    "Java",
    "JavaScript"
]

lengths = {
    word: len(word)
    for word in words
}

print(lengths)

# =========================================================
# FILTERING
# =========================================================

marks = {
    "Amit": 95,
    "Rahul": 40,
    "Rohan": 85
}

passed = {
    name: mark
    for name, mark in marks.items()
    if mark >= 50
}

print(passed)

# =========================================================
# 15. SHALLOW COPY vs DEEP COPY
# =========================================================

import copy

# =========================================================
# ASSIGNMENT
# =========================================================

student1 = {
    "name": "Amit"
}

student2 = student1

student2["city"] = "Mumbai"

print(student1)

print(student2)

# =========================================================
# SHALLOW COPY
# =========================================================

student1 = {
    "name": "Rahul"
}

student2 = student1.copy()

student2["city"] = "Delhi"

print(student1)

print(student2)

# =========================================================
# SHALLOW COPY WITH NESTED DICTIONARY
# =========================================================

student1 = {
    "marks": {
        "math": 90
    }
}

student2 = student1.copy()

student2["marks"]["math"] = 100

print(student1)

print(student2)

# Inner dictionary is shared.

# =========================================================
# DEEP COPY
# =========================================================

student1 = {
    "marks": {
        "math": 90
    }
}

student2 = copy.deepcopy(student1)

student2["marks"]["math"] = 100

print(student1)

print(student2)

# =========================================================
# 16. USEFUL BUILT-IN FUNCTIONS
# =========================================================

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

print(len(student))

print(sorted(student))

print(list(student))

print(tuple(student))

print(dict(student))

# =========================================================
# enumerate()
# =========================================================

for index, item in enumerate(student.items()):
    print(index, item)

# =========================================================
# zip()
# =========================================================

keys = [
    "name",
    "age",
    "city"
]

values = [
    "Rahul",
    25,
    "Delhi"
]

employee = dict(zip(keys, values))

print(employee)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1
# Student Record

student = {
    "name": "Diwakar",
    "age": 22,
    "city": "Mumbai"
}

print(student)

# ---------------------------------------------------------

# Example 2
# Employee Database

employee = {
    "id": 101,
    "name": "Rahul",
    "department": "Backend",
    "salary": 70000
}

print(employee)

# ---------------------------------------------------------

# Example 3
# Counting Characters

text = "banana"

frequency = {}

for character in text:
    frequency[character] = (
        frequency.get(character, 0) + 1
    )

print(frequency)

# ---------------------------------------------------------

# Example 4
# Merge Dictionaries

dict1 = {
    "a": 1,
    "b": 2
}

dict2 = {
    "c": 3,
    "d": 4
}

merged = {
    **dict1,
    **dict2
}

print(merged)

# ---------------------------------------------------------

# Example 5
# Dictionary from Lists

subjects = [
    "Math",
    "Science"
]

marks = [
    90,
    95
]

result = dict(zip(subjects, marks))

print(result)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Accessing a missing key.

student = {
    "name": "Amit"
}

# student["age"]

# KeyError

# Correct

print(student.get("age"))

# ---------------------------------------------------------

# Mistake 2
#
# Membership checks keys.

print("name" in student)

print("Amit" in student)

print("Amit" in student.values())

# ---------------------------------------------------------

# Mistake 3
#
# Assignment is not copying.

dict1 = {
    "name": "Amit"
}

dict2 = dict1

dict2["city"] = "Mumbai"

print(dict1)

# ---------------------------------------------------------

# Mistake 4
#
# Shallow copy shares nested objects.

import copy

a = {
    "marks": {
        "math": 90
    }
}

b = a.copy()

b["marks"]["math"] = 100

print(a)

# ---------------------------------------------------------

# Mistake 5
#
# Forgetting duplicate keys overwrite.

student = {
    "name": "Amit",
    "name": "Rahul"
}

print(student)

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is a dictionary?
#
# Answer:
# A mutable collection of key-value pairs.
#
# ---------------------------------------------------------
#
# Q2. Are dictionary keys unique?
#
# Answer:
#
# Yes.
#
# ---------------------------------------------------------
#
# Q3. Can dictionary values be duplicated?
#
# Answer:
#
# Yes.
#
# ---------------------------------------------------------
#
# Q4. Difference between [] and get()?
#
# []
# ----
# Raises KeyError if the key is missing.
#
# get()
# -----
# Returns None or a default value.
#
# ---------------------------------------------------------
#
# Q5. Difference between keys(), values(), and items()?
#
# keys()
# -------
# Returns dictionary keys.
#
# values()
# ---------
# Returns dictionary values.
#
# items()
# --------
# Returns key-value pairs.
#
# ---------------------------------------------------------
#
# Q6. Difference between pop() and popitem()?
#
# pop()
# -----
# Removes a specified key.
#
# popitem()
# ----------
# Removes the last inserted key-value pair.
#
# ---------------------------------------------------------
#
# Q7. What is dictionary comprehension?
#
# Answer:
# A concise way to create dictionaries.
#
# ---------------------------------------------------------
#
# Q8. Difference between shallow copy and deep copy?
#
# Shallow Copy
# ------------
# Copies only the outer dictionary.
#
# Deep Copy
# ---------
# Copies the entire nested structure.
#
# ---------------------------------------------------------
#
# Q9. Can dictionary keys be mutable?
#
# Answer:
#
# No.
#
# Keys must be hashable.
#
# ---------------------------------------------------------
#
# Q10. How do you merge two dictionaries?
#
# Answer:
#
# merged = {**dict1, **dict2}
#
# or
#
# dict1.update(dict2)
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Dictionaries store key-value pairs.
#
# ✓ Dictionaries are mutable.
#
# ✓ Dictionary keys are unique.
#
# ✓ Dictionary values can be duplicated.
#
# ✓ Common access methods:
#   []
#   get()
#
# ✓ Common insertion methods:
#   update()
#   setdefault()
#
# ✓ Common removal methods:
#   pop()
#   popitem()
#   clear()
#   del
#
# ✓ Common iteration methods:
#   keys()
#   values()
#   items()
#
# ✓ Dictionary comprehension:
#   {key: value for ...}
#
# ✓ copy() performs a shallow copy.
#
# ✓ copy.deepcopy() performs a deep copy.
#
# ✓ Dictionaries are ideal for fast key-based lookups.
#
# =========================================================
# END OF 10_dictionaries.py
# =========================================================
# =========================================================
# FILE: 09_sets.py
# PART 1
# =========================================================
#
# PYTHON SETS
#
# INDEX
#
# 1. What is a Set?
# 2. Why Sets?
# 3. Creating Sets
# 4. Set Characteristics
# 5. Empty Set
# 6. Set Indexing
# 7. Iterating Sets
# 8. Adding Elements
#
# =========================================================
# 1. WHAT IS A SET?
# =========================================================
#
# A set is an unordered, mutable collection of
# unique (non-duplicate) elements.
#
# Sets are mainly used for:
#
# • Removing duplicates
# • Membership testing
# • Mathematical set operations
#
# Syntax:
#
# set_name = {value1, value2, value3}
#

numbers = {10, 20, 30, 40}

print(numbers)

print(type(numbers))

# Output
#
# {10, 20, 30, 40}
# <class 'set'>

# =========================================================
# 2. WHY SETS?
# =========================================================
#
# Without a set:
#

numbers = [
    10,
    20,
    20,
    30,
    30,
    40
]

print(numbers)

# Remove duplicates

unique_numbers = set(numbers)

print(unique_numbers)

# =========================================================
# 3. CREATING SETS
# =========================================================

# Integer Set

numbers = {
    10,
    20,
    30
}

# String Set

languages = {
    "Python",
    "Java",
    "Go"
}

# Float Set

prices = {
    10.5,
    20.5,
    30.5
}

# Boolean Set

status = {
    True,
    False
}

print(numbers)
print(languages)
print(prices)
print(status)

# =========================================================
# MIXED DATA TYPES
# =========================================================

data = {
    10,
    20.5,
    "Python",
    True
}

print(data)

# =========================================================
# DUPLICATE VALUES
# =========================================================

numbers = {
    10,
    20,
    20,
    30,
    30,
    40
}

print(numbers)

# Output
#
# {10, 20, 30, 40}

# =========================================================
# USING set() CONSTRUCTOR
# =========================================================

letters = set("Python")

print(letters)

numbers = set([1, 2, 2, 3])

print(numbers)

# =========================================================
# 4. SET CHARACTERISTICS
# =========================================================
#
# Sets are:
#
# ✓ Unordered
# ✓ Mutable
# ✓ Iterable
# ✓ Unique Elements
# ✓ Unindexed
#
# Sets DO NOT support:
#
# ✗ Indexing
# ✗ Slicing
#

# =========================================================
# EMPTY SET
# =========================================================

empty = set()

print(empty)

print(type(empty))

# =========================================================
# COMMON MISTAKE
# =========================================================

empty = {}

print(type(empty))

# Output
#
# <class 'dict'>

# {} creates a dictionary,
# not a set.

# =========================================================
# 5. UNORDERED NATURE
# =========================================================
#
# The order of elements is not guaranteed.
#

numbers = {
    5,
    1,
    8,
    3,
    9
}

print(numbers)

# Output may differ.

# =========================================================
# 6. NO INDEXING
# =========================================================

numbers = {
    10,
    20,
    30
}

# print(numbers[0])

# TypeError

# =========================================================
# NO SLICING
# =========================================================

# print(numbers[1:3])

# TypeError

# =========================================================
# MEMBERSHIP
# =========================================================

numbers = {
    10,
    20,
    30,
    40
}

print(20 in numbers)

print(100 in numbers)

print(100 not in numbers)

# =========================================================
# 7. ITERATING A SET
# =========================================================

languages = {
    "Python",
    "Java",
    "Go"
}

for language in languages:
    print(language)

# Order is not guaranteed.

# =========================================================
# CONVERTING TO LIST
# =========================================================

numbers = {
    10,
    20,
    30
}

numbers_list = list(numbers)

print(numbers_list)

# =========================================================
# SORTING A SET
# =========================================================

numbers = {
    50,
    20,
    40,
    10
}

print(sorted(numbers))

# sorted() returns a list.

# =========================================================
# SET LENGTH
# =========================================================

numbers = {
    10,
    20,
    30
}

print(len(numbers))

# =========================================================
# 8. ADDING ELEMENTS
# =========================================================

numbers = {
    10,
    20
}

# =========================================================
# add()
# =========================================================
#
# Adds one element.
#

numbers.add(30)

print(numbers)

numbers.add(40)

print(numbers)

# =========================================================
# DUPLICATE ADD
# =========================================================

numbers.add(20)

print(numbers)

# No duplicate will be added.

# =========================================================
# update()
# =========================================================
#
# Adds multiple elements.
#

numbers.update(
    [
        50,
        60,
        70
    ]
)

print(numbers)

# =========================================================
# update() WITH TUPLE
# =========================================================

numbers.update(
    (
        80,
        90
    )
)

print(numbers)

# =========================================================
# update() WITH STRING
# =========================================================

letters = {
    "A",
    "B"
}

letters.update("CD")

print(letters)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

fruits = {
    "Apple",
    "Banana"
}

fruits.add("Mango")

print(fruits)

students = {
    "Amit",
    "Rahul"
}

students.update(
    [
        "Rohan",
        "Diwakar"
    ]
)

print(students)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# {} creates a dictionary.

empty = {}

print(type(empty))

# Correct

empty = set()

print(type(empty))

# ---------------------------------------------------------

# Mistake 2
#
# Expecting duplicate values.

numbers = {
    1,
    1,
    1,
    2,
    2
}

print(numbers)

# ---------------------------------------------------------

# Mistake 3
#
# Using indexing.

# numbers[0]

# TypeError


# =========================================================
# FILE: 09_sets.py
# PART 2
# =========================================================
#
# PYTHON SETS
#
# INDEX
#
# 9. Removing Elements
# 10. Set Operations
# 11. Set Methods
# 12. Frozen Set
#
# =========================================================
# 9. REMOVING ELEMENTS
# =========================================================

numbers = {
    10,
    20,
    30,
    40,
    50
}

print(numbers)

# =========================================================
# remove()
# =========================================================
#
# Removes the specified element.
#
# Raises KeyError if the element
# does not exist.
#

numbers.remove(20)

print(numbers)

# numbers.remove(100)

# KeyError

# =========================================================
# discard()
# =========================================================
#
# Removes the specified element.
#
# Does NOT raise an error if the
# element does not exist.
#

numbers.discard(30)

print(numbers)

numbers.discard(100)

print(numbers)

# =========================================================
# pop()
# =========================================================
#
# Removes and returns a random element.
#
# Since sets are unordered,
# you cannot predict which element
# will be removed.
#

numbers = {
    10,
    20,
    30
}

removed = numbers.pop()

print(removed)

print(numbers)

# =========================================================
# clear()
# =========================================================
#
# Removes all elements.
#

numbers = {
    10,
    20,
    30
}

numbers.clear()

print(numbers)

# Output
#
# set()

# =========================================================
# del
# =========================================================

numbers = {
    1,
    2,
    3
}

del numbers

# print(numbers)

# NameError

# =========================================================
# remove() vs discard()
# =========================================================

numbers = {
    10,
    20,
    30
}

numbers.discard(100)

print(numbers)

# numbers.remove(100)

# KeyError

# =========================================================
# 10. SET OPERATIONS
# =========================================================
#
# Set operations are based on
# mathematical set theory.
#

set1 = {
    1,
    2,
    3,
    4
}

set2 = {
    3,
    4,
    5,
    6
}

print(set1)

print(set2)

# =========================================================
# UNION
# =========================================================
#
# Combines both sets.
#

print(set1 | set2)

print(set1.union(set2))

# Output
#
# {1, 2, 3, 4, 5, 6}

# =========================================================
# INTERSECTION
# =========================================================
#
# Common elements.
#

print(set1 & set2)

print(set1.intersection(set2))

# Output
#
# {3, 4}

# =========================================================
# DIFFERENCE
# =========================================================
#
# Elements present in first set
# but not in second.
#

print(set1 - set2)

print(set2 - set1)

print(set1.difference(set2))

# =========================================================
# SYMMETRIC DIFFERENCE
# =========================================================
#
# Elements that are unique
# to each set.
#

print(set1 ^ set2)

print(set1.symmetric_difference(set2))

# Output
#
# {1, 2, 5, 6}

# =========================================================
# UPDATE OPERATIONS
# =========================================================

set1 = {
    1,
    2,
    3
}

set2 = {
    3,
    4,
    5
}

# =========================================================
# update()
# =========================================================

set1.update(set2)

print(set1)

# =========================================================
# intersection_update()
# =========================================================

set1 = {
    1,
    2,
    3,
    4
}

set2 = {
    3,
    4,
    5,
    6
}

set1.intersection_update(set2)

print(set1)

# =========================================================
# difference_update()
# =========================================================

set1 = {
    1,
    2,
    3,
    4
}

set2 = {
    3,
    4
}

set1.difference_update(set2)

print(set1)

# =========================================================
# symmetric_difference_update()
# =========================================================

set1 = {
    1,
    2,
    3
}

set2 = {
    3,
    4,
    5
}

set1.symmetric_difference_update(set2)

print(set1)

# =========================================================
# 11. SET METHODS
# =========================================================

set1 = {
    1,
    2,
    3
}

set2 = {
    1,
    2,
    3,
    4,
    5
}

set3 = {
    10,
    20
}

# =========================================================
# issubset()
# =========================================================

print(set1.issubset(set2))

print(set2.issubset(set1))

# =========================================================
# issuperset()
# =========================================================

print(set2.issuperset(set1))

print(set1.issuperset(set2))

# =========================================================
# isdisjoint()
# =========================================================

print(set1.isdisjoint(set3))

print(set1.isdisjoint(set2))

# =========================================================
# copy()
# =========================================================

copy_set = set1.copy()

print(copy_set)

# =========================================================
# 12. FROZENSET
# =========================================================
#
# frozenset is an immutable version
# of a set.
#

numbers = frozenset(
    [
        10,
        20,
        30
    ]
)

print(numbers)

print(type(numbers))

# =========================================================
# MEMBERSHIP
# =========================================================

print(20 in numbers)

print(100 in numbers)

# =========================================================
# IMMUTABLE
# =========================================================

# numbers.add(40)

# AttributeError

# numbers.remove(10)

# AttributeError

# =========================================================
# FROZENSET AS DICTIONARY KEY
# =========================================================

data = {
    frozenset(
        [
            1,
            2
        ]
    ): "Python"
}

print(data)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

python_students = {
    "Amit",
    "Rahul",
    "Diwakar"
}

java_students = {
    "Rahul",
    "Rohan"
}

print(
    python_students &
    java_students
)

print(
    python_students |
    java_students
)

print(
    python_students -
    java_students
)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Using remove() when the element
# may not exist.

numbers = {
    1,
    2,
    3
}

numbers.discard(10)

print(numbers)

# ---------------------------------------------------------

# Mistake 2
#
# Expecting pop() to remove
# the first element.

numbers = {
    10,
    20,
    30
}

print(numbers.pop())

# The removed value is arbitrary.

# ---------------------------------------------------------

# Mistake 3
#
# Forgetting that union()
# returns a new set.

set1 = {
    1,
    2
}

set2 = {
    2,
    3
}

print(set1.union(set2))

print(set1)


# =========================================================
# FILE: 09_sets.py
# PART 3
# =========================================================
#
# PYTHON SETS
#
# INDEX
#
# 13. Set Comprehension
# 14. Set vs List vs Tuple
# 15. Practical Examples
# 16. Common Beginner Mistakes
# 17. Interview Questions
# 18. Quick Revision
#
# =========================================================
# 13. SET COMPREHENSION
# =========================================================
#
# Set comprehension provides a concise way
# to create sets.
#
# Syntax:
#
# {expression for item in iterable}
#

# =========================================================
# BASIC EXAMPLE
# =========================================================

numbers = {
    number
    for number in range(1, 6)
}

print(numbers)

# Output
#
# {1, 2, 3, 4, 5}

# =========================================================
# SQUARES
# =========================================================

squares = {
    number ** 2
    for number in range(1, 6)
}

print(squares)

# =========================================================
# EVEN NUMBERS
# =========================================================

evens = {
    number
    for number in range(20)
    if number % 2 == 0
}

print(evens)

# =========================================================
# ODD NUMBERS
# =========================================================

odds = {
    number
    for number in range(20)
    if number % 2 != 0
}

print(odds)

# =========================================================
# STRING TO UPPERCASE
# =========================================================

languages = {
    "python",
    "java",
    "go"
}

upper_languages = {
    language.upper()
    for language in languages
}

print(upper_languages)

# =========================================================
# STRING LENGTHS
# =========================================================

words = {
    "Python",
    "Java",
    "JavaScript"
}

lengths = {
    len(word)
    for word in words
}

print(lengths)

# =========================================================
# REMOVE DUPLICATES
# =========================================================

numbers = [
    10,
    20,
    20,
    30,
    30,
    40
]

unique_numbers = {
    number
    for number in numbers
}

print(unique_numbers)

# =========================================================
# FILTERING
# =========================================================

numbers = {
    10,
    15,
    20,
    25,
    30
}

greater_than_15 = {
    number
    for number in numbers
    if number > 15
}

print(greater_than_15)

# =========================================================
# 14. SET vs LIST vs TUPLE
# =========================================================
#
# +----------------+-----------+----------+----------+
# | Feature        | List      | Tuple    | Set      |
# +----------------+-----------+----------+----------+
# | Ordered        | Yes       | Yes      | No       |
# | Mutable        | Yes       | No       | Yes      |
# | Indexed        | Yes       | Yes      | No       |
# | Duplicates     | Yes       | Yes      | No       |
# | Slicing        | Yes       | Yes      | No       |
# | Hashable       | No        | Yes*     | No       |
# +----------------+-----------+----------+----------+
#
# *Tuple is hashable only if all its elements
# are hashable.
#

list_data = [1, 2, 2, 3]

tuple_data = (1, 2, 2, 3)

set_data = {
    1,
    2,
    2,
    3
}

print(list_data)

print(tuple_data)

print(set_data)

# =========================================================
# WHEN TO USE A LIST
# =========================================================
#
# • Ordered data
# • Frequent updates
# • Indexing required
#

shopping_cart = [
    "Milk",
    "Bread",
    "Butter"
]

print(shopping_cart)

# =========================================================
# WHEN TO USE A TUPLE
# =========================================================
#
# • Fixed data
# • Coordinates
# • Configuration
#

coordinate = (
    10,
    20
)

print(coordinate)

# =========================================================
# WHEN TO USE A SET
# =========================================================
#
# • Remove duplicates
# • Membership testing
# • Mathematical operations
#

numbers = {
    1,
    2,
    3
}

print(numbers)

# =========================================================
# PERFORMANCE
# =========================================================
#
# Membership testing in sets is generally
# much faster than lists and tuples.
#

numbers_list = list(range(1000))

numbers_set = set(range(1000))

print(500 in numbers_list)

print(500 in numbers_set)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1
# Remove Duplicate Names

names = [
    "Amit",
    "Rahul",
    "Amit",
    "Rohan",
    "Rahul"
]

unique_names = list(set(names))

print(unique_names)

# ---------------------------------------------------------

# Example 2
# Common Subjects

student1 = {
    "Python",
    "Java",
    "SQL"
}

student2 = {
    "Python",
    "MongoDB",
    "SQL"
}

common = student1.intersection(student2)

print(common)

# ---------------------------------------------------------

# Example 3
# All Subjects

subjects = student1.union(student2)

print(subjects)

# ---------------------------------------------------------

# Example 4
# Unique Subjects

print(student1.symmetric_difference(student2))

# ---------------------------------------------------------

# Example 5
# Membership Check

allowed_users = {
    "amit",
    "rahul",
    "diwakar"
}

username = "diwakar"

if username in allowed_users:
    print("Access Granted")
else:
    print("Access Denied")

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# {} creates a dictionary,
# not a set.

empty = {}

print(type(empty))

# Correct

empty = set()

print(type(empty))

# ---------------------------------------------------------

# Mistake 2
#
# Trying to access by index.

numbers = {
    10,
    20,
    30
}

# numbers[0]

# TypeError

# ---------------------------------------------------------

# Mistake 3
#
# Expecting duplicate values.

numbers = {
    1,
    1,
    1,
    2
}

print(numbers)

# ---------------------------------------------------------

# Mistake 4
#
# Confusing remove() and discard().

numbers = {
    1,
    2,
    3
}

numbers.discard(100)

print(numbers)

# remove(100)
#
# KeyError

# ---------------------------------------------------------

# Mistake 5
#
# Assuming sorted() returns a set.

numbers = {
    3,
    2,
    1
}

print(sorted(numbers))

print(type(sorted(numbers)))

# sorted() returns a list.

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is a set?
#
# Answer:
# A set is an unordered, mutable collection
# of unique elements.
#
# ---------------------------------------------------------
#
# Q2. Does a set allow duplicate values?
#
# Answer:
#
# No.
#
# ---------------------------------------------------------
#
# Q3. Can a set be indexed?
#
# Answer:
#
# No.
#
# ---------------------------------------------------------
#
# Q4. Difference between remove() and discard()?
#
# remove()
# --------
# Raises KeyError if the element does not exist.
#
# discard()
# ---------
# Does not raise an error.
#
# ---------------------------------------------------------
#
# Q5. Difference between union() and update()?
#
# union()
# -------
# Returns a new set.
#
# update()
# --------
# Modifies the original set.
#
# ---------------------------------------------------------
#
# Q6. Difference between pop() in a list and a set?
#
# List:
# Removes by index (default: last element).
#
# Set:
# Removes an arbitrary element.
#
# ---------------------------------------------------------
#
# Q7. What is a frozenset?
#
# Answer:
#
# An immutable version of a set.
#
# ---------------------------------------------------------
#
# Q8. Can a set contain another set?
#
# Answer:
#
# No.
#
# Sets are mutable and therefore unhashable.
#
# Use frozenset if needed.
#
# ---------------------------------------------------------
#
# Q9. Which data structure is fastest
# for membership testing?
#
# Answer:
#
# Set
#
# ---------------------------------------------------------
#
# Q10. What is set comprehension?
#
# Answer:
#
# A concise way to create sets using
# a single expression.
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Sets are unordered.
#
# ✓ Sets are mutable.
#
# ✓ Sets do not allow duplicates.
#
# ✓ Sets do not support indexing or slicing.
#
# ✓ Common insertion methods:
#   add()
#   update()
#
# ✓ Common removal methods:
#   remove()
#   discard()
#   pop()
#   clear()
#
# ✓ Mathematical operations:
#   union()
#   intersection()
#   difference()
#   symmetric_difference()
#
# ✓ Useful methods:
#   issubset()
#   issuperset()
#   isdisjoint()
#   copy()
#
# ✓ frozenset() creates an immutable set.
#
# ✓ Set comprehension uses:
#   {expression for item in iterable}
#
# ✓ Sets are ideal for removing duplicates
#   and fast membership testing.
#
# =========================================================
# END OF 09_sets.py
# =========================================================
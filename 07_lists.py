# =========================================================
# FILE: 07_lists.py
# PART 1
# =========================================================
#
# PYTHON LISTS
#
# INDEX
#
# 1. What is a List?
# 2. Why Lists?
# 3. Creating Lists
# 4. List Characteristics
# 5. List Indexing
# 6. Negative Indexing
# 7. List Slicing
# 8. List Mutability
#
# =========================================================
# 1. WHAT IS A LIST?
# =========================================================
#
# A list is an ordered, mutable collection that can store
# multiple values in a single variable.
#
# Lists are one of the most commonly used data structures
# in Python.
#
# Syntax:
#
# list_name = [item1, item2, item3]
#

numbers = [10, 20, 30, 40]

print(numbers)

print(type(numbers))

# Output
#
# [10, 20, 30, 40]
# <class 'list'>

# =========================================================
# 2. WHY LISTS?
# =========================================================
#
# Without a list:
#

student1 = "Amit"
student2 = "Rahul"
student3 = "Rohan"

print(student1)
print(student2)
print(student3)

# With a list:
#

students = ["Amit", "Rahul", "Rohan"]

print(students)

# Lists make data easier to:
#
# • Store
# • Access
# • Modify
# • Search
# • Sort
# • Iterate

# =========================================================
# 3. CREATING LISTS
# =========================================================

# Empty list

empty = []

print(empty)

# Integer list

numbers = [10, 20, 30]

# Float list

prices = [10.5, 20.8, 30.25]

# String list

names = ["Amit", "Rahul", "Rohan"]

# Boolean list

status = [True, False, True]

print(numbers)
print(prices)
print(names)
print(status)

# =========================================================
# MIXED DATA TYPES
# =========================================================

data = [
    10,
    20.5,
    "Python",
    True,
    None
]

print(data)

# =========================================================
# NESTED LIST
# =========================================================

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(matrix)

# =========================================================
# USING list() CONSTRUCTOR
# =========================================================

letters = list("Python")

print(letters)

numbers = list(range(1, 6))

print(numbers)

# =========================================================
# 4. LIST CHARACTERISTICS
# =========================================================
#
# Lists are:
#
# ✓ Ordered
# ✓ Mutable
# ✓ Dynamic
# ✓ Iterable
# ✓ Indexed
# ✓ Allow Duplicates
# ✓ Allow Mixed Data Types
#

sample = [10, 20, 20, 30]

print(sample)

# =========================================================
# 5. LIST INDEXING
# =========================================================
#
# Positive Indexing
#

fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange"
]

print(fruits[0])

print(fruits[1])

print(fruits[2])

print(fruits[3])

# =========================================================
# NEGATIVE INDEXING
# =========================================================
#
# Apple Banana Mango Orange
#  -4     -3    -2     -1
#

print(fruits[-1])

print(fruits[-2])

print(fruits[-3])

print(fruits[-4])

# =========================================================
# INDEX ERROR
# =========================================================

# print(fruits[10])

# IndexError

# =========================================================
# ACCESSING FIRST & LAST ELEMENT
# =========================================================

print(fruits[0])

print(fruits[-1])

# =========================================================
# 6. LIST SLICING
# =========================================================
#
# Syntax
#
# list[start : stop : step]
#

numbers = [
    10,
    20,
    30,
    40,
    50,
    60,
    70
]

print(numbers[0:3])

print(numbers[2:5])

print(numbers[:4])

print(numbers[4:])

print(numbers[:])

# =========================================================
# NEGATIVE SLICING
# =========================================================

print(numbers[-3:])

print(numbers[:-2])

print(numbers[-5:-1])

# =========================================================
# STEP VALUE
# =========================================================

print(numbers[::2])

print(numbers[1::2])

print(numbers[::-1])

# =========================================================
# COPYING A LIST
# =========================================================

copy = numbers[:]

print(copy)

# =========================================================
# 7. LIST MUTABILITY
# =========================================================
#
# Lists are mutable.
#
# Elements can be changed after creation.
#

numbers = [10, 20, 30]

numbers[1] = 200

print(numbers)

# Output
#
# [10, 200, 30]

# =========================================================
# MODIFYING MULTIPLE ELEMENTS
# =========================================================

numbers = [
    10,
    20,
    30,
    40,
    50
]

numbers[1:4] = [
    200,
    300,
    400
]

print(numbers)

# =========================================================
# REPLACING USING SLICE
# =========================================================

letters = [
    "A",
    "B",
    "C",
    "D"
]

letters[1:3] = [
    "X",
    "Y"
]

print(letters)

# =========================================================
# LIST LENGTH
# =========================================================

numbers = [10, 20, 30]

print(len(numbers))

# =========================================================
# MEMBERSHIP
# =========================================================

numbers = [10, 20, 30, 40]

print(20 in numbers)

print(100 in numbers)

print(100 not in numbers)

# =========================================================
# ITERATING THROUGH A LIST
# =========================================================

languages = [
    "Python",
    "Java",
    "Go"
]

for language in languages:
    print(language)

# =========================================================
# USING range()
# =========================================================

for index in range(len(languages)):
    print(index, languages[index])

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

cities = [
    "Mumbai",
    "Delhi",
    "Pune",
    "Chennai"
]

print(cities[0])

print(cities[-1])

print(cities[::-1])

print(len(cities))

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Confusing list indexing.

numbers = [10, 20, 30]

print(numbers[0])

# Not numbers[1]

# ---------------------------------------------------------

# Mistake 2
#
# Index out of range.

# print(numbers[10])

# ---------------------------------------------------------

# Mistake 3
#
# Forgetting slicing excludes
# the ending index.

print(numbers[0:2])

# Output
#
# [10, 20]

# =========================================================
# FILE: 07_lists.py
# PART 2
# =========================================================
#
# INDEX
#
# 8. Adding Elements
# 9. Removing Elements
# 10. List Methods
# 11. Sorting Lists
# 12. Reversing Lists
# 13. Copying Lists
#
# =========================================================
# 8. ADDING ELEMENTS
# =========================================================

numbers = [10, 20, 30]

print(numbers)

# =========================================================
# append()
# =========================================================
#
# Adds one element at the end.
#

numbers.append(40)

print(numbers)

numbers.append(50)

print(numbers)

# =========================================================
# append() WITH DIFFERENT DATA TYPES
# =========================================================

data = [10, 20]

data.append("Python")

data.append(True)

print(data)

# =========================================================
# append() WITH LIST
# =========================================================

numbers = [1, 2, 3]

numbers.append([4, 5])

print(numbers)

# Output
#
# [1, 2, 3, [4, 5]]

# =========================================================
# extend()
# =========================================================
#
# Adds multiple elements from another iterable.
#

numbers = [10, 20]

numbers.extend([30, 40])

print(numbers)

# =========================================================
# extend() WITH TUPLE
# =========================================================

numbers = [1, 2]

numbers.extend((3, 4))

print(numbers)

# =========================================================
# extend() WITH STRING
# =========================================================

letters = ["A", "B"]

letters.extend("CD")

print(letters)

# Output
#
# ['A', 'B', 'C', 'D']

# =========================================================
# append() vs extend()
# =========================================================

list1 = [1, 2]

list1.append([3, 4])

print(list1)

# Output
#
# [1, 2, [3, 4]]

list2 = [1, 2]

list2.extend([3, 4])

print(list2)

# Output
#
# [1, 2, 3, 4]

# =========================================================
# insert()
# =========================================================
#
# Inserts an element at a specific index.
#

numbers = [10, 20, 30]

numbers.insert(1, 15)

print(numbers)

numbers.insert(0, 5)

print(numbers)

numbers.insert(100, 40)

print(numbers)

# =========================================================
# 9. REMOVING ELEMENTS
# =========================================================

numbers = [10, 20, 30, 40, 50]

# =========================================================
# remove()
# =========================================================
#
# Removes the first matching value.
#

numbers.remove(30)

print(numbers)

# =========================================================
# remove() ERROR
# =========================================================

# numbers.remove(100)

# ValueError

# =========================================================
# pop()
# =========================================================
#
# Removes and returns an element.
#

numbers = [10, 20, 30, 40]

removed = numbers.pop()

print(removed)

print(numbers)

# =========================================================
# pop(index)
# =========================================================

numbers = [10, 20, 30, 40]

removed = numbers.pop(1)

print(removed)

print(numbers)

# =========================================================
# pop() ERROR
# =========================================================

# numbers.pop(100)

# IndexError

# =========================================================
# del
# =========================================================

numbers = [10, 20, 30, 40]

del numbers[1]

print(numbers)

# Delete Slice

numbers = [1, 2, 3, 4, 5, 6]

del numbers[2:5]

print(numbers)

# =========================================================
# clear()
# =========================================================
#
# Removes all elements.
#

numbers = [10, 20, 30]

numbers.clear()

print(numbers)

# Output
#
# []

# =========================================================
# 10. LIST METHODS
# =========================================================

numbers = [40, 10, 50, 20, 30]

# =========================================================
# count()
# =========================================================

print(numbers.count(10))

numbers = [1, 2, 2, 3, 2]

print(numbers.count(2))

# =========================================================
# index()
# =========================================================

numbers = [10, 20, 30, 40]

print(numbers.index(20))

# numbers.index(100)

# ValueError

# =========================================================
# len()
# =========================================================

numbers = [10, 20, 30]

print(len(numbers))

# =========================================================
# max()
# =========================================================

print(max(numbers))

# =========================================================
# min()
# =========================================================

print(min(numbers))

# =========================================================
# sum()
# =========================================================

print(sum(numbers))

# =========================================================
# any()
# =========================================================

print(any([0, 0, 1]))

print(any([0, 0, 0]))

# =========================================================
# all()
# =========================================================

print(all([1, 2, 3]))

print(all([1, 0, 3]))

# =========================================================
# 11. SORTING LISTS
# =========================================================

numbers = [50, 10, 30, 20, 40]

# =========================================================
# sort()
# =========================================================
#
# Sorts the original list.
#

numbers.sort()

print(numbers)

# =========================================================
# Descending Order
# =========================================================

numbers.sort(reverse=True)

print(numbers)

# =========================================================
# sorted()
# =========================================================
#
# Returns a new sorted list.
#

numbers = [30, 10, 20]

new_list = sorted(numbers)

print(new_list)

print(numbers)

# =========================================================
# SORTING STRINGS
# =========================================================

languages = [
    "Java",
    "Python",
    "Go",
    "C"
]

languages.sort()

print(languages)

# =========================================================
# SORT BY LENGTH
# =========================================================

languages = [
    "Python",
    "C",
    "Java",
    "JavaScript"
]

languages.sort(key=len)

print(languages)

# =========================================================
# 12. REVERSING LISTS
# =========================================================

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

# =========================================================
# REVERSED()
# =========================================================

numbers = [1, 2, 3, 4]

result = reversed(numbers)

print(list(result))

# =========================================================
# SLICING
# =========================================================

numbers = [1, 2, 3, 4]

print(numbers[::-1])

# =========================================================
# 13. COPYING LISTS
# =========================================================

numbers = [10, 20, 30]

# =========================================================
# copy()
# =========================================================

copy1 = numbers.copy()

print(copy1)

# =========================================================
# Slice Copy
# =========================================================

copy2 = numbers[:]

print(copy2)

# =========================================================
# list()
# =========================================================

copy3 = list(numbers)

print(copy3)

# =========================================================
# SHALLOW COPY EXAMPLE
# =========================================================

list1 = [10, 20]

list2 = list1

list2.append(30)

print(list1)

print(list2)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

students = [
    "Amit",
    "Rahul",
    "Rohan"
]

students.append("Diwakar")

print(students)

students.remove("Rahul")

print(students)

students.sort()

print(students)

students.reverse()

print(students)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# append() vs extend()

numbers = [1, 2]

numbers.append([3, 4])

print(numbers)

# ---------------------------------------------------------

numbers = [1, 2]

numbers.extend([3, 4])

print(numbers)

# ---------------------------------------------------------

# Mistake 2
#
# sort() returns None.

numbers = [3, 2, 1]

result = numbers.sort()

print(result)

print(numbers)

# ---------------------------------------------------------

# Mistake 3
#
# reverse() changes the original list.

numbers = [1, 2, 3]

numbers.reverse()

print(numbers)

# =========================================================
# FILE: 07_lists.py
# PART 3
# =========================================================
#
# INDEX
#
# 14. Nested Lists
# 15. List Comprehension
# 16. Shallow Copy vs Deep Copy
# 17. Useful Built-in Functions
# 18. Practical Examples
# 19. Common Beginner Mistakes
# 20. Interview Questions
# 21. Quick Revision
#
# =========================================================
# 14. NESTED LISTS
# =========================================================
#
# A nested list is a list that contains one or more lists
# as its elements.
#

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix)

# =========================================================
# ACCESSING NESTED LIST ELEMENTS
# =========================================================

print(matrix[0])

print(matrix[1])

print(matrix[2])

# Access individual elements

print(matrix[0][0])

print(matrix[1][2])

print(matrix[2][1])

# =========================================================
# MODIFYING NESTED LISTS
# =========================================================

matrix[1][1] = 500

print(matrix)

# =========================================================
# ITERATING THROUGH A NESTED LIST
# =========================================================

for row in matrix:
    print(row)

print()

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# =========================================================
# MULTIPLICATION TABLE EXAMPLE
# =========================================================

table = [
    [1, 2],
    [3, 4]
]

for row in table:
    for value in row:
        print(value, end=" ")
    print()

# =========================================================
# 15. LIST COMPREHENSION
# =========================================================
#
# List comprehension provides a concise way
# to create lists.
#
# Syntax:
#
# [expression for item in iterable]
#

# =========================================================
# BASIC EXAMPLE
# =========================================================

numbers = [x for x in range(1, 6)]

print(numbers)

# =========================================================
# SQUARES
# =========================================================

squares = [x ** 2 for x in range(1, 6)]

print(squares)

# Output
#
# [1, 4, 9, 16, 25]

# =========================================================
# CUBES
# =========================================================

cubes = [x ** 3 for x in range(1, 6)]

print(cubes)

# =========================================================
# EVEN NUMBERS
# =========================================================

evens = [x for x in range(20) if x % 2 == 0]

print(evens)

# =========================================================
# ODD NUMBERS
# =========================================================

odds = [x for x in range(20) if x % 2 != 0]

print(odds)

# =========================================================
# STRING TO UPPERCASE
# =========================================================

languages = [
    "python",
    "java",
    "go"
]

upper_languages = [
    language.upper()
    for language in languages
]

print(upper_languages)

# =========================================================
# STRING LENGTHS
# =========================================================

words = [
    "Python",
    "Java",
    "JavaScript"
]

lengths = [
    len(word)
    for word in words
]

print(lengths)

# =========================================================
# FILTERING
# =========================================================

numbers = [10, 15, 20, 25, 30]

greater = [
    number
    for number in numbers
    if number > 15
]

print(greater)

# =========================================================
# CONDITIONAL EXPRESSION
# =========================================================

numbers = [1, 2, 3, 4, 5]

result = [
    "Even"
    if number % 2 == 0
    else "Odd"
    for number in numbers
]

print(result)

# =========================================================
# NESTED LIST COMPREHENSION
# =========================================================

matrix = [
    [1, 2],
    [3, 4]
]

flatten = [
    value
    for row in matrix
    for value in row
]

print(flatten)

# =========================================================
# 16. SHALLOW COPY vs DEEP COPY
# =========================================================

import copy

# =========================================================
# ASSIGNMENT
# =========================================================

list1 = [10, 20, 30]

list2 = list1

list2.append(40)

print(list1)

print(list2)

# Both variables point to the same list.

# =========================================================
# SHALLOW COPY
# =========================================================

list1 = [10, 20, 30]

list2 = list1.copy()

list2.append(40)

print(list1)

print(list2)

# =========================================================
# SHALLOW COPY WITH NESTED LIST
# =========================================================

list1 = [
    [1, 2],
    [3, 4]
]

list2 = list1.copy()

list2[0][0] = 100

print(list1)

print(list2)

# Inner list is still shared.

# =========================================================
# DEEP COPY
# =========================================================

list1 = [
    [1, 2],
    [3, 4]
]

list2 = copy.deepcopy(list1)

list2[0][0] = 999

print(list1)

print(list2)

# Deep copy creates completely
# independent objects.

# =========================================================
# 17. USEFUL BUILT-IN FUNCTIONS
# =========================================================

numbers = [30, 10, 40, 20]

print(len(numbers))

print(max(numbers))

print(min(numbers))

print(sum(numbers))

print(sorted(numbers))

print(reversed(numbers))

print(list(reversed(numbers)))

print(enumerate(numbers))

print(list(enumerate(numbers)))

# =========================================================
# ENUMERATE
# =========================================================

languages = [
    "Python",
    "Java",
    "Go"
]

for index, language in enumerate(languages):
    print(index, language)

# =========================================================
# ZIP
# =========================================================

names = [
    "Amit",
    "Rahul",
    "Rohan"
]

marks = [
    90,
    85,
    95
]

for name, mark in zip(names, marks):
    print(name, mark)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

numbers = [12, 45, 67, 23, 89]

print(max(numbers))

print(min(numbers))

print(sum(numbers))

print(sorted(numbers))

# ---------------------------------------------------------

marks = [75, 85, 90, 95]

average = sum(marks) / len(marks)

print(average)

# ---------------------------------------------------------

numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]

print(squares)

# ---------------------------------------------------------

students = [
    "amit",
    "rahul",
    "rohan"
]

students = [
    student.title()
    for student in students
]

print(students)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Assignment is not copying.

list1 = [1, 2, 3]

list2 = list1

list2.append(4)

print(list1)

# ---------------------------------------------------------

# Mistake 2
#
# Forgetting nested lists in shallow copy.

import copy

a = [
    [1],
    [2]
]

b = a.copy()

b[0][0] = 100

print(a)

# ---------------------------------------------------------

# Mistake 3
#
# sort() modifies the original list.

numbers = [3, 1, 2]

numbers.sort()

print(numbers)

# ---------------------------------------------------------

# Mistake 4
#
# Using remove() for indexes.

numbers = [10, 20, 30]

# numbers.remove(1)

# remove() removes values,
# not indexes.

numbers.pop(1)

print(numbers)

# ---------------------------------------------------------

# Mistake 5
#
# Assuming list comprehension is only for numbers.

words = [
    "python",
    "java"
]

print(
    [word.upper() for word in words]
)

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is a list?
#
# Answer:
# A list is an ordered, mutable collection that
# allows duplicate values.
#
# ---------------------------------------------------------
#
# Q2. Are lists mutable?
#
# Answer:
#
# Yes.
#
# ---------------------------------------------------------
#
# Q3. Difference between append() and extend()?
#
# append()
# ----------
# Adds one object.
#
# extend()
# ----------
# Adds multiple elements from an iterable.
#
# ---------------------------------------------------------
#
# Q4. Difference between remove() and pop()?
#
# remove()
# ----------
# Removes by value.
#
# pop()
# -----
# Removes by index and returns the removed element.
#
# ---------------------------------------------------------
#
# Q5. Difference between sort() and sorted()?
#
# sort()
# -------
# Modifies the original list.
#
# sorted()
# --------
# Returns a new sorted list.
#
# ---------------------------------------------------------
#
# Q6. Difference between reverse() and reversed()?
#
# reverse()
# ----------
# Modifies the original list.
#
# reversed()
# -----------
# Returns an iterator.
#
# ---------------------------------------------------------
#
# Q7. What is list comprehension?
#
# Answer:
# A concise way to create lists using a single expression.
#
# ---------------------------------------------------------
#
# Q8. Difference between shallow copy and deep copy?
#
# Shallow Copy
# ------------
# Copies only the outer object.
#
# Deep Copy
# ---------
# Copies the entire object recursively.
#
# ---------------------------------------------------------
#
# Q9. Which function removes duplicate values from a list?
#
# Answer:
#
# list(set(my_list))
#
# ---------------------------------------------------------
#
# Q10. How do you reverse a list?
#
# Answer:
#
# list.reverse()
#
# or
#
# list[::-1]
#
# or
#
# list(reversed(list))
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Lists are ordered and mutable.
#
# ✓ Lists allow duplicate values.
#
# ✓ Lists support indexing and slicing.
#
# ✓ Common insertion methods:
#   append()
#   extend()
#   insert()
#
# ✓ Common removal methods:
#   remove()
#   pop()
#   clear()
#   del
#
# ✓ Useful methods:
#   count()
#   index()
#   copy()
#
# ✓ Sorting:
#   sort()
#   sorted()
#
# ✓ Reversing:
#   reverse()
#   reversed()
#   [::-1]
#
# ✓ List comprehension provides a concise way
#   to create new lists.
#
# ✓ Assignment is NOT copying.
#
# ✓ Use copy.deepcopy() for nested lists.
#
# ✓ enumerate() provides both index and value.
#
# ✓ zip() iterates over multiple iterables together.
#
# =========================================================
# END OF 07_lists.py
# =========================================================
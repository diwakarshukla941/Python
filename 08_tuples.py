# =========================================================
# FILE: 08_tuples.py
# PART 1
# =========================================================
#
# PYTHON TUPLES
#
# INDEX
#
# 1. What is a Tuple?
# 2. Why Tuples?
# 3. Creating Tuples
# 4. Tuple Characteristics
# 5. Tuple Indexing
# 6. Negative Indexing
# 7. Tuple Slicing
# 8. Tuple Immutability
#
# =========================================================
# 1. WHAT IS A TUPLE?
# =========================================================
#
# A tuple is an ordered, immutable collection that can
# store multiple values.
#
# Once created, its elements cannot be modified.
#
# Syntax:
#
# tuple_name = (item1, item2, item3)
#

numbers = (10, 20, 30)

print(numbers)

print(type(numbers))

# Output
#
# (10, 20, 30)
# <class 'tuple'>

# =========================================================
# 2. WHY TUPLES?
# =========================================================
#
# Tuples are useful when the data should not change.
#
# Examples:
#
# • Coordinates
# • RGB Colors
# • Days of the week
# • Database Records
# • Configuration Values
#

days = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
)

print(days)

# =========================================================
# 3. CREATING TUPLES
# =========================================================

# Empty Tuple

empty = ()

print(empty)

# Integer Tuple

numbers = (10, 20, 30)

# Float Tuple

prices = (10.5, 20.8, 30.2)

# String Tuple

names = (
    "Amit",
    "Rahul",
    "Rohan"
)

# Boolean Tuple

status = (
    True,
    False,
    True
)

print(numbers)
print(prices)
print(names)
print(status)

# =========================================================
# MIXED DATA TYPES
# =========================================================

data = (
    10,
    20.5,
    "Python",
    True,
    None
)

print(data)

# =========================================================
# NESTED TUPLE
# =========================================================

matrix = (
    (1, 2),
    (3, 4),
    (5, 6)
)

print(matrix)

# =========================================================
# USING tuple() CONSTRUCTOR
# =========================================================

letters = tuple("Python")

print(letters)

numbers = tuple(range(1, 6))

print(numbers)

# =========================================================
# SINGLE ELEMENT TUPLE
# =========================================================
#
# A comma is required.
#

value = (10,)

print(value)

print(type(value))

# Without comma

value = (10)

print(type(value))

# Output
#
# <class 'int'>

# =========================================================
# 4. TUPLE CHARACTERISTICS
# =========================================================
#
# Tuples are:
#
# ✓ Ordered
# ✓ Immutable
# ✓ Indexed
# ✓ Iterable
# ✓ Allow Duplicates
# ✓ Allow Mixed Data Types
#

sample = (
    10,
    20,
    20,
    30
)

print(sample)

# =========================================================
# 5. TUPLE INDEXING
# =========================================================

fruits = (
    "Apple",
    "Banana",
    "Mango",
    "Orange"
)

print(fruits[0])

print(fruits[1])

print(fruits[2])

print(fruits[3])

# =========================================================
# NEGATIVE INDEXING
# =========================================================

print(fruits[-1])

print(fruits[-2])

print(fruits[-3])

print(fruits[-4])

# =========================================================
# INDEX ERROR
# =========================================================

# print(fruits[100])

# IndexError

# =========================================================
# ACCESSING FIRST & LAST ELEMENT
# =========================================================

print(fruits[0])

print(fruits[-1])

# =========================================================
# 6. TUPLE SLICING
# =========================================================

numbers = (
    10,
    20,
    30,
    40,
    50,
    60,
    70
)

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
# COPYING A TUPLE
# =========================================================

copy_tuple = numbers[:]

print(copy_tuple)

# =========================================================
# 7. TUPLE IMMUTABILITY
# =========================================================
#
# Tuples cannot be modified after creation.
#

numbers = (
    10,
    20,
    30
)

# numbers[1] = 200

# TypeError

# =========================================================
# REASSIGNMENT
# =========================================================

numbers = (
    10,
    20,
    30
)

numbers = (
    100,
    200,
    300
)

print(numbers)

# =========================================================
# id() EXAMPLE
# =========================================================

a = (
    1,
    2,
    3
)

print(id(a))

a = (
    4,
    5,
    6
)

print(id(a))

# A new tuple object is created.

# =========================================================
# TUPLE LENGTH
# =========================================================

numbers = (
    10,
    20,
    30
)

print(len(numbers))

# =========================================================
# MEMBERSHIP
# =========================================================

numbers = (
    10,
    20,
    30,
    40
)

print(20 in numbers)

print(100 in numbers)

print(100 not in numbers)

# =========================================================
# ITERATING THROUGH A TUPLE
# =========================================================

languages = (
    "Python",
    "Java",
    "Go"
)

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

cities = (
    "Mumbai",
    "Delhi",
    "Pune",
    "Chennai"
)

print(cities[0])

print(cities[-1])

print(cities[::-1])

print(len(cities))

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Forgetting the comma in a
# single-element tuple.

value = (100)

print(type(value))

# Correct

value = (100,)

print(type(value))

# ---------------------------------------------------------

# Mistake 2
#
# Trying to modify a tuple.

# numbers[0] = 100

# TypeError

# ---------------------------------------------------------

# Mistake 3
#
# Confusing tuple with list.

numbers = (10, 20)

print(type(numbers))

# =========================================================
# FILE: 08_tuples.py
# PART 2
# =========================================================
#
# INDEX
#
# 8. Tuple Methods
# 9. Tuple Packing
# 10. Tuple Unpacking
# 11. Nested Tuples
# 12. Tuple Operators
# 13. Useful Built-in Functions
#
# =========================================================
# 8. TUPLE METHODS
# =========================================================
#
# Tuples have only two built-in methods:
#
# 1. count()
# 2. index()
#

numbers = (
    10,
    20,
    20,
    30,
    20,
    40
)

# =========================================================
# count()
# =========================================================
#
# Returns the number of occurrences of a value.
#

print(numbers.count(20))

print(numbers.count(100))

# Output
#
# 3
# 0

# =========================================================
# index()
# =========================================================
#
# Returns the index of the first occurrence.
#

numbers = (
    10,
    20,
    30,
    40
)

print(numbers.index(20))

print(numbers.index(40))

# numbers.index(100)
#
# ValueError

# =========================================================
# 9. TUPLE PACKING
# =========================================================
#
# Packing means storing multiple values into one tuple.
#

student = (
    "Amit",
    20,
    "Mumbai"
)

print(student)

# Parentheses are optional.

student = "Rahul", 21, "Delhi"

print(student)

# =========================================================
# MULTIPLE VALUE PACKING
# =========================================================

data = 10, 20, 30, 40

print(data)

print(type(data))

# =========================================================
# FUNCTION RETURN VALUES
# =========================================================

def get_coordinates():
    return 10, 20

point = get_coordinates()

print(point)

# =========================================================
# 10. TUPLE UNPACKING
# =========================================================
#
# Unpacking extracts tuple values into variables.
#

student = (
    "Amit",
    20,
    "Mumbai"
)

name, age, city = student

print(name)

print(age)

print(city)

# =========================================================
# UNPACKING NUMBERS
# =========================================================

numbers = (
    10,
    20,
    30
)

a, b, c = numbers

print(a)

print(b)

print(c)

# =========================================================
# VALUE ERROR
# =========================================================

# numbers = (10, 20, 30)

# a, b = numbers

# ValueError
#
# Number of variables must match
# the number of tuple elements.

# =========================================================
# USING *
# =========================================================

numbers = (
    10,
    20,
    30,
    40,
    50
)

first, *middle, last = numbers

print(first)

print(middle)

print(last)

# =========================================================
# IGNORING VALUES
# =========================================================

student = (
    "Amit",
    20,
    "Mumbai"
)

name, _, city = student

print(name)

print(city)

# =========================================================
# SWAPPING VARIABLES
# =========================================================
#
# Python uses tuple packing and unpacking internally.
#

a = 10
b = 20

a, b = b, a

print(a)

print(b)

# =========================================================
# RETURNING MULTIPLE VALUES
# =========================================================

def calculate(a, b):
    return (
        a + b,
        a - b,
        a * b,
        a / b
    )

result = calculate(20, 10)

print(result)

# Unpacking

add, sub, mul, div = calculate(20, 10)

print(add)

print(sub)

print(mul)

print(div)

# =========================================================
# 11. NESTED TUPLES
# =========================================================

matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix)

# =========================================================
# ACCESSING ELEMENTS
# =========================================================

print(matrix[0])

print(matrix[1])

print(matrix[2])

print(matrix[0][0])

print(matrix[1][2])

print(matrix[2][1])

# =========================================================
# ITERATING NESTED TUPLES
# =========================================================

for row in matrix:
    print(row)

print()

for row in matrix:
    for value in row:
        print(value, end=" ")
    print()

# =========================================================
# 12. TUPLE OPERATORS
# =========================================================

tuple1 = (
    1,
    2,
    3
)

tuple2 = (
    4,
    5,
    6
)

# =========================================================
# CONCATENATION
# =========================================================

print(tuple1 + tuple2)

# =========================================================
# REPETITION
# =========================================================

print(tuple1 * 3)

# =========================================================
# MEMBERSHIP
# =========================================================

print(2 in tuple1)

print(10 in tuple1)

print(10 not in tuple1)

# =========================================================
# COMPARISON
# =========================================================

print((1, 2) == (1, 2))

print((1, 2) != (2, 1))

print((1, 2) < (1, 3))

print((2, 1) > (1, 5))

# =========================================================
# 13. USEFUL BUILT-IN FUNCTIONS
# =========================================================

numbers = (
    30,
    10,
    40,
    20
)

print(len(numbers))

print(max(numbers))

print(min(numbers))

print(sum(numbers))

print(sorted(numbers))

print(tuple(sorted(numbers)))

print(reversed(numbers))

print(tuple(reversed(numbers)))

# =========================================================
# enumerate()
# =========================================================

languages = (
    "Python",
    "Java",
    "Go"
)

for index, language in enumerate(languages):
    print(index, language)

# =========================================================
# zip()
# =========================================================

names = (
    "Amit",
    "Rahul",
    "Rohan"
)

marks = (
    95,
    88,
    91
)

for name, mark in zip(names, marks):
    print(name, mark)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

coordinates = (
    100,
    250
)

x, y = coordinates

print(x)

print(y)

# ---------------------------------------------------------

rgb = (
    255,
    128,
    0
)

print(rgb)

# ---------------------------------------------------------

days = (
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri"
)

print(days.count("Mon"))

print(days.index("Wed"))

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Tuples cannot use append().

numbers = (
    1,
    2,
    3
)

# numbers.append(4)

# AttributeError

# ---------------------------------------------------------

# Mistake 2
#
# Tuples cannot use remove().

# numbers.remove(2)

# AttributeError

# ---------------------------------------------------------

# Mistake 3
#
# Incorrect unpacking.

# a, b = (1, 2, 3)

# ValueError

# ---------------------------------------------------------

# Mistake 4
#
# Assuming sorted() returns a tuple.

numbers = (
    3,
    2,
    1
)

print(sorted(numbers))

print(type(sorted(numbers)))

# sorted() returns a list.

# =========================================================
# FILE: 08_tuples.py
# PART 3
# =========================================================
#
# INDEX
#
# 14. Tuple vs List
# 15. Copying Tuples
# 16. Tuple Performance
# 17. Practical Examples
# 18. Common Beginner Mistakes
# 19. Interview Questions
# 20. Quick Revision
#
# =========================================================
# 14. TUPLE vs LIST
# =========================================================
#
# Both are sequence data types, but they have
# important differences.
#
# +----------------+----------------+----------------+
# | Feature        | List           | Tuple          |
# +----------------+----------------+----------------+
# | Mutable        | Yes            | No             |
# | Ordered        | Yes            | Yes            |
# | Indexed        | Yes            | Yes            |
# | Duplicates     | Yes            | Yes            |
# | Dynamic Size   | Yes            | No             |
# | Memory         | More           | Less           |
# | Performance    | Slower         | Faster         |
# +----------------+----------------+----------------+
#

numbers_list = [10, 20, 30]

numbers_tuple = (10, 20, 30)

print(type(numbers_list))

print(type(numbers_tuple))

# =========================================================
# WHEN TO USE A LIST
# =========================================================
#
# Use a list when data changes frequently.
#
# Examples:
#
# • Shopping cart
# • Student marks
# • Messages
# • Todo list
#

shopping_cart = [
    "Milk",
    "Bread",
    "Butter"
]

shopping_cart.append("Eggs")

print(shopping_cart)

# =========================================================
# WHEN TO USE A TUPLE
# =========================================================
#
# Use a tuple when data should never change.
#
# Examples:
#
# • Coordinates
# • Months
# • Days
# • RGB Colors
#

rgb = (
    255,
    128,
    64
)

print(rgb)

# =========================================================
# MEMORY COMPARISON
# =========================================================

import sys

list_data = [1, 2, 3, 4, 5]

tuple_data = (1, 2, 3, 4, 5)

print(sys.getsizeof(list_data))

print(sys.getsizeof(tuple_data))

# Tuples generally require less memory.

# =========================================================
# PERFORMANCE
# =========================================================
#
# Tuples are generally faster than lists
# because they are immutable.
#

numbers = (10, 20, 30)

for number in numbers:
    print(number)

# =========================================================
# 15. COPYING TUPLES
# =========================================================
#
# Since tuples are immutable, copying is usually
# unnecessary.
#

tuple1 = (
    10,
    20,
    30
)

tuple2 = tuple1

print(tuple1)

print(tuple2)

print(tuple1 is tuple2)

# Output
#
# True

# =========================================================
# USING tuple()
# =========================================================

tuple1 = (
    1,
    2,
    3
)

tuple2 = tuple(tuple1)

print(tuple1)

print(tuple2)

print(tuple1 is tuple2)

# For immutable tuples, Python may return
# the same object.

# =========================================================
# NESTED TUPLES
# =========================================================

data = (
    (1, 2),
    (3, 4)
)

print(data)

# Although the tuple itself cannot change,
# mutable objects inside a tuple can.

# =========================================================
# TUPLE CONTAINING A LIST
# =========================================================

student = (
    "Amit",
    [90, 80, 70]
)

print(student)

student[1].append(95)

print(student)

# The tuple is immutable,
# but the list inside it is mutable.

# =========================================================
# HASHABILITY
# =========================================================
#
# Immutable tuples can be used
# as dictionary keys.
#

location = {
    (10, 20): "Point A",
    (30, 40): "Point B"
}

print(location[(10, 20)])

# =========================================================
# TUPLES AS DICTIONARY KEYS
# =========================================================

employees = {
    (101, "IT"): "Amit",
    (102, "HR"): "Rahul"
}

print(employees[(101, "IT")])

# =========================================================
# TUPLES IN SETS
# =========================================================

points = {
    (1, 2),
    (3, 4),
    (5, 6)
}

print(points)

# =========================================================
# 16. PRACTICAL EXAMPLES
# =========================================================

# Example 1
# Coordinates

coordinate = (120, 450)

x, y = coordinate

print(x)

print(y)

# ---------------------------------------------------------

# Example 2
# RGB Color

red = (255, 0, 0)

green = (0, 255, 0)

blue = (0, 0, 255)

print(red)

print(green)

print(blue)

# ---------------------------------------------------------

# Example 3
# Returning Multiple Values

def calculate(a, b):
    return (
        a + b,
        a - b,
        a * b,
        a / b
    )

result = calculate(20, 10)

print(result)

# ---------------------------------------------------------

# Example 4
# Tuple Unpacking

student = (
    "Diwakar",
    22,
    "Mumbai"
)

name, age, city = student

print(name)

print(age)

print(city)

# ---------------------------------------------------------

# Example 5
# Swapping Variables

a = 100
b = 200

a, b = b, a

print(a)

print(b)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Forgetting the comma.

value = (10)

print(type(value))

# Correct

value = (10,)

print(type(value))

# ---------------------------------------------------------

# Mistake 2
#
# Trying to modify a tuple.

numbers = (10, 20)

# numbers[0] = 100

# TypeError

# ---------------------------------------------------------

# Mistake 3
#
# Trying to use append().

# numbers.append(30)

# AttributeError

# ---------------------------------------------------------

# Mistake 4
#
# Trying to use remove().

# numbers.remove(10)

# AttributeError

# ---------------------------------------------------------

# Mistake 5
#
# Incorrect unpacking.

# a, b = (1, 2, 3)

# ValueError

# ---------------------------------------------------------

# Mistake 6
#
# Assuming tuple() creates a new object.

t1 = (1, 2, 3)

t2 = tuple(t1)

print(t1 is t2)

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is a tuple?
#
# Answer:
# A tuple is an ordered, immutable sequence
# that allows duplicate values.
#
# ---------------------------------------------------------
#
# Q2. Are tuples mutable?
#
# Answer:
#
# No.
#
# ---------------------------------------------------------
#
# Q3. How many built-in tuple methods exist?
#
# Answer:
#
# Two
#
# • count()
# • index()
#
# ---------------------------------------------------------
#
# Q4. Difference between list and tuple?
#
# List
# ----
# Mutable
#
# Tuple
# -----
# Immutable
#
# ---------------------------------------------------------
#
# Q5. Can tuples contain mutable objects?
#
# Answer:
#
# Yes.
#
# Example:
#
# ("Python", [1, 2, 3])
#
# ---------------------------------------------------------
#
# Q6. Can tuples be dictionary keys?
#
# Answer:
#
# Yes, if all elements inside the tuple
# are hashable (immutable).
#
# ---------------------------------------------------------
#
# Q7. Why are tuples faster than lists?
#
# Answer:
#
# Because tuples are immutable,
# requiring less memory and fewer operations.
#
# ---------------------------------------------------------
#
# Q8. What is tuple packing?
#
# Answer:
#
# Combining multiple values into a tuple.
#
# ---------------------------------------------------------
#
# Q9. What is tuple unpacking?
#
# Answer:
#
# Assigning tuple elements to multiple variables.
#
# ---------------------------------------------------------
#
# Q10. How do you create a single-element tuple?
#
# Answer:
#
# (10,)
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Tuples are ordered.
#
# ✓ Tuples are immutable.
#
# ✓ Tuples support indexing and slicing.
#
# ✓ Tuples allow duplicate values.
#
# ✓ Tuples support packing and unpacking.
#
# ✓ Common methods:
#   count()
#   index()
#
# ✓ Tuples can be concatenated using +.
#
# ✓ Tuples can be repeated using *.
#
# ✓ Tuples are faster than lists.
#
# ✓ Tuples consume less memory.
#
# ✓ Tuples can be dictionary keys if they
#   contain only hashable values.
#
# ✓ A single-element tuple requires a comma.
#
# ✓ Tuple unpacking is commonly used to
#   return multiple values from functions.
#
# =========================================================
# END OF 08_tuples.py
# =========================================================
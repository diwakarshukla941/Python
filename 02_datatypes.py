# =========================================================
# PYTHON DATA TYPES
# =========================================================
#
# INDEX
#
# 1. What are Data Types?
# 2. Why Do We Need Data Types?
# 3. Dynamic Typing
# 4. Built-in Data Types
# 5. Numeric Data Types
#       - int
#       - float
#       - complex
# 6. Boolean Data Type
# 7. String Data Type
#
# =========================================================
# 1. WHAT ARE DATA TYPES?
# =========================================================
#
# A Data Type defines:
#
# • What kind of value a variable stores.
# • What operations can be performed on it.
# • How much memory it occupies.
#
# Every value in Python belongs to a data type.
#
# Example:
#

age = 20
price = 99.99
name = "Amit"
is_student = True

print(type(age))
print(type(price))
print(type(name))
print(type(is_student))

# Output
#
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'bool'>

# =========================================================
# 2. WHY DO WE NEED DATA TYPES?
# =========================================================
#
# Data types help Python understand:
#
# • How to store the value
# • How much memory to allocate
# • Which operations are valid
#
# Example:
#

a = 10
b = 20

print(a + b)

name = "Amit"

print(name.upper())

# Numbers support arithmetic operations.
# Strings support string methods.

# =========================================================
# 3. DYNAMIC TYPING
# =========================================================
#
# Python is dynamically typed.
#
# This means you don't need to specify the data type.
# Python automatically detects it.
#

value = 10
print(value)
print(type(value))

value = "Hello"
print(value)
print(type(value))

value = 10.5
print(value)
print(type(value))

value = True
print(value)
print(type(value))

# Output
#
# 10
# <class 'int'>
# Hello
# <class 'str'>
# 10.5
# <class 'float'>
# True
# <class 'bool'>

# =========================================================
# 4. BUILT-IN DATA TYPES
# =========================================================
#
# Python provides several built-in data types.
#
# Numeric
# -------
# int
# float
# complex
#
# Sequence
# --------
# str
# list
# tuple
# range
#
# Mapping
# -------
# dict
#
# Set
# ---
# set
# frozenset
#
# Boolean
# -------
# bool
#
# Binary
# ------
# bytes
# bytearray
# memoryview
#
# Special
# -------
# NoneType

# =========================================================
# 5. NUMERIC DATA TYPES
# =========================================================
#
# Numeric data types are used for mathematical calculations.
#
# Python has three numeric types:
#
# 1. int
# 2. float
# 3. complex

# =========================================================
# INTEGER (int)
# =========================================================
#
# Integer stores whole numbers.
#
# Positive
# Negative
# Zero
#

age = 20
marks = 450
temperature = -5
count = 0

print(age)
print(marks)
print(temperature)
print(count)

print(type(age))

# Output
#
# <class 'int'>

# Integer Operations

a = 20
b = 5

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)

# =========================================================
# FLOAT
# =========================================================
#
# Float stores decimal numbers.
#

price = 99.99
height = 5.8
pi = 3.14159

print(price)
print(height)
print(pi)

print(type(price))

# Output
#
# <class 'float'>

# Float Arithmetic

x = 10.5
y = 2.5

print(x + y)
print(x - y)
print(x * y)
print(x / y)

# =========================================================
# COMPLEX
# =========================================================
#
# Complex numbers contain:
#
# Real Part
# Imaginary Part
#
# Syntax
#
# real + imaginaryj
#

num1 = 2 + 3j
num2 = 5 - 4j

print(num1)
print(num2)

print(type(num1))

# Accessing Parts

print(num1.real)
print(num1.imag)

# Output
#
# 2.0
# 3.0

# Complex Arithmetic

a = 2 + 3j
b = 1 + 4j

print(a + b)
print(a - b)
print(a * b)

# Note:
#
# Complex numbers are mostly used in
# scientific computing,
# signal processing,
# electrical engineering,
# and mathematics.

# =========================================================
# COMPARISON OF NUMERIC TYPES
# =========================================================

integer = 10
floating = 10.5
complex_number = 10 + 2j

print(type(integer))
print(type(floating))
print(type(complex_number))

# Output
#
# int
# float
# complex

# =========================================================
# 6. BOOLEAN DATA TYPE
# =========================================================
#
# Boolean represents only two values:
#
# True
# False
#
# Internally:
#
# True  = 1
# False = 0
#

is_logged_in = True
is_admin = False

print(is_logged_in)
print(is_admin)

print(type(is_logged_in))

# Output
#
# <class 'bool'>

# Boolean in Comparisons

print(10 > 5)
print(10 < 5)
print(10 == 10)
print(10 != 10)

# Output
#
# True
# False
# True
# False

# Boolean Arithmetic

print(True + True)
print(True + False)
print(False + False)

# Output
#
# 2
# 1
# 0

# Truthy and Falsy Values

print(bool(1))
print(bool(100))
print(bool("Python"))

print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))
print(bool(None))

# Output
#
# True
# True
# True
# False
# False
# False
# False
# False

# =========================================================
# 7. STRING DATA TYPE
# =========================================================
#
# A String is a sequence of characters.
#
# Strings are enclosed in:
#
# ""
# ''
# """ """
# ''' '''
#

name = "Amit"
city = 'Mumbai'

message = """
Welcome
to
Python
"""

print(name)
print(city)
print(message)

print(type(name))

# Output
#
# <class 'str'>

# =========================================================
# STRING INDEXING
# =========================================================

language = "Python"

print(language[0])
print(language[1])
print(language[2])
print(language[3])
print(language[4])
print(language[5])

# Negative Indexing

print(language[-1])
print(language[-2])
print(language[-3])

# =========================================================
# STRING SLICING
# =========================================================

text = "Programming"

print(text[0:6])
print(text[3:8])
print(text[:5])
print(text[5:])
print(text[-5:])
print(text[:-3])

# =========================================================
# STRING CONCATENATION
# =========================================================

first = "Hello"
second = "World"

print(first + second)
print(first + " " + second)

# =========================================================
# STRING REPETITION
# =========================================================

print("Python " * 3)

# Output
#
# Python Python Python

# =========================================================
# STRING LENGTH
# =========================================================

name = "Diwakar"

print(len(name))

# =========================================================
# STRING MEMBERSHIP
# =========================================================

text = "Python Programming"

print("Python" in text)
print("Java" in text)

print("Java" not in text)

# =========================================================
# COMMON STRING METHODS
# =========================================================

text = "python programming"

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())

sample = "   Hello   "

print(sample.strip())
print(sample.lstrip())
print(sample.rstrip())

message = "Python is easy"

print(message.replace("easy", "powerful"))

print(message.split())

words = ["Python", "is", "awesome"]

print(" ".join(words))

# =========================================================
# STRING IMMUTABILITY
# =========================================================
#
# Strings are immutable.
# Once created, they cannot be changed.
#

name = "Python"

# name[0] = "J"
#
# TypeError
#
# 'str' object does not support item assignment

# Correct way

name = "Jython"

print(name)

# =========================================================
# 8. LIST DATA TYPE
# =========================================================
#
# A List is an ordered, mutable (changeable) collection.
#
# Characteristics:
#
# • Ordered
# • Mutable
# • Allows duplicate values
# • Can store multiple data types
#

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(type(numbers))

# Output
#
# [10, 20, 30, 40, 50]
# <class 'list'>

# =========================================================
# LIST WITH DIFFERENT DATA TYPES
# =========================================================

data = [10, 10.5, "Python", True]

print(data)

# =========================================================
# LIST INDEXING
# =========================================================

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
print(fruits[1])
print(fruits[-1])
print(fruits[-2])

# =========================================================
# LIST SLICING
# =========================================================

print(fruits[0:2])
print(fruits[1:4])
print(fruits[:3])
print(fruits[2:])
print(fruits[::-1])

# =========================================================
# MODIFYING LIST
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

fruits[1] = "Kiwi"

print(fruits)

# =========================================================
# ADDING ELEMENTS
# =========================================================

numbers = [10, 20, 30]

numbers.append(40)
print(numbers)

numbers.insert(1, 15)
print(numbers)

numbers.extend([50, 60, 70])
print(numbers)

# =========================================================
# REMOVING ELEMENTS
# =========================================================

numbers = [10, 20, 30, 40, 50]

numbers.remove(30)
print(numbers)

numbers.pop()
print(numbers)

numbers.pop(1)
print(numbers)

del numbers[0]
print(numbers)

# =========================================================
# LIST METHODS
# =========================================================

numbers = [40, 10, 60, 20, 30]

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)

print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

# =========================================================
# MEMBERSHIP
# =========================================================

fruits = ["Apple", "Banana", "Mango"]

print("Apple" in fruits)
print("Orange" in fruits)

# =========================================================
# ITERATING OVER A LIST
# =========================================================

numbers = [10, 20, 30]

for number in numbers:
    print(number)

# =========================================================
# LIST COMPREHENSION
# =========================================================

numbers = [1, 2, 3, 4, 5]

squares = [num * num for num in numbers]

print(squares)

# =========================================================
# NESTED LIST
# =========================================================

matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

print(matrix)

print(matrix[0])
print(matrix[1][1])

# =========================================================
# LIST COPYING
# =========================================================

list1 = [10, 20, 30]

list2 = list1.copy()

print(list1)
print(list2)

# =========================================================
# 9. TUPLE DATA TYPE
# =========================================================
#
# Tuple is an ordered, immutable collection.
#
# Characteristics:
#
# • Ordered
# • Immutable
# • Allows duplicates
# • Faster than lists
#

numbers = (10, 20, 30, 40)

print(numbers)
print(type(numbers))

# =========================================================
# SINGLE ELEMENT TUPLE
# =========================================================

num = (10,)
print(type(num))

# Without comma

num = (10)
print(type(num))

# =========================================================
# TUPLE INDEXING
# =========================================================

colors = ("Red", "Green", "Blue")

print(colors[0])
print(colors[-1])

# =========================================================
# TUPLE SLICING
# =========================================================

print(colors[:2])
print(colors[1:])
print(colors[::-1])

# =========================================================
# TUPLE METHODS
# =========================================================

numbers = (10, 20, 30, 20, 50)

print(numbers.count(20))
print(numbers.index(30))

# =========================================================
# IMMUTABLE
# =========================================================

numbers = (10, 20, 30)

# numbers[0] = 100
#
# TypeError

# =========================================================
# PACKING
# =========================================================

student = ("Amit", 20, "Mumbai")

print(student)

# =========================================================
# UNPACKING
# =========================================================

name, age, city = student

print(name)
print(age)
print(city)

# =========================================================
# 10. SET DATA TYPE
# =========================================================
#
# Set is an unordered collection.
#
# Characteristics:
#
# • Unordered
# • Mutable
# • No duplicate values
# • Fast lookup
#

numbers = {10, 20, 30, 40}

print(numbers)
print(type(numbers))

# =========================================================
# DUPLICATES ARE REMOVED
# =========================================================

data = {10, 20, 10, 30, 20, 40}

print(data)

# Output
#
# {10,20,30,40}

# =========================================================
# ADDING ELEMENTS
# =========================================================

numbers = {10, 20}

numbers.add(30)

print(numbers)

numbers.update([40, 50, 60])

print(numbers)

# =========================================================
# REMOVING ELEMENTS
# =========================================================

numbers = {10, 20, 30, 40}

numbers.remove(20)
print(numbers)

numbers.discard(30)
print(numbers)

removed = numbers.pop()

print(removed)
print(numbers)

# =========================================================
# SET OPERATIONS
# =========================================================

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A | B)

print(A & B)

print(A - B)

print(A ^ B)

# =========================================================
# MEMBERSHIP
# =========================================================

print(3 in A)
print(10 in A)

# =========================================================
# ITERATING
# =========================================================

for item in A:
    print(item)

# =========================================================
# FROZENSET
# =========================================================
#
# Immutable version of set.
#

numbers = frozenset([10, 20, 30])

print(numbers)

# numbers.add(40)
#
# AttributeError

# =========================================================
# 11. DICTIONARY DATA TYPE
# =========================================================
#
# Dictionary stores data as key-value pairs.
#
# Characteristics:
#
# • Mutable
# • Ordered (Python 3.7+)
# • Keys are unique
# • Values can repeat
#

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

print(student)
print(type(student))

# =========================================================
# ACCESSING VALUES
# =========================================================

print(student["name"])
print(student["age"])

print(student.get("city"))

# =========================================================
# ADDING VALUES
# =========================================================

student["college"] = "XYZ College"

print(student)

# =========================================================
# MODIFYING VALUES
# =========================================================

student["age"] = 21

print(student)

# =========================================================
# REMOVING VALUES
# =========================================================

student.pop("city")

print(student)

del student["college"]

print(student)

# =========================================================
# DICTIONARY METHODS
# =========================================================

student = {
    "name": "Amit",
    "age": 20,
    "city": "Mumbai"
}

print(student.keys())

print(student.values())

print(student.items())

# =========================================================
# ITERATING
# =========================================================

for key in student:
    print(key)

for value in student.values():
    print(value)

for key, value in student.items():
    print(key, value)

# =========================================================
# NESTED DICTIONARY
# =========================================================

employees = {
    "emp1": {
        "name": "Amit",
        "salary": 50000
    },
    "emp2": {
        "name": "Rahul",
        "salary": 60000
    }
}

print(employees)

print(employees["emp1"]["name"])
print(employees["emp2"]["salary"])

# =========================================================
# DICTIONARY COMPREHENSION
# =========================================================

squares = {x: x * x for x in range(1, 6)}

print(squares)

# =========================================================
# 12. NONETYPE
# =========================================================
#
# None represents the absence of a value.
#
# It is often used:
# • As a default value
# • To indicate "no result"
# • To initialize variables
#

value = None

print(value)
print(type(value))

# Output
#
# None
# <class 'NoneType'>

# Checking None

if value is None:
    print("Variable has no value.")

# =========================================================
# FUNCTIONS RETURNING NONE
# =========================================================

def greet():
    print("Hello")

result = greet()

print(result)

# Output
#
# Hello
# None

# =========================================================
# 13. MUTABLE VS IMMUTABLE
# =========================================================#
# Mutable objects can be modified after creation.
#
# Immutable objects cannot be modified after creation.
#

# -------------------------
# IMMUTABLE EXAMPLE
# -------------------------

name = "Python"

# name[0] = "J"
#
# TypeError

name = "Jython"

print(name)

# -------------------------
# MUTABLE EXAMPLE
# -------------------------

numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)

# Output
#
# [100, 20, 30]

# =========================================================
# COMMON MUTABLE TYPES
# =========================================================

# list
# dict
# set
# bytearray

# =========================================================
# COMMON IMMUTABLE TYPES
# =========================================================

# int
# float
# bool
# complex
# str
# tuple
# frozenset
# bytes
# NoneType

# =========================================================
# MEMORY BEHAVIOR
# =========================================================

a = 10
b = a

print(id(a))
print(id(b))

a = 20

print(id(a))
print(id(b))

# Since integers are immutable,
# changing a creates a new object.

# =========================================================
# MUTABLE MEMORY EXAMPLE
# =========================================================

list1 = [10, 20]
list2 = list1

list2.append(30)

print(list1)
print(list2)

# Both variables reference the same object.

# =========================================================
# 14. type() FUNCTION
# =========================================================
#
# type() returns the data type of an object.
#

age = 20
price = 99.99
name = "Python"
skills = ["Python", "JavaScript"]

print(type(age))
print(type(price))
print(type(name))
print(type(skills))

# =========================================================
# USING type() IN CONDITIONS
# =========================================================

value = 100

if type(value) == int:
    print("Integer")

# =========================================================
# 15. isinstance()
# =========================================================
#
# isinstance() checks whether an object belongs
# to a particular class or data type.
#
# Syntax:
#
# isinstance(object, datatype)
#

age = 20

print(isinstance(age, int))
print(isinstance(age, float))

# Output
#
# True
# False

name = "Python"

print(isinstance(name, str))

numbers = [1, 2, 3]

print(isinstance(numbers, list))

# =========================================================
# WHY isinstance() IS BETTER THAN type()
# =========================================================

class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(type(dog) == Animal)

print(isinstance(dog, Animal))

# Output
#
# False
# True

# isinstance() supports inheritance.

# =========================================================
# 16. TYPE CONVERSION (INTRODUCTION)
# =========================================================
#
# Python allows conversion between data types.
#

# Integer

print(int(10.9))

# Float

print(float(10))

# String

print(str(100))

# Boolean

print(bool(1))
print(bool(0))

# List

print(list("Python"))

# Tuple

print(tuple([1, 2, 3]))

# Set

print(set([1, 2, 2, 3]))

# Dictionary

pairs = [("name", "Amit"), ("age", 20)]

print(dict(pairs))

# =========================================================
# EXAMPLES
# =========================================================

age = "20"

age = int(age)

print(age + 10)

price = 100

price = float(price)

print(price)

number = 50

number = str(number)

print(number)

# =========================================================
# 17. DATA TYPE SUMMARY
# =========================================================
#
# +------------+-----------+---------+------------+
# | Data Type  | Mutable   | Ordered | Duplicates |
# +------------+-----------+---------+------------+
# | int        | No        | N/A     | N/A        |
# | float      | No        | N/A     | N/A        |
# | complex    | No        | N/A     | N/A        |
# | bool       | No        | N/A     | N/A        |
# | str        | No        | Yes     | Yes        |
# | list       | Yes       | Yes     | Yes        |
# | tuple      | No        | Yes     | Yes        |
# | set        | Yes       | No      | No         |
# | frozenset  | No        | No      | No         |
# | dict       | Yes       | Yes*    | Keys No    |
# | NoneType   | No        | N/A     | N/A        |
# +------------+-----------+---------+------------+
#
# *Ordered since Python 3.7

# =========================================================
# 18. COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Expecting strings to change.

text = "Python"

# text[0] = "J"

# Correct

text = "Jython"

# ----------------------------

# Mistake 2
#
# Using remove() on a tuple.

numbers = (10, 20, 30)

# numbers.remove(20)

# ----------------------------

# Mistake 3
#
# Duplicate values in a set.

data = {1, 2, 2, 3, 3, 4}

print(data)

# Output
#
# {1, 2, 3, 4}

# ----------------------------

# Mistake 4
#
# Accessing a missing dictionary key.

student = {"name": "Amit"}

# print(student["age"])
#
# KeyError

# Better

print(student.get("age"))

# ----------------------------

# Mistake 5
#
# Comparing with None incorrectly.

value = None

# Wrong

if value == None:
    print("Wrong Style")

# Recommended

if value is None:
    print("Correct Style")

# =========================================================
# 19. INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is a data type?
#
# Answer:
# A data type defines the kind of value a variable stores
# and determines the operations that can be performed.
#
# -------------------------------------------------
#
# Q2. Is Python statically typed?
#
# Answer:
# No.
# Python is dynamically typed.
#
# -------------------------------------------------
#
# Q3. Difference between List and Tuple?
#
# List
# • Mutable
# • Slower
#
# Tuple
# • Immutable
# • Faster
#
# -------------------------------------------------
#
# Q4. Difference between Set and Dictionary?
#
# Set
# • Stores only values.
#
# Dictionary
# • Stores key-value pairs.
#
# -------------------------------------------------
#
# Q5. Difference between type() and isinstance()?
#
# type()
# • Returns the exact data type.
#
# isinstance()
# • Checks whether an object belongs to a type.
# • Supports inheritance.
#
# -------------------------------------------------
#
# Q6. Which Python data types are mutable?
#
# Answer:
#
# • list
# • dict
# • set
# • bytearray
#
# -------------------------------------------------
#
# Q7. Which Python data types are immutable?
#
# Answer:
#
# • int
# • float
# • bool
# • complex
# • str
# • tuple
# • frozenset
# • bytes
# • NoneType
#
# -------------------------------------------------
#
# Q8. What is None?
#
# Answer:
#
# None represents the absence of a value.
#
# -------------------------------------------------
#
# Q9. What is the difference between == and is?
#
# ==
# Compares values.
#
# is
# Compares object identity (memory reference).

# =========================================================
# 20. QUICK REVISION
# =========================================================
#
# ✓ Python is dynamically typed.
# ✓ Use type() to know an object's data type.
# ✓ Use isinstance() for safe type checking.
# ✓ int stores whole numbers.
# ✓ float stores decimal numbers.
# ✓ complex stores complex numbers.
# ✓ bool has only True and False.
# ✓ str is immutable.
# ✓ list is ordered, mutable, and allows duplicates.
# ✓ tuple is ordered and immutable.
# ✓ set is unordered and removes duplicates.
# ✓ frozenset is an immutable set.
# ✓ dict stores key-value pairs.
# ✓ None means no value.
# ✓ Mutable objects can be modified.
# ✓ Immutable objects cannot be modified.
# ✓ Use type conversion functions like int(), float(), str(), list(), tuple(), set(), dict().
#
# =========================================================
# END OF datatypes.py
# =========================================================
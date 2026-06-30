# =========================================================
# PYTHON TYPE CONVERSION
# =========================================================
#
# INDEX
#
# 1. What is Type Conversion?
# 2. Why Do We Need Type Conversion?
# 3. Types of Type Conversion
# 4. Implicit Type Conversion
# 5. Explicit Type Conversion (Type Casting)
# 6. int()
# 7. float()
#
# =========================================================
# 1. WHAT IS TYPE CONVERSION?
# =========================================================
#
# Type Conversion is the process of converting one data type
# into another data type.
#
# Python provides two ways:
#
# 1. Implicit Conversion (Automatic)
# 2. Explicit Conversion (Manual)
#
# Example
#

age = "20"

print(type(age))

age = int(age)

print(type(age))

# Output
#
# <class 'str'>
# <class 'int'>

# =========================================================
# 2. WHY DO WE NEED TYPE CONVERSION?
# =========================================================
#
# Different data types cannot always work together.
#
# Example
#

# age = "20"
#
# print(age + 10)
#
# TypeError

# Correct

age = int("20")

print(age + 10)

# Output
#
# 30

# =========================================================
# 3. TYPES OF TYPE CONVERSION
# =========================================================
#
# 1. Implicit Type Conversion
#
# Python automatically converts one data type
# into another.
#
# -----------------------------
#
# 2. Explicit Type Conversion
#
# Programmer manually converts one
# data type into another.
#

# =========================================================
# 4. IMPLICIT TYPE CONVERSION
# =========================================================
#
# Also called Automatic Type Conversion.
#
# Python converts smaller data types
# into larger compatible data types.
#

a = 10
b = 5.5

result = a + b

print(result)

print(type(result))

# Output
#
# 15.5
# <class 'float'>

# Integer + Float

x = 100
y = 99.9

print(type(x))
print(type(y))
print(type(x + y))

# Float + Complex

a = 10.5
b = 2 + 3j

print(type(a + b))

# Boolean + Integer

print(True + 5)

print(False + 20)

# Output
#
# 6
# 20

# Boolean behaves like:
#
# True = 1
# False = 0

# =========================================================
# IMPLICIT CONVERSION RULE
# =========================================================
#
# int
#   ↓
# float
#   ↓
# complex
#
# Python always converts towards
# the higher precision type.

print(type(10 + 10.5))

print(type(10 + (2 + 3j)))

# =========================================================
# EXPLICIT TYPE CONVERSION
# =========================================================
#
# Also called Type Casting.
#
# Python provides built-in functions
# for manual conversion.
#

# int()
# float()
# str()
# bool()
# list()
# tuple()
# set()
# dict()
# complex()

# =========================================================
# 6. int()
# =========================================================
#
# Converts a compatible value into integer.
#

print(int(10.9))

print(int(15.1))

print(int(True))

print(int(False))

print(int("100"))

# Output
#
# 10
# 15
# 1
# 0
# 100

# ---------------------------------------------------------
# Float → Integer
# ---------------------------------------------------------

price = 99.99

price = int(price)

print(price)

# Output
#
# 99

# Decimal part is removed.
# It is NOT rounded.

# ---------------------------------------------------------
# String → Integer
# ---------------------------------------------------------

age = "25"

print(int(age))

marks = "450"

print(int(marks))

# ---------------------------------------------------------
# Boolean → Integer
# ---------------------------------------------------------

print(int(True))

print(int(False))

# ---------------------------------------------------------
# Invalid Conversion
# ---------------------------------------------------------

# print(int("Python"))
#
# ValueError

# print(int("10.5"))
#
# ValueError

# print(int(None))
#
# TypeError

# =========================================================
# USING int() WITH DIFFERENT BASES
# =========================================================

binary = "1010"

print(int(binary, 2))

# Output
#
# 10

octal = "17"

print(int(octal, 8))

# Output
#
# 15

hexadecimal = "FF"

print(int(hexadecimal, 16))

# Output
#
# 255

# =========================================================
# 7. float()
# =========================================================
#
# Converts compatible values into float.
#

print(float(10))

print(float(True))

print(float(False))

print(float("10"))

print(float("10.5"))

# Output
#
# 10.0
# 1.0
# 0.0
# 10.0
# 10.5

# ---------------------------------------------------------
# Integer → Float
# ---------------------------------------------------------

age = 20

age = float(age)

print(age)

# ---------------------------------------------------------
# Boolean → Float
# ---------------------------------------------------------

print(float(True))

print(float(False))

# ---------------------------------------------------------
# String → Float
# ---------------------------------------------------------

price = "99.99"

price = float(price)

print(price)

# ---------------------------------------------------------
# Invalid Conversion
# ---------------------------------------------------------

# print(float("Python"))
#
# ValueError

# print(float(None))
#
# TypeError

# =========================================================
# float() Examples
# =========================================================

num1 = "100"

num2 = "25.5"

print(float(num1))

print(float(num2))

print(type(float(num1)))

# =========================================================
# 8. str()
# =========================================================
#
# str() converts almost any object into a string.
#

print(str(100))
print(str(99.99))
print(str(True))
print(str(False))
print(str(None))

# Output
#
# '100'
# '99.99'
# 'True'
# 'False'
# 'None'

# ---------------------------------------------------------
# Integer → String
# ---------------------------------------------------------

age = 25

age = str(age)

print(age)
print(type(age))

# ---------------------------------------------------------
# Float → String
# ---------------------------------------------------------

price = 99.99

price = str(price)

print(price)
print(type(price))

# ---------------------------------------------------------
# Boolean → String
# ---------------------------------------------------------

status = True

status = str(status)

print(status)
print(type(status))

# ---------------------------------------------------------
# List → String
# ---------------------------------------------------------

numbers = [10, 20, 30]

print(str(numbers))

# ---------------------------------------------------------
# Dictionary → String
# ---------------------------------------------------------

student = {
    "name": "Amit",
    "age": 20
}

print(str(student))

# =========================================================
# STRING CONCATENATION AFTER CONVERSION
# =========================================================

age = 20

message = "Age = " + str(age)

print(message)

# =========================================================
# 9. bool()
# =========================================================
#
# bool() converts a value into either:
#
# True
# False
#

print(bool(1))
print(bool(100))
print(bool(-5))

print(bool(0))

# Output
#
# True
# True
# True
# False

# ---------------------------------------------------------
# Numbers
# ---------------------------------------------------------

print(bool(10))
print(bool(-20))
print(bool(0))

# ---------------------------------------------------------
# Strings
# ---------------------------------------------------------

print(bool("Python"))

print(bool("Hello"))

print(bool(""))

# ---------------------------------------------------------
# Lists
# ---------------------------------------------------------

print(bool([1, 2, 3]))

print(bool([]))

# ---------------------------------------------------------
# Tuples
# ---------------------------------------------------------

print(bool((10, 20)))

print(bool(()))

# ---------------------------------------------------------
# Sets
# ---------------------------------------------------------

print(bool({1, 2, 3}))

print(bool(set()))

# ---------------------------------------------------------
# Dictionaries
# ---------------------------------------------------------

print(bool({"name": "Amit"}))

print(bool({}))

# ---------------------------------------------------------
# None
# ---------------------------------------------------------

print(bool(None))

# =========================================================
# FALSY VALUES
# =========================================================
#
# These always become False:
#
# 0
# 0.0
# 0j
# ""
# ''
# []
# ()
# {}
# set()
# None
#

# Everything else is True.

# =========================================================
# 10. list()
# =========================================================
#
# list() converts an iterable into a list.
#

print(list("Python"))

# Output
#
# ['P','y','t','h','o','n']

# ---------------------------------------------------------
# Tuple → List
# ---------------------------------------------------------

numbers = (10, 20, 30)

print(list(numbers))

# ---------------------------------------------------------
# Set → List
# ---------------------------------------------------------

numbers = {10, 20, 30}

print(list(numbers))

# ---------------------------------------------------------
# Range → List
# ---------------------------------------------------------

print(list(range(1, 6)))

# ---------------------------------------------------------
# Dictionary → List
# ---------------------------------------------------------

student = {
    "name": "Amit",
    "age": 20
}

print(list(student))

# Output
#
# ['name', 'age']

# =========================================================
# 11. tuple()
# =========================================================
#
# tuple() converts an iterable into a tuple.
#

print(tuple("Python"))

# ---------------------------------------------------------
# List → Tuple
# ---------------------------------------------------------

numbers = [10, 20, 30]

print(tuple(numbers))

# ---------------------------------------------------------
# Set → Tuple
# ---------------------------------------------------------

numbers = {10, 20, 30}

print(tuple(numbers))

# ---------------------------------------------------------
# Range → Tuple
# ---------------------------------------------------------

print(tuple(range(1, 6)))

# =========================================================
# 12. set()
# =========================================================
#
# set() creates a set from an iterable.
#
# Duplicate values are removed.
#

print(set("Python"))

# ---------------------------------------------------------
# List → Set
# ---------------------------------------------------------

numbers = [10, 20, 20, 30, 30, 40]

print(set(numbers))

# ---------------------------------------------------------
# Tuple → Set
# ---------------------------------------------------------

numbers = (1, 2, 2, 3, 3)

print(set(numbers))

# ---------------------------------------------------------
# String → Set
# ---------------------------------------------------------

print(set("banana"))

# Output
#
# {'b', 'a', 'n'}

# =========================================================
# 13. dict()
# =========================================================
#
# dict() converts key-value pairs into a dictionary.
#

pairs = [
    ("name", "Amit"),
    ("age", 20),
    ("city", "Mumbai")
]

student = dict(pairs)

print(student)

# ---------------------------------------------------------
# Keyword Arguments
# ---------------------------------------------------------

student = dict(
    name="Rahul",
    age=21,
    city="Delhi"
)

print(student)

# ---------------------------------------------------------
# Zipping Two Lists
# ---------------------------------------------------------

keys = ["name", "age", "city"]

values = ["Amit", 20, "Mumbai"]

student = dict(zip(keys, values))

print(student)

# ---------------------------------------------------------
# Invalid Conversion
# ---------------------------------------------------------

# dict([1,2,3])
#
# TypeError

# =========================================================
# 14. complex()
# =========================================================
#
# complex() converts numbers into complex numbers.
#

print(complex(10))

print(complex(10.5))

print(complex(True))

# Output
#
# (10+0j)
# (10.5+0j)
# (1+0j)

# ---------------------------------------------------------
# String → Complex
# ---------------------------------------------------------

print(complex("10"))

print(complex("5+3j"))

# ---------------------------------------------------------
# Real + Imaginary Parts
# ---------------------------------------------------------

number = complex(10, 5)

print(number)

# Output
#
# (10+5j)

# ---------------------------------------------------------
# Accessing Parts
# ---------------------------------------------------------

print(number.real)

print(number.imag)

# ---------------------------------------------------------
# Invalid Conversion
# ---------------------------------------------------------

# complex("Python")
#
# ValueError

# =========================================================
# CONVERSION SUMMARY
# =========================================================
#
# int()      → Integer
# float()    → Float
# str()      → String
# bool()     → Boolean
# list()     → List
# tuple()    → Tuple
# set()      → Set
# dict()     → Dictionary
# complex()  → Complex Number
#

# =========================================================
# 15. VALID VS INVALID CONVERSIONS
# =========================================================
#
# Not every data type can be converted into every other
# data type. Some conversions are valid, while others
# raise exceptions.
#

# ---------------------------------------------------------
# VALID CONVERSIONS
# ---------------------------------------------------------

print(int("100"))
print(float("99.99"))
print(str(500))
print(bool(1))
print(bool(0))
print(list("Python"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))
print(dict([("name", "Amit"), ("age", 20)]))
print(complex(10))

# ---------------------------------------------------------
# INVALID CONVERSIONS
# ---------------------------------------------------------

# int("Python")
# ValueError

# float("Hello")
# ValueError

# int(None)
# TypeError

# float(None)
# TypeError

# dict([1, 2, 3])
# TypeError

# int([10, 20])
# TypeError

# float({"a": 1})
# TypeError

# complex("Hello")
# ValueError

# =========================================================
# 16. ValueError
# =========================================================
#
# ValueError occurs when the data type is correct,
# but the value itself cannot be converted.
#

# Example 1

# int("Python")

# ValueError:
# invalid literal for int()

# Example 2

# float("Hello")

# ValueError

# Example 3

# int("10.5")

# ValueError

# Correct

print(int("10"))

print(float("10.5"))

# =========================================================
# 17. TypeError
# =========================================================
#
# TypeError occurs when the object type itself
# cannot be converted.
#

# Example

# int(None)

# TypeError

# Example

# float([10, 20])

# TypeError

# Example

# int({"age": 20})

# TypeError

# =========================================================
# HANDLING CONVERSION ERRORS
# =========================================================

value = "Python"

try:
    number = int(value)
    print(number)

except ValueError:
    print("Cannot convert to integer.")

# ---------------------------------------------------------

value = None

try:
    print(int(value))

except TypeError:
    print("Invalid object type.")

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1
# User Input

age = "25"

age = int(age)

print(age + 5)

# ---------------------------------------------------------
# Example 2
# Decimal String
# ---------------------------------------------------------

price = "199.99"

price = float(price)

print(price * 2)

# ---------------------------------------------------------
# Example 3
# Integer to String
# ---------------------------------------------------------

roll = 101

message = "Roll Number: " + str(roll)

print(message)

# ---------------------------------------------------------
# Example 4
# Remove Duplicate Values
# ---------------------------------------------------------

numbers = [10, 20, 20, 30, 30, 40]

numbers = list(set(numbers))

print(numbers)

# ---------------------------------------------------------
# Example 5
# Tuple Conversion
# ---------------------------------------------------------

marks = [90, 80, 70]

marks = tuple(marks)

print(marks)

# ---------------------------------------------------------
# Example 6
# Dictionary Conversion
# ---------------------------------------------------------

pairs = [
    ("id", 1),
    ("name", "Amit"),
    ("city", "Mumbai")
]

student = dict(pairs)

print(student)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# ---------------------------------------------------------
# Mistake 1
# ---------------------------------------------------------

# age = "20"
# print(age + 10)

# TypeError

# Correct

age = int("20")

print(age + 10)

# ---------------------------------------------------------
# Mistake 2
# ---------------------------------------------------------

# print(int("10.5"))

# ValueError

# Correct

print(int(float("10.5")))

# ---------------------------------------------------------
# Mistake 3
# ---------------------------------------------------------

text = "False"

print(bool(text))

# Output
#
# True

# Explanation:
# Any non-empty string is True.

# ---------------------------------------------------------
# Mistake 4
# ---------------------------------------------------------

numbers = [1, 2, 2, 3]

print(set(numbers))

# Output
#
# {1, 2, 3}

# Remember:
# set() removes duplicate values.

# ---------------------------------------------------------
# Mistake 5
# ---------------------------------------------------------

student = {
    "name": "Amit"
}

print(list(student))

# Output
#
# ['name']

# Explanation:
# list(dictionary) returns only keys.

# ---------------------------------------------------------
# Mistake 6
# ---------------------------------------------------------

print(str([1, 2, 3]))

# Output
#
# '[1, 2, 3]'

# str() creates a string representation.
# It does NOT convert elements individually.

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is type conversion?
#
# Answer:
# Type conversion is the process of converting one
# data type into another.
#
# ---------------------------------------------------------
#
# Q2. How many types of conversion are there?
#
# Answer:
#
# 1. Implicit Conversion
# 2. Explicit Conversion
#
# ---------------------------------------------------------
#
# Q3. What is implicit type conversion?
#
# Answer:
# Python automatically converts compatible
# data types during an operation.
#
# Example:
#

print(10 + 5.5)

# ---------------------------------------------------------
#
# Q4. What is explicit type conversion?
#
# Answer:
# The programmer manually converts one
# data type into another using built-in functions.
#
# Example:
#

print(int("100"))

# ---------------------------------------------------------
#
# Q5. Name some type conversion functions.
#
# Answer:
#
# int()
# float()
# str()
# bool()
# list()
# tuple()
# set()
# dict()
# complex()
#
# ---------------------------------------------------------
#
# Q6. What is the difference between ValueError
# and TypeError?
#
# ValueError:
# The value is invalid.
#
# Example:
#
# int("Python")
#
# -----------------------------
#
# TypeError:
# The object type is incompatible.
#
# Example:
#
# int(None)
#
# ---------------------------------------------------------
#
# Q7. Does int() round decimal values?
#
# Answer:
#
# No.
#
# It truncates (removes) the decimal part.
#
# Example:
#

print(int(9.99))

# Output
#
# 9

# ---------------------------------------------------------
#
# Q8. Why does bool("False") return True?
#
# Answer:
#
# Because any non-empty string is True.
#
# Only an empty string ("") becomes False.

print(bool("False"))

print(bool(""))

# ---------------------------------------------------------
#
# Q9. What does list(dictionary) return?
#
# Answer:
#
# It returns only the dictionary keys.

student = {
    "name": "Amit",
    "age": 20
}

print(list(student))

# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Type conversion changes one data type into another.
#
# ✓ Two types:
#     - Implicit
#     - Explicit
#
# ✓ Implicit conversion is automatic.
#
# ✓ Explicit conversion uses built-in functions.
#
# ✓ int() converts to integer.
#
# ✓ float() converts to float.
#
# ✓ str() converts to string.
#
# ✓ bool() converts to True or False.
#
# ✓ list() converts an iterable into a list.
#
# ✓ tuple() converts an iterable into a tuple.
#
# ✓ set() converts an iterable into a set and removes duplicates.
#
# ✓ dict() converts key-value pairs into a dictionary.
#
# ✓ complex() converts values into complex numbers.
#
# ✓ int() removes the decimal part; it does not round.
#
# ✓ ValueError means the value cannot be converted.
#
# ✓ TypeError means the object's type is incompatible.
#
# ✓ Any non-empty string is True when converted using bool().
#
# ✓ list(dictionary) returns only the dictionary keys.
#
# =========================================================
# END OF type_conversion.py
# =========================================================
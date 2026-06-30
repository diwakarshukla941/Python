# =========================================================
# FILE: 05_operators.py
# =========================================================
#
# PYTHON OPERATORS
#
# INDEX
#
# 1. What are Operators?
# 2. Why Operators?
# 3. Types of Operators
# 4. Arithmetic Operators
# 5. Unary Operators
# 6. Assignment Operators
#
# =========================================================
# 1. WHAT ARE OPERATORS?
# =========================================================
#
# Operators are special symbols that perform operations
# on one or more operands (values or variables).
#
# Example:
#

a = 10
b = 5

print(a + b)

# Here:
#
# + is the operator.
#
# a and b are operands.

# =========================================================
# 2. WHY DO WE NEED OPERATORS?
# =========================================================
#
# Operators help us:
#
# • Perform calculations
# • Compare values
# • Make decisions
# • Assign values
# • Work with collections
# • Perform logical operations
#

price = 200
quantity = 5

total = price * quantity

print(total)

# =========================================================
# 3. TYPES OF OPERATORS
# =========================================================
#
# Python provides the following operators:
#
# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Identity Operators
# 6. Membership Operators
# 7. Bitwise Operators
#
# =========================================================
# 4. ARITHMETIC OPERATORS
# =========================================================
#
# Used to perform mathematical calculations.
#

a = 20
b = 6

# =========================================================
# Addition (+)
# =========================================================

print(a + b)

# Output
#
# 26

# =========================================================
# Subtraction (-)
# =========================================================

print(a - b)

# Output
#
# 14

# =========================================================
# Multiplication (*)
# =========================================================

print(a * b)

# Output
#
# 120

# =========================================================
# Division (/)
# =========================================================

print(a / b)

# Output
#
# 3.3333333333333335

# Division always returns float.

print(type(a / b))

# =========================================================
# Floor Division (//)
# =========================================================
#
# Returns the quotient without decimal.
#

print(a // b)

# Output
#
# 3

print(25 // 4)

# Output
#
# 6

print(10 // 3)

# Output
#
# 3

# =========================================================
# Modulus (%)
# =========================================================
#
# Returns the remainder.
#

print(a % b)

# Output
#
# 2

print(15 % 4)

# Output
#
# 3

# =========================================================
# Exponent (**)
# =========================================================
#
# Raises a number to a power.
#

print(2 ** 3)

# Output
#
# 8

print(5 ** 2)

# Output
#
# 25

print(10 ** 0)

# Output
#
# 1

# =========================================================
# PRECEDENCE OF ARITHMETIC OPERATORS
# =========================================================
#
# Highest
#
# ()
# **
# *, /, //, %
# +, -
#
# Lowest
#

print(2 + 3 * 4)

# Output
#
# 14

print((2 + 3) * 4)

# Output
#
# 20

print(2 ** 3 * 4)

# Output
#
# 32

# =========================================================
# ARITHMETIC WITH FLOATS
# =========================================================

x = 10.5
y = 2

print(x + y)

print(x - y)

print(x * y)

print(x / y)

print(x // y)

print(x % y)

# =========================================================
# ARITHMETIC WITH STRINGS
# =========================================================

text = "Python"

print(text * 3)

# Output
#
# PythonPythonPython

# String Concatenation

first = "Hello"

second = "World"

print(first + second)

print(first + " " + second)

# Invalid

# print("Python" - "Java")
#
# TypeError

# =========================================================
# ARITHMETIC WITH BOOLEAN
# =========================================================

print(True + True)

print(True + False)

print(False + False)

print(True * 10)

print(False * 100)

# Output
#
# 2
# 1
# 0
# 10
# 0

# =========================================================
# UNARY OPERATORS
# =========================================================
#
# Unary operators operate on one operand.
#

number = 10

print(+number)

print(-number)

# =========================================================
# ABSOLUTE VALUE
# =========================================================

print(abs(-100))

print(abs(25))

# =========================================================
# ROUNDING
# =========================================================

print(round(10.5))

print(round(10.49))

print(round(3.14159, 2))

# =========================================================
# POWER FUNCTION
# =========================================================

print(pow(2, 5))

print(pow(10, 2))

# =========================================================
# DIVMOD FUNCTION
# =========================================================
#
# Returns quotient and remainder.
#

print(divmod(20, 3))

# Output
#
# (6, 2)

quotient, remainder = divmod(20, 3)

print(quotient)

print(remainder)

# =========================================================
# 5. ASSIGNMENT OPERATORS
# =========================================================
#
# Used to assign values to variables.
#

x = 10

print(x)

# =========================================================
# +=
# =========================================================

x = 10

x += 5

print(x)

# Output
#
# 15

# =========================================================
# -=
# =========================================================

x = 20

x -= 5

print(x)

# Output
#
# 15

# =========================================================
# *=
# =========================================================

x = 10

x *= 3

print(x)

# Output
#
# 30

# =========================================================
# /=
# =========================================================

x = 20

x /= 4

print(x)

# Output
#
# 5.0

# =========================================================
# //=
# =========================================================

x = 25

x //= 4

print(x)

# Output
#
# 6

# =========================================================
# %=
# =========================================================

x = 20

x %= 3

print(x)

# Output
#
# 2

# =========================================================
# **=
# =========================================================

x = 5

x **= 2

print(x)

# Output
#
# 25

# =========================================================
# PRACTICE EXAMPLES
# =========================================================

a = 25
b = 4

print(a + b)

print(a - b)

print(a * b)

print(a / b)

print(a // b)

print(a % b)

print(a ** b)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1

# 10 / 2 returns 5.0
#
# Not 5

print(10 / 2)

# ----------------------------

# Mistake 2

# Confusing / and //

print(7 / 2)

print(7 // 2)

# ----------------------------

# Mistake 3

# Using arithmetic on strings

# "Python" - "Java"

# TypeError

# =========================================================
# FILE: 05_operators.py
# PART 2
# =========================================================
#
# INDEX
#
# 6. Comparison Operators
# 7. Logical Operators
# 8. Identity Operators
# 9. Membership Operators
#
# =========================================================
# 6. COMPARISON OPERATORS
# =========================================================
#
# Comparison operators compare two values.
#
# They always return:
#
# True
# or
# False
#

a = 20
b = 10

# =========================================================
# Equal To (==)
# =========================================================

print(a == b)

print(10 == 10)

print("Python" == "Python")

# Output
#
# False
# True
# True

# =========================================================
# Not Equal To (!=)
# =========================================================

print(a != b)

print(10 != 10)

# Output
#
# True
# False

# =========================================================
# Greater Than (>)
# =========================================================

print(a > b)

print(10 > 20)

# =========================================================
# Less Than (<)
# =========================================================

print(a < b)

print(5 < 10)

# =========================================================
# Greater Than or Equal To (>=)
# =========================================================

print(a >= b)

print(20 >= 20)

# =========================================================
# Less Than or Equal To (<=)
# =========================================================

print(a <= b)

print(10 <= 10)

# =========================================================
# COMPARING STRINGS
# =========================================================
#
# Strings are compared lexicographically
# (dictionary order).
#

print("apple" == "apple")

print("apple" < "banana")

print("zebra" > "apple")

print("Python" == "python")

# Python is case-sensitive.

# =========================================================
# COMPARING BOOLEAN VALUES
# =========================================================

print(True == 1)

print(False == 0)

print(True > False)

print(True != False)

# =========================================================
# CHAINED COMPARISON
# =========================================================

age = 25

print(18 <= age <= 60)

marks = 85

print(40 <= marks <= 100)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

salary = 50000

print(salary > 30000)

temperature = 35

print(temperature >= 30)

marks = 45

print(marks >= 35)

# =========================================================
# 7. LOGICAL OPERATORS
# =========================================================
#
# Logical operators combine multiple conditions.
#
# Python provides:
#
# and
# or
# not
#

# =========================================================
# and
# =========================================================
#
# Returns True only if both conditions are True.
#

age = 25
salary = 50000

print(age > 18 and salary > 30000)

print(age > 30 and salary > 30000)

# Truth Table
#
# True  and True  -> True
# True  and False -> False
# False and True  -> False
# False and False -> False

# =========================================================
# or
# =========================================================
#
# Returns True if at least one condition is True.
#

print(age > 18 or salary > 100000)

print(age > 30 or salary > 100000)

# Truth Table
#
# True  or True  -> True
# True  or False -> True
# False or True  -> True
# False or False -> False

# =========================================================
# not
# =========================================================
#
# Reverses the boolean value.
#

print(not True)

print(not False)

print(not (10 > 5))

print(not (5 > 10))

# =========================================================
# LOGICAL OPERATORS WITH BOOLEAN
# =========================================================

is_admin = True
is_logged_in = False

print(is_admin and is_logged_in)

print(is_admin or is_logged_in)

print(not is_logged_in)

# =========================================================
# SHORT-CIRCUIT EVALUATION
# =========================================================
#
# Python stops evaluating as soon as the result
# is determined.
#

print(True or False)

print(False and True)

# Example

a = 10

print(a > 5 and a < 20)

print(a < 5 or a == 10)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

age = 22
has_license = True

print(age >= 18 and has_license)

username = "admin"
password = "1234"

print(username == "admin" and password == "1234")

# =========================================================
# 8. IDENTITY OPERATORS
# =========================================================
#
# Identity operators compare object identity
# (memory location), not values.
#
# Operators:
#
# is
# is not
#

# =========================================================
# is
# =========================================================

a = [10, 20]

b = a

print(a is b)

# Output
#
# True

# =========================================================
# is not
# =========================================================

a = [10, 20]

b = [10, 20]

print(a is not b)

# Output
#
# True

# =========================================================
# == vs is
# =========================================================

list1 = [1, 2, 3]

list2 = [1, 2, 3]

print(list1 == list2)

print(list1 is list2)

# Output
#
# True
# False

# Explanation
#
# ==
# compares values.
#
# is
# compares memory location.

# =========================================================
# USING id()
# =========================================================

x = [1, 2, 3]

y = x

print(id(x))

print(id(y))

print(x is y)

# =========================================================
# None Comparison
# =========================================================

value = None

print(value is None)

print(value is not None)

# Recommended style:
#
# if value is None:
#     ...

# =========================================================
# 9. MEMBERSHIP OPERATORS
# =========================================================
#
# Membership operators check whether
# an element exists inside a sequence.
#
# Operators:
#
# in
# not in
#

# =========================================================
# in
# =========================================================

numbers = [10, 20, 30, 40]

print(20 in numbers)

print(100 in numbers)

# =========================================================
# not in
# =========================================================

print(50 not in numbers)

print(20 not in numbers)

# =========================================================
# MEMBERSHIP IN STRING
# =========================================================

language = "Python Programming"

print("Python" in language)

print("Java" in language)

print("Java" not in language)

# =========================================================
# MEMBERSHIP IN TUPLE
# =========================================================

colors = ("Red", "Green", "Blue")

print("Red" in colors)

print("Black" not in colors)

# =========================================================
# MEMBERSHIP IN SET
# =========================================================

fruits = {"Apple", "Banana", "Mango"}

print("Apple" in fruits)

print("Orange" in fruits)

# =========================================================
# MEMBERSHIP IN DICTIONARY
# =========================================================
#
# Membership checks only keys,
# not values.
#

student = {
    "name": "Amit",
    "age": 20
}

print("name" in student)

print("Amit" in student)

print("Amit" in student.values())

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

email = "amit@gmail.com"

print("@" in email)

languages = ["Python", "Java", "Go"]

print("Python" in languages)

print("Rust" not in languages)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Using is instead of ==

a = 100
b = 100

print(a == b)

print(a is b)

# For value comparison,
# always use ==.

# ---------------------------------------------------------

# Mistake 2
#
# Dictionary membership checks keys.

student = {
    "name": "Amit"
}

print("Amit" in student)

print("Amit" in student.values())

# ---------------------------------------------------------

# Mistake 3
#
# Confusing logical operators.

print(True and False)

print(True or False)

print(not True)

# =========================================================
# FILE: 05_operators.py
# PART 3
# =========================================================
#
# INDEX
#
# 10. Bitwise Operators
# 11. Operator Precedence
# 12. Operator Associativity
# 13. Common Operator Mistakes
# 14. Practical Examples
# 15. Interview Questions
# 16. Quick Revision
#
# =========================================================
# 10. BITWISE OPERATORS
# =========================================================
#
# Bitwise operators work on the binary representation
# of integers.
#
# Binary of 10 -> 1010
# Binary of 5  -> 0101
#
# Operators:
#
# &
# |
# ^
# ~
# <<
# >>
#

a = 10
b = 5

# =========================================================
# Bitwise AND (&)
# =========================================================
#
# Returns 1 only if both bits are 1.
#

print(a & b)

# Binary
#
# 1010
# 0101
# ----
# 0000
#
# Output
#
# 0

# =========================================================
# Bitwise OR (|)
# =========================================================
#
# Returns 1 if either bit is 1.
#

print(a | b)

# Binary
#
# 1010
# 0101
# ----
# 1111
#
# Output
#
# 15

# =========================================================
# Bitwise XOR (^)
# =========================================================
#
# Returns 1 if bits are different.
#

print(a ^ b)

# Binary
#
# 1010
# 0101
# ----
# 1111
#
# Output
#
# 15

# =========================================================
# Bitwise NOT (~)
# =========================================================
#
# Inverts all bits.
#

print(~10)

print(~5)

# Formula:
#
# ~x = -(x + 1)

# =========================================================
# Left Shift (<<)
# =========================================================
#
# Shifts bits to the left.
#
# Equivalent to:
#
# number * (2 ** shift)
#

print(10 << 1)

print(10 << 2)

print(5 << 3)

# Output
#
# 20
# 40
# 40

# =========================================================
# Right Shift (>>)
# =========================================================
#
# Shifts bits to the right.
#
# Equivalent to:
#
# number // (2 ** shift)
#

print(10 >> 1)

print(10 >> 2)

print(20 >> 2)

# Output
#
# 5
# 2
# 5

# =========================================================
# BITWISE ASSIGNMENT OPERATORS
# =========================================================

x = 10

x &= 3

print(x)

# ----------------------------

x = 10

x |= 3

print(x)

# ----------------------------

x = 10

x ^= 3

print(x)

# ----------------------------

x = 10

x <<= 2

print(x)

# ----------------------------

x = 20

x >>= 2

print(x)

# =========================================================
# PRACTICAL BITWISE EXAMPLES
# =========================================================

# Check if a number is even

number = 20

print(number & 1)

# Output
#
# 0 means Even

number = 21

print(number & 1)

# Output
#
# 1 means Odd

# =========================================================
# 11. OPERATOR PRECEDENCE
# =========================================================
#
# Operator precedence determines the order in which
# operators are evaluated.
#
# Highest
#
# ()
# **
# +x -x ~x
# * / // %
# + -
# << >>
# &
# ^
# |
# == != > < >= <=
# not
# and
# or
#
# Lowest
#

# =========================================================
# PRECEDENCE EXAMPLES
# =========================================================

print(2 + 3 * 4)

# Output
#
# 14

print((2 + 3) * 4)

# Output
#
# 20

print(2 ** 3 * 2)

# Output
#
# 16

print(100 / 5 + 10)

# Output
#
# 30.0

print(10 + 5 > 12)

# Output
#
# True

print(True or False and False)

# Output
#
# True

# Because:
#
# and executes before or.

# =========================================================
# 12. OPERATOR ASSOCIATIVITY
# =========================================================
#
# Associativity determines the direction
# in which operators of the same precedence
# are evaluated.
#

# =========================================================
# LEFT TO RIGHT
# =========================================================

print(20 - 5 - 3)

# Evaluates as:
#
# (20 - 5) - 3

# Output
#
# 12

# =========================================================
# RIGHT TO LEFT
# =========================================================

print(2 ** 3 ** 2)

# Evaluates as:
#
# 2 ** (3 ** 2)
#
# = 2 ** 9
#
# = 512

# =========================================================
# 13. COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Confusing ^ with exponent.

print(2 ^ 3)

# Output
#
# 1

# Correct exponent

print(2 ** 3)

# Output
#
# 8

# ---------------------------------------------------------

# Mistake 2
#
# Using = instead of ==

age = 20

print(age == 20)

# ---------------------------------------------------------

# Mistake 3
#
# Confusing is with ==

list1 = [1, 2]

list2 = [1, 2]

print(list1 == list2)

print(list1 is list2)

# ---------------------------------------------------------

# Mistake 4
#
# Dictionary membership

student = {
    "name": "Amit"
}

print("Amit" in student)

print("Amit" in student.values())

# ---------------------------------------------------------

# Mistake 5
#
# Assuming / returns integer

print(10 / 2)

print(type(10 / 2))

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

length = 10
width = 5

area = length * width

print(area)

# ---------------------------------------------------------

radius = 7

pi = 3.14159

area = pi * radius ** 2

print(area)

# ---------------------------------------------------------

marks = 85

print(marks >= 40)

# ---------------------------------------------------------

username = "admin"
password = "1234"

print(
    username == "admin"
    and password == "1234"
)

# ---------------------------------------------------------

numbers = [10, 20, 30]

print(20 in numbers)

# ---------------------------------------------------------

student = {
    "name": "Rahul",
    "age": 22
}

print("name" in student)

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What are operators?
#
# Answer:
# Operators are symbols used to perform operations
# on operands.
#
# ---------------------------------------------------------
#
# Q2. How many types of operators are there in Python?
#
# Answer:
#
# 1. Arithmetic
# 2. Assignment
# 3. Comparison
# 4. Logical
# 5. Identity
# 6. Membership
# 7. Bitwise
#
# ---------------------------------------------------------
#
# Q3. Difference between / and // ?
#
# /
# Returns floating-point division.
#
# //
# Returns floor division.
#
# ---------------------------------------------------------
#
# Q4. Difference between == and is ?
#
# ==
# Compares values.
#
# is
# Compares object identity (memory location).
#
# ---------------------------------------------------------
#
# Q5. Difference between in and is ?
#
# in
# Checks membership.
#
# is
# Checks object identity.
#
# ---------------------------------------------------------
#
# Q6. Which operator is used for exponentiation?
#
# Answer:
#
# **
#
# ---------------------------------------------------------
#
# Q7. Which operator returns the remainder?
#
# Answer:
#
# %
#
# ---------------------------------------------------------
#
# Q8. What is operator precedence?
#
# Answer:
#
# The order in which operators are evaluated.
#
# ---------------------------------------------------------
#
# Q9. Which operator has higher precedence:
# and or or?
#
# Answer:
#
# and
#
# ---------------------------------------------------------
#
# Q10. Does ^ mean exponentiation?
#
# Answer:
#
# No.
#
# ^ is the Bitwise XOR operator.
#
# Exponentiation uses **.
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Operators perform operations on operands.
#
# ✓ Python has 7 categories of operators.
#
# ✓ Arithmetic:
#   +  -  *  /  //  %  **
#
# ✓ Assignment:
#   =  +=  -=  *=  /=  //=  %=  **=
#
# ✓ Comparison:
#   ==  !=  >  <  >=  <=
#
# ✓ Logical:
#   and  or  not
#
# ✓ Identity:
#   is  is not
#
# ✓ Membership:
#   in  not in
#
# ✓ Bitwise:
#   &  |  ^  ~  <<  >>
#
# ✓ == compares values.
#
# ✓ is compares memory location.
#
# ✓ / returns float.
#
# ✓ // returns floor division.
#
# ✓ ** is exponentiation.
#
# ✓ % returns the remainder.
#
# ✓ ^ is Bitwise XOR, not exponentiation.
#
# ✓ Operator precedence controls evaluation order.
#
# ✓ Parentheses () improve readability and override precedence.
#
# =========================================================
# END OF 05_operators.py
# =========================================================
 
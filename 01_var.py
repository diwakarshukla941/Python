# =========================================================

# PYTHON VARIABLES

# =========================================================

#

# INDEX

#

# 1. What is a Variable?

# 2. Why Do We Need Variables?

# 3. Creating Variables

# 4. Allowed Variable Names

# 5. Not Allowed Variable Names

# 6. Python Keywords

# 7. Variable Naming Rules

# 8. Variable Naming Conventions (PEP 8)

# 9. Variable Assignment

# 10. Multiple Variable Assignment

# 11. Variable Reassignment

# 12. Dynamic Typing

# 13. Checking Variable Type

# 14. Deleting Variables

# 15. Case Sensitivity

# 16. Common Beginner Mistakes

# 17. Interview Questions

# 18. Quick Revision

#

# =========================================================

# 1. WHAT IS A VARIABLE?

# =========================================================

#

# A variable is a named container used to store data in memory.

# Instead of writing values repeatedly, we store them inside variables

# and use the variable name whenever needed.

#

# Syntax:

#

# variable_name = value

#

# Example:

#

age = 20
name = "Amit"
salary = 50000
is_student = True

print(age)
print(name)
print(salary)
print(is_student)

# Output:

# 20

# Amit

# 50000

# True

# =========================================================

# 2. WHY DO WE NEED VARIABLES?

# =========================================================

#

# Variables make programs:

#

# • Easy to read

# • Easy to modify

# • Reusable

# • Memory efficient

#

# Without variables:

#

print(50000)
print(50000)
print(50000)

# With variables:

#

salary = 50000

print(salary)
print(salary)
print(salary)

# =========================================================

# 3. CREATING VARIABLES

# =========================================================

#

# Variables are created automatically when a value is assigned.

# Python does NOT require declaring the data type.

#

age = 20
price = 99.99
student = "Amit"
passed = True

print(age)
print(price)
print(student)
print(passed)

# =========================================================

# 4. ALLOWED VARIABLE NAMES

# =========================================================

#

# A variable name CAN:

#

# ✓ Start with a letter

# ✓ Start with an underscore (_)

# ✓ Contain numbers (after the first character)

# ✓ Contain underscores

#

age = 20
student = "Amit"

_total = 450
_ok = True

student1 = "Rahul"
marks2025 = 95

first_name = "Amit"
last_name = "Sharma"

# All of the above are valid variable names.

# =========================================================

# 5. NOT ALLOWED VARIABLE NAMES

# =========================================================

#

# A variable name CANNOT:

#

# ✗ Start with a number

# ✗ Contain spaces

# ✗ Contain special characters

# ✗ Be a Python keyword

#

# Invalid Examples

# 1age = 20

# student name = "Amit"

# salary$ = 50000

# user-name = "John"

# marks@ = 95

# class = "A"

# if = 10

# for = 20

# Correct Versions

age1 = 20
student_name = "Amit"
salary = 50000
user_name = "John"

# =========================================================

# 6. PYTHON KEYWORDS

# =========================================================

#

# Keywords are reserved words used by Python.

# They CANNOT be used as variable names.

#

# Common Keywords:

#

# False

# None

# True

# and

# as

# assert

# async

# await

# break

# class

# continue

# def

# del

# elif

# else

# except

# finally

# for

# from

# global

# if

# import

# in

# is

# lambda

# nonlocal

# not

# or

# pass

# raise

# return

# try

# while

# with

# yield

#these are the list of keywords that are 

import keyword

print(keyword.kwlist)

# =========================================================

# 7. VARIABLE NAMING RULES

# =========================================================

#

# Rule 1:

# Must start with a letter or underscore.

#

# Rule 2:

# Cannot start with a number.

#

# Rule 3:

# Can contain letters, numbers, and underscores.

#

# Rule 4:

# Cannot contain spaces.

#

# Rule 5:

# Cannot contain special characters.

#

# Rule 6:

# Cannot be a Python keyword.

#

# Valid

name = "Amit"
_name = "Rahul"
student1 = "John"
total_marks = 480

# Invalid

# 1student

# student-name

# student name

# total$

# class

# =========================================================

# 8. VARIABLE NAMING CONVENTIONS (PEP 8)

# =========================================================

#

# Python recommends using snake_case for variables.

#

# Good

first_name = "Amit"
last_name = "Sharma"
total_marks = 450
is_logged_in = True

# Avoid

firstName = "Amit"
FirstName = "Amit"
FIRSTNAME = "Amit"

# Explanation:

#

# snake_case -> Variables and Functions

# PascalCase -> Classes

# UPPER_CASE -> Constants

# =========================================================

# 9. VARIABLE ASSIGNMENT

# =========================================================

#

# Assign values using =

#

city = "Mumbai"
temperature = 32

print(city)
print(temperature)

# =========================================================

# 10. MULTIPLE VARIABLE ASSIGNMENT

# =========================================================

a, b, c = 10, 20, 30

print(a)
print(b)
print(c)

# Same value to multiple variables

x = y = z = 100

print(x)
print(y)
print(z)

# =========================================================

# 11. VARIABLE REASSIGNMENT

# =========================================================

#

# Variables can be updated anytime.

#

age = 20
print(age)

age = 21
print(age)

name = "Amit"
name = "Rahul"

print(name)

# Output:

#

# 20

# 21

# Rahul

# =========================================================

# 12. DYNAMIC TYPING

# =========================================================

#

# Python is dynamically typed.

#

# A variable can hold different data types during execution.

#

value = 10
print(value)

value = "Hello"
print(value)

value = True
print(value)

value = 9.99
print(value)

# =========================================================

# 13. CHECKING VARIABLE TYPE

# =========================================================

#

# Use type() to know the data type.

#

age = 20
price = 50.5
name = "Amit"
status = True

print(type(age))
print(type(price))
print(type(name))
print(type(status))

# Output:

#

# <class 'int'>

# <class 'float'>

# <class 'str'>

# <class 'bool'>

# =========================================================

# 14. DELETING VARIABLES

# =========================================================

#

# Use del to delete a variable.

#

marks = 95

print(marks)

del marks

# print(marks)

#

# NameError

# because the variable no longer exists.

# =========================================================

# 15. CASE SENSITIVITY

# =========================================================

#

# Python is case-sensitive.

#

name = "Amit"
Name = "Rahul"
NAME = "John"

print(name)
print(Name)
print(NAME)

# These are three different variables.

# =========================================================

# 16. COMMON BEGINNER MISTAKES

# =========================================================

#

# Mistake 1

#

# Starting with numbers

#

# 1age = 20

#

# Correct:

#

age1 = 20

# ----------------------------------

# Mistake 2

#

# Spaces

#

# first name = "Amit"

#

# Correct:

#

first_name = "Amit"

# ----------------------------------

# Mistake 3

#

# Using keywords

#

# class = "Python"

#

# Correct:

#

class_name = "Python"

# ----------------------------------

# Mistake 4

#

# Forgetting Python is case-sensitive

#

age = 20
Age = 50

print(age)
print(Age)

# =========================================================

# 17. INTERVIEW QUESTIONS

# =========================================================

#

# Q1. What is a variable?

#

# Answer:

# A variable is a named memory location used to store data.

#

# -------------------------------------------------------

#

# Q2. Does Python require variable declaration?

#

# Answer:

# No.

# Variables are created automatically when a value is assigned.

#

# -------------------------------------------------------

#

# Q3. Can a variable start with a number?

#

# Answer:

# No.

#

# -------------------------------------------------------

#

# Q4. Can a variable contain numbers?

#

# Answer:

# Yes.

#

# Example:

#

student1 = "Amit"

# -------------------------------------------------------

#

# Q5. Can a variable start with an underscore?

#

# Answer:

# Yes.

#

_private = "Secret"

# -------------------------------------------------------

#

# Q6. Is Python case-sensitive?

#

# Answer:

# Yes.

#

# name, Name, and NAME are different variables.

#

# -------------------------------------------------------

#

# Q7. Which naming convention is recommended?

#

# Answer:

# snake_case

#

employee_salary = 45000

# =========================================================

# 18. QUICK REVISION

# =========================================================

#

# ✓ Variables store data.

# ✓ Created using = operator.

# ✓ Python is dynamically typed.

# ✓ No declaration required.

# ✓ Start with letter or underscore.

# ✓ Cannot start with numbers.

# ✓ No spaces allowed.

# ✓ No special characters allowed.

# ✓ Cannot use Python keywords.

# ✓ Python is case-sensitive.

# ✓ Follow snake_case naming convention.

# ✓ Use type() to check data type.

# ✓ Use del to delete variables.

# ✓ Variables can be reassigned anytime.

#

# =========================================================

# END OF VARIABLES

# =========================================================

# =========================================================
# PYTHON INPUT & OUTPUT
# =========================================================
#
# INDEX
#
# 1. What is Input and Output?
# 2. Why Input & Output?
# 3. print() Function
# 4. Printing Multiple Values
# 5. sep Parameter
# 6. end Parameter
# 7. Escape Characters
#
# =========================================================
# 1. WHAT IS INPUT AND OUTPUT?
# =========================================================
#
# Input:
# ------
# Data provided by the user or another source.
#
# Output:
# -------
# Information displayed to the user.
#
# Example
#

print("Hello Python")

# Output
#
# Hello Python

# =========================================================
# 2. WHY DO WE NEED INPUT & OUTPUT?
# =========================================================
#
# Programs become interactive using input.
#
# Programs communicate results using output.
#

print("Welcome!")

name = "Amit"

print(name)

# =========================================================
# 3. print() FUNCTION
# =========================================================
#
# print() is used to display output.
#
# Syntax:
#
# print(object)
#

print("Hello")

print(100)

print(99.99)

print(True)

# =========================================================
# PRINTING VARIABLES
# =========================================================

name = "Amit"

age = 20

salary = 45000

print(name)
print(age)
print(salary)

# =========================================================
# PRINTING EXPRESSIONS
# =========================================================

print(10 + 20)

print(100 - 50)

print(10 * 5)

print(20 / 2)

# =========================================================
# PRINTING MULTIPLE VALUES
# =========================================================

name = "Rahul"

age = 22

city = "Mumbai"

print(name, age, city)

# Output
#
# Rahul 22 Mumbai

# =========================================================
# DEFAULT SEPARATOR
# =========================================================
#
# By default, print() separates values using a space.
#

print("Python", "Java", "C++")

# Output
#
# Python Java C++

# =========================================================
# 4. sep PARAMETER
# =========================================================
#
# sep specifies the separator between values.
#
# Syntax:
#
# print(value1, value2, sep="separator")
#

print("Python", "Java", sep="-")

print("2026", "06", "30", sep="/")

print("A", "B", "C", sep=" | ")

# Output
#
# Python-Java
# 2026/06/30
# A | B | C

# =========================================================
# MORE sep EXAMPLES
# =========================================================

print(10, 20, 30, sep=",")

print(10, 20, 30, sep=" -> ")

print("www", "google", "com", sep=".")

print("Python", "Notes", sep="***")

# =========================================================
# 5. end PARAMETER
# =========================================================
#
# end specifies what should be printed
# after the current print() statement.
#
# Default:
#
# end="\n"
#

print("Hello")
print("World")

# Output
#
# Hello
# World

# =========================================================
# CHANGING end
# =========================================================

print("Hello", end=" ")

print("World")

# Output
#
# Hello World

# =========================================================
# MORE end EXAMPLES
# =========================================================

print("Python", end=" -> ")

print("Java", end=" -> ")

print("C++")

# Output
#
# Python -> Java -> C++

print("Loading", end="...")

print("Done")

# =========================================================
# USING sep AND end TOGETHER
# =========================================================

print("A", "B", "C", sep="-", end=" ")

print("Completed")

# Output
#
# A-B-C Completed

# =========================================================
# 6. ESCAPE CHARACTERS
# =========================================================
#
# Escape characters begin with a backslash (\)
# and provide special meaning.
#

# =========================================================
# \n (New Line)
# =========================================================

print("Hello\nPython")

# Output
#
# Hello
# Python

# =========================================================
# \t (Tab Space)
# =========================================================

print("Name\tAge")

print("Amit\t20")

# Output
#
# Name    Age
# Amit    20

# =========================================================
# \\ (Backslash)
# =========================================================

print("C:\\Users\\Amit")

# Output
#
# C:\Users\Amit

# =========================================================
# \' (Single Quote)
# =========================================================

print('It\'s Python')

# Output
#
# It's Python

# =========================================================
# \" (Double Quote)
# =========================================================

print("He said \"Hello\"")

# Output
#
# He said "Hello"

# =========================================================
# \b (Backspace)
# =========================================================

print("ABC\bD")

# Result depends on terminal.
# Generally removes the previous character.

# =========================================================
# \r (Carriage Return)
# =========================================================

print("Hello\rHi")

# Terminal-dependent output.

# =========================================================
# ESCAPE CHARACTER EXAMPLES
# =========================================================

print("Python\nJava\nC++")

print("A\tB\tC")

print("Folder\\File")

print("\"Python\"")

print('\'Programming\'')

# =========================================================
# PRINTING MULTIPLE LINES
# =========================================================

print("""
Python
Java
C++
JavaScript
""")

# =========================================================
# MULTI-LINE STRING
# =========================================================

message = """
Welcome
to
Python Programming
"""

print(message)

# =========================================================
# COMMENTS VS OUTPUT
# =========================================================
#
# Comments are ignored by Python.
#

# This is a comment.

print("This is output.")

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Missing quotes

# print(Hello)

# NameError

# Correct

print("Hello")

# --------------------------

# Forgetting parentheses

# print "Hello"

# SyntaxError (Python 3)

# Correct

print("Hello")

# --------------------------

# Incorrect escape sequence

print("C:\\Python\\Notes")

# =========================================================
# PRACTICE EXAMPLES
# =========================================================

print("My name is Amit.")

print("I am learning Python.")

print("Python", "Java", "JavaScript")

print("Apple", "Banana", "Mango", sep=", ")

print("2026", "06", "30", sep="-")

print("Hello", end=" ")

print("World")

print("A\nB\nC")

print("Roll\tMarks")

print("101\t95")

# =========================================================
# 8. input() FUNCTION
# =========================================================
#
# input() is used to take input from the user.
#
# Syntax:
#
# input("Message")
#
# It always returns a STRING.
#

name = input("Enter your name: ")

print(name)

# =========================================================
# SIMPLE INPUT EXAMPLE
# =========================================================

city = input("Enter your city: ")

print("City:", city)

# =========================================================
# TAKING MULTIPLE INPUTS
# =========================================================

first_name = input("Enter first name: ")

last_name = input("Enter last name: ")

print(first_name, last_name)

# =========================================================
# 9. TYPE OF input()
# =========================================================
#
# Regardless of what the user enters,
# input() always returns a string.
#

age = input("Enter age: ")

print(age)

print(type(age))

# Suppose user enters:
#
# 20
#
# Output:
#
# 20
# <class 'str'>

# =========================================================
# WHY TYPE CONVERSION IS REQUIRED
# =========================================================

age = input("Enter age: ")

# print(age + 10)
#
# TypeError

# Correct

age = int(age)

print(age + 10)

# =========================================================
# INTEGER INPUT
# =========================================================

number = int(input("Enter a number: "))

print(number)

print(type(number))

# =========================================================
# FLOAT INPUT
# =========================================================

price = float(input("Enter price: "))

print(price)

print(type(price))

# =========================================================
# BOOLEAN INPUT
# =========================================================
#
# input() never returns bool automatically.
#

value = input("Enter True or False: ")

print(value)

print(type(value))

# Output
#
# Always string.

# =========================================================
# EXAMPLE
# =========================================================

name = input("Name: ")

age = int(input("Age: "))

salary = float(input("Salary: "))

print(name)
print(age)
print(salary)

# =========================================================
# 10. MULTIPLE INPUTS
# =========================================================
#
# split() separates the input using spaces.
#

name, city = input("Enter name and city: ").split()

print(name)
print(city)

# Example Input
#
# Amit Mumbai

# =========================================================
# THREE INPUTS
# =========================================================

name, age, city = input(
    "Enter name age city: "
).split()

print(name)
print(age)
print(city)

# Example
#
# Amit 20 Mumbai

# =========================================================
# 11. split()
# =========================================================
#
# split() converts a string into a list.
#

text = "Python Java C++"

words = text.split()

print(words)

# Output
#
# ['Python', 'Java', 'C++']

# =========================================================
# SPLIT USING CUSTOM SEPARATOR
# =========================================================

date = "30-06-2026"

parts = date.split("-")

print(parts)

# Output
#
# ['30', '06', '2026']

# =========================================================
# COMMA SEPARATED VALUES
# =========================================================

names = "Amit,Rahul,Rohan"

print(names.split(","))

# =========================================================
# PIPE SEPARATOR
# =========================================================

text = "A|B|C|D"

print(text.split("|"))

# =========================================================
# LIMITING split()
# =========================================================

sentence = "Python is very easy to learn"

print(sentence.split())

print(sentence.split(maxsplit=2))

# Output
#
# ['Python', 'is', 'very easy to learn']

# =========================================================
# TAKING A LIST FROM USER
# =========================================================

numbers = input(
    "Enter numbers separated by spaces: "
).split()

print(numbers)

# Example Input
#
# 10 20 30 40

# Output
#
# ['10', '20', '30', '40']

# =========================================================
# CONVERTING TO INTEGER LIST
# =========================================================

numbers = list(
    map(
        int,
        input("Enter numbers: ").split()
    )
)

print(numbers)

# Example
#
# Input:
#
# 10 20 30
#
# Output:
#
# [10, 20, 30]

# =========================================================
# 12. map()
# =========================================================
#
# map() applies a function
# to every element of an iterable.
#
# Syntax:
#
# map(function, iterable)
#

numbers = ["1", "2", "3"]

result = map(int, numbers)

print(result)

print(list(result))

# Output
#
# [1, 2, 3]

# =========================================================
# map() WITH float()
# =========================================================

prices = ["10.5", "20.25", "30.75"]

prices = list(map(float, prices))

print(prices)

# =========================================================
# map() WITH str()
# =========================================================

numbers = [10, 20, 30]

numbers = list(map(str, numbers))

print(numbers)

# =========================================================
# MULTIPLE INTEGER INPUTS
# =========================================================

a, b = map(
    int,
    input("Enter two numbers: ").split()
)

print(a)
print(b)

print(a + b)

# Example Input
#
# 10 20

# Output
#
# 30

# =========================================================
# THREE INTEGER INPUTS
# =========================================================

x, y, z = map(
    int,
    input("Enter three numbers: ").split()
)

print(x)
print(y)
print(z)

# =========================================================
# FLOAT INPUT USING map()
# =========================================================

a, b = map(
    float,
    input("Enter two decimal numbers: ").split()
)

print(a)
print(b)

# =========================================================
# LIST OF FLOATS
# =========================================================

prices = list(
    map(
        float,
        input("Enter prices: ").split()
    )
)

print(prices)

# =========================================================
# LIST OF STRINGS
# =========================================================

names = input(
    "Enter names: "
).split()

print(names)

# =========================================================
# PRACTICE EXAMPLES
# =========================================================

name = input("Enter your name: ")

print("Welcome", name)

age = int(input("Enter age: "))

print(age + 5)

marks = list(
    map(
        int,
        input("Enter marks: ").split()
    )
)

print(marks)

a, b = map(
    int,
    input("Enter two numbers: ").split()
)

print(a * b)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Assuming input() returns int.

age = input("Age: ")

print(type(age))

# Always str.

# --------------------------

# Mistake 2

# age = input()
# print(age + 10)

# TypeError

# Correct

age = int(input("Age: "))

print(age + 10)

# --------------------------

# Mistake 3

numbers = input().split()

print(numbers)

# Returns list of strings.

# To convert

numbers = list(map(int, numbers))

# --------------------------

# Mistake 4

# name, age = input().split()

# User enters only one value.
#
# ValueError

# User must enter exactly
# the expected number of values.

# =========================================================
# 13. eval()
# =========================================================
#
# eval() evaluates a string as a Python expression.
#
# Syntax:
#
# eval(expression)
#
# NOTE:
# Avoid using eval() with user input because it can
# execute arbitrary Python code and is a security risk.
#

print(eval("10 + 20"))

print(eval("5 * 8"))

# Output
#
# 30
# 40

# ---------------------------------------------------------
# Example
# ---------------------------------------------------------

expression = "100 / 5"

print(eval(expression))

# ---------------------------------------------------------
# User Input (Not Recommended)
# ---------------------------------------------------------

# number = eval(input("Enter a number: "))
#
# Avoid using eval() with untrusted input.

# Prefer this:

number = int(input("Enter an integer: "))

print(number)

# =========================================================
# 14. f-STRINGS
# =========================================================
#
# f-Strings were introduced in Python 3.6.
#
# They provide an easy and readable way to format strings.
#
# Syntax:
#
# f"...{variable}..."
#

name = "Amit"
age = 20

print(f"My name is {name}.")

print(f"My age is {age}.")

# =========================================================
# MULTIPLE VARIABLES
# =========================================================

city = "Mumbai"
salary = 50000

print(f"{name} lives in {city}.")
print(f"Salary = {salary}")

# =========================================================
# EXPRESSIONS INSIDE f-STRINGS
# =========================================================

a = 10
b = 20

print(f"Sum = {a + b}")

print(f"Product = {a * b}")

print(f"Average = {(a + b) / 2}")

# =========================================================
# CALLING FUNCTIONS
# =========================================================

language = "python"

print(f"{language.upper()}")

print(f"Length = {len(language)}")

# =========================================================
# DECIMAL PRECISION
# =========================================================

pi = 3.1415926535

print(f"{pi:.2f}")

print(f"{pi:.3f}")

print(f"{pi:.5f}")

# Output
#
# 3.14
# 3.142
# 3.14159

# =========================================================
# WIDTH FORMATTING
# =========================================================

number = 25

print(f"{number:5}")

print(f"{number:10}")

print(f"{number:05}")

# =========================================================
# LEFT / RIGHT ALIGNMENT
# =========================================================

name = "Python"

print(f"|{name:<15}|")

print(f"|{name:>15}|")

print(f"|{name:^15}|")

# =========================================================
# 15. str.format()
# =========================================================
#
# format() was introduced before f-strings.
#

name = "Rahul"
age = 22

print("Name: {}".format(name))

print("Age: {}".format(age))

# =========================================================
# MULTIPLE VALUES
# =========================================================

print(
    "Name: {} Age: {}".format(name, age)
)

# =========================================================
# POSITIONAL INDEX
# =========================================================

print(
    "{1} {0}".format("Python", "Hello")
)

# Output
#
# Hello Python

# =========================================================
# NAMED PLACEHOLDERS
# =========================================================

print(
    "Name: {name}, Age: {age}".format(
        name="Amit",
        age=20
    )
)

# =========================================================
# DECIMAL FORMATTING
# =========================================================

pi = 3.1415926

print("{:.2f}".format(pi))

print("{:.4f}".format(pi))

# =========================================================
# 16. OLD STYLE (%) FORMATTING
# =========================================================
#
# Older formatting method.
# Still seen in legacy code.
#

name = "Python"

print("Hello %s" % name)

age = 20

print("Age = %d" % age)

price = 99.99

print("Price = %.2f" % price)

# =========================================================
# MULTIPLE VALUES
# =========================================================

name = "Amit"
marks = 95

print(
    "Student: %s Marks: %d"
    % (name, marks)
)

# =========================================================
# COMPARISON OF FORMATTING METHODS
# =========================================================
#
# 1. f-Strings
#    ✓ Fastest
#    ✓ Most readable
#    ✓ Recommended
#
# 2. str.format()
#    ✓ Good
#    ✓ Common in older projects
#
# 3. % Formatting
#    ✓ Legacy
#    ✓ Rarely used in new code
#

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

name = input("Enter your name: ")

print(f"Welcome {name}")

# ---------------------------------------------------------

age = int(input("Enter age: "))

print(f"After 5 years you will be {age + 5}.")

# ---------------------------------------------------------

a, b = map(
    int,
    input("Enter two numbers: ").split()
)

print(f"Addition = {a + b}")

print(f"Subtraction = {a - b}")

print(f"Multiplication = {a * b}")

print(f"Division = {a / b}")

# ---------------------------------------------------------

marks = list(
    map(
        int,
        input("Enter marks: ").split()
    )
)

print(f"Marks = {marks}")

print(f"Total = {sum(marks)}")

print(f"Highest = {max(marks)}")

print(f"Lowest = {min(marks)}")

print(f"Average = {sum(marks) / len(marks):.2f}")

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Forgetting the 'f'

name = "Amit"

print("{name}")

# Output
#
# {name}

# Correct

print(f"{name}")

# ---------------------------------------------------------

# Mistake 2
#
# Mixing string and integer

age = 20

# print("Age = " + age)

# TypeError

# Correct

print("Age = " + str(age))

# Or

print(f"Age = {age}")

# ---------------------------------------------------------

# Mistake 3
#
# Wrong number of variables

# name, age = input().split()
#
# User enters:
#
# Amit
#
# ValueError

# ---------------------------------------------------------

# Mistake 4
#
# Using eval() for user input.

#
# Avoid:
#
# eval(input())
#
# Better:
#
# int(input())
# float(input())

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is input()?
#
# Answer:
# input() reads data from the user and
# always returns a string.
#
# ---------------------------------------------------------
#
# Q2. What is print()?
#
# Answer:
# print() displays output on the console.
#
# ---------------------------------------------------------
#
# Q3. What is the default separator in print()?
#
# Answer:
#
# A single space (" ")
#
# ---------------------------------------------------------
#
# Q4. What is the default value of end?
#
# Answer:
#
# "\n" (newline)
#
# ---------------------------------------------------------
#
# Q5. Why is int(input()) commonly used?
#
# Answer:
#
# Because input() returns a string.
#
# int() converts it into an integer.
#
# ---------------------------------------------------------
#
# Q6. Difference between split() and map()?
#
# split()
# -------
# Splits a string into a list of strings.
#
# map()
# -----
# Applies a function to every element.
#
# ---------------------------------------------------------
#
# Q7. Which string formatting method is recommended?
#
# Answer:
#
# f-Strings
#
# ---------------------------------------------------------
#
# Q8. Why should eval() be avoided?
#
# Answer:
#
# It can execute arbitrary Python code and
# is unsafe for user input.
#
# ---------------------------------------------------------
#
# Q9. Name three string formatting methods.
#
# Answer:
#
# 1. f-Strings
# 2. str.format()
# 3. % Formatting
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ print() displays output.
#
# ✓ input() takes user input.
#
# ✓ input() always returns a string.
#
# ✓ Use int() or float() to convert numeric input.
#
# ✓ split() converts a string into a list.
#
# ✓ map() applies a function to every element.
#
# ✓ list(map(int, input().split()))
#   is commonly used to read a list of integers.
#
# ✓ sep changes the separator in print().
#
# ✓ end changes what is printed after print().
#
# ✓ Escape characters:
#   \n  New Line
#   \t  Tab
#   \\  Backslash
#   \"  Double Quote
#   \'  Single Quote
#
# ✓ Prefer f-Strings for formatting.
#
# ✓ Avoid eval() with user input.
#
# =========================================================
# END OF 04_input_output.py
# ========================================================= 
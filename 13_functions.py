# =========================================================
# FILE: 13_functions.py
# PART 1
# =========================================================
#
# PYTHON FUNCTIONS
#
# INDEX
#
# 1. What is a Function?
# 2. Why Functions?
# 3. Creating Functions
# 4. Calling Functions
# 5. Parameters
# 6. Arguments
# 7. Return Statement
# 8. Local Variables
#
# =========================================================
# 1. WHAT IS A FUNCTION?
# =========================================================
#
# A function is a reusable block of code that performs
# a specific task.
#
# Instead of writing the same code multiple times,
# we write it once inside a function and call it
# whenever needed.
#
# Syntax:
#
# def function_name(parameters):
#     statements
#

# =========================================================
# SIMPLE FUNCTION
# =========================================================

def greet():
    print("Hello Python")

greet()

# =========================================================
# 2. WHY FUNCTIONS?
# =========================================================
#
# Functions help us:
#
# • Reuse code
# • Improve readability
# • Reduce duplication
# • Simplify debugging
# • Organize programs
#

# Without Function

print("Welcome")
print("Welcome")
print("Welcome")

# With Function

def welcome():
    print("Welcome")

welcome()
welcome()
welcome()

# =========================================================
# 3. CREATING FUNCTIONS
# =========================================================

def say_hello():
    print("Hello")

say_hello()

# =========================================================
# FUNCTION WITH MULTIPLE STATEMENTS
# =========================================================

def display_info():
    print("Python")
    print("Version 3")
    print("Programming Language")

display_info()

# =========================================================
# EMPTY FUNCTION
# =========================================================

def future_feature():
    pass

# =========================================================
# FUNCTION NAMING
# =========================================================
#
# Good:
#

def calculate_total():
    pass

def get_user():
    pass

def is_valid():
    pass

# Bad:
#
# def A():
# def X():
# def abc123():
#

# =========================================================
# 4. CALLING FUNCTIONS
# =========================================================

def message():
    print("Learning Python")

message()

message()

message()

# =========================================================
# EXECUTION FLOW
# =========================================================

print("Start")

def hello():
    print("Inside Function")

hello()

print("End")

# =========================================================
# 5. PARAMETERS
# =========================================================
#
# Parameters are variables declared
# in the function definition.
#

def greet(name):
    print("Hello", name)

greet("Amit")

greet("Rahul")

# =========================================================
# MULTIPLE PARAMETERS
# =========================================================

def student(name, age):

    print(name)

    print(age)

student(
    "Amit",
    20
)

# =========================================================
# THREE PARAMETERS
# =========================================================

def employee(name, department, salary):

    print(name)

    print(department)

    print(salary)

employee(
    "Diwakar",
    "Backend",
    70000
)

# =========================================================
# 6. ARGUMENTS
# =========================================================
#
# Arguments are the actual values passed
# while calling a function.
#

def add(a, b):
    print(a + b)

add(10, 20)

add(50, 30)

# =========================================================
# STRING ARGUMENTS
# =========================================================

def welcome_user(name):
    print("Welcome", name)

welcome_user("Python")

# =========================================================
# BOOLEAN ARGUMENTS
# =========================================================

def login(status):

    if status:
        print("Login Successful")

login(True)

# =========================================================
# 7. RETURN STATEMENT
# =========================================================
#
# return sends a value back to
# the caller.
#

def square(number):
    return number ** 2

result = square(5)

print(result)

# =========================================================
# RETURNING STRINGS
# =========================================================

def full_name(first, last):
    return first + " " + last

print(
    full_name(
        "Amit",
        "Sharma"
    )
)

# =========================================================
# RETURNING BOOLEAN
# =========================================================

def is_even(number):
    return number % 2 == 0

print(is_even(10))

print(is_even(7))

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

# =========================================================
# RETURN ENDS FUNCTION
# =========================================================

def demo():

    print("Before Return")

    return

    print("After Return")

demo()

# =========================================================
# 8. LOCAL VARIABLES
# =========================================================
#
# Variables declared inside a function
# exist only within that function.
#

def example():

    message = "Local Variable"

    print(message)

example()

# print(message)

# NameError

# =========================================================
# LOCAL SCOPE
# =========================================================

def calculate_sum():

    a = 10
    b = 20

    print(a + b)

calculate_sum()

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1

def multiply(a, b):
    return a * b

print(multiply(5, 6))

# ---------------------------------------------------------

# Example 2

def greet_user(name):
    print(f"Hello {name}")

greet_user("Diwakar")

# ---------------------------------------------------------

# Example 3

def cube(number):
    return number ** 3

print(cube(4))

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Forgetting parentheses.

def hello():
    print("Hello")

hello()

# Wrong
#
# hello

# ---------------------------------------------------------

# Mistake 2
#
# Forgetting return.

def add(a, b):
    return a + b

print(add(5, 7))

# ---------------------------------------------------------

# Mistake 3
#
# Accessing local variables outside
# the function.

def sample():
    x = 100

# print(x)

# NameError

# =========================================================
# FILE: 13_functions.py
# PART 2
# =========================================================
#
# PYTHON FUNCTIONS
#
# INDEX
#
# 9. Default Parameters
# 10. Keyword Arguments
# 11. Positional Arguments
# 12. Variable-Length Arguments
# 13. Lambda Functions
# 14. Scope (Global & Local)
#
# =========================================================
# 9. DEFAULT PARAMETERS
# =========================================================
#
# Default parameters allow a function
# to use a predefined value when an
# argument is not provided.
#

# =========================================================
# BASIC EXAMPLE
# =========================================================

def greet(name="Guest"):
    print(f"Hello {name}")

greet()

greet("Amit")

# =========================================================
# MULTIPLE DEFAULT PARAMETERS
# =========================================================

def employee(
    name,
    department="Backend",
    salary=50000
):
    print(name)
    print(department)
    print(salary)

employee("Diwakar")

employee(
    "Rahul",
    "Frontend",
    70000
)

# =========================================================
# MIXING REQUIRED & DEFAULT PARAMETERS
# =========================================================

def student(
    name,
    age,
    city="Mumbai"
):
    print(name)
    print(age)
    print(city)

student(
    "Amit",
    20
)

student(
    "Rahul",
    22,
    "Delhi"
)

# =========================================================
# IMPORTANT RULE
# =========================================================
#
# Non-default parameters must come
# before default parameters.
#

# Correct

def demo(a, b=10):
    print(a, b)

# Wrong

# def demo(a=10, b):
#     pass

# SyntaxError

# =========================================================
# 10. KEYWORD ARGUMENTS
# =========================================================
#
# Arguments can be passed using
# parameter names.
#

def person(name, age, city):
    print(name)
    print(age)
    print(city)

person(
    name="Amit",
    age=20,
    city="Mumbai"
)

# =========================================================
# ORDER DOES NOT MATTER
# =========================================================

person(
    city="Delhi",
    name="Rahul",
    age=22
)

# =========================================================
# MIXING POSITIONAL & KEYWORD
# =========================================================

person(
    "Rohan",
    city="Pune",
    age=25
)

# =========================================================
# INVALID
# =========================================================

# person(
#     name="Amit",
#     20,
#     "Mumbai"
# )

# SyntaxError

# =========================================================
# 11. POSITIONAL ARGUMENTS
# =========================================================
#
# Values are matched by position.
#

def subtract(a, b):
    print(a - b)

subtract(20, 10)

subtract(10, 20)

# =========================================================
# POSITION MATTERS
# =========================================================

def display(first, second):
    print(first)
    print(second)

display(
    "Python",
    "Java"
)

# =========================================================
# 12. VARIABLE-LENGTH ARGUMENTS
# =========================================================
#
# *args
#
# Collects positional arguments
# into a tuple.
#

def total(*numbers):

    print(numbers)

    print(type(numbers))

total(
    10,
    20,
    30
)

# =========================================================
# SUM USING *args
# =========================================================

def add(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total

print(add(10, 20))

print(add(10, 20, 30, 40))

# =========================================================
# **kwargs
# =========================================================
#
# Collects keyword arguments
# into a dictionary.
#

def details(**data):

    print(data)

details(
    name="Amit",
    age=20,
    city="Mumbai"
)

# =========================================================
# ITERATING kwargs
# =========================================================

def employee_details(**employee):

    for key, value in employee.items():
        print(key, value)

employee_details(
    name="Diwakar",
    department="Backend",
    salary=70000
)

# =========================================================
# *args + **kwargs
# =========================================================

def demo(*args, **kwargs):

    print(args)

    print(kwargs)

demo(
    10,
    20,
    30,
    name="Python",
    version=3
)

# =========================================================
# 13. LAMBDA FUNCTIONS
# =========================================================
#
# Anonymous (nameless) functions.
#
# Syntax:
#
# lambda parameters: expression
#

square = lambda number: number ** 2

print(square(5))

# =========================================================
# ADDITION
# =========================================================

add = lambda a, b: a + b

print(add(10, 20))

# =========================================================
# EVEN CHECK
# =========================================================

is_even = lambda number: number % 2 == 0

print(is_even(10))

print(is_even(7))

# =========================================================
# SORTING USING LAMBDA
# =========================================================

students = [
    ("Amit", 80),
    ("Rahul", 95),
    ("Rohan", 75)
]

students.sort(
    key=lambda student: student[1]
)

print(students)

# =========================================================
# MAP
# =========================================================

numbers = [
    1,
    2,
    3,
    4
]

result = map(
    lambda number: number ** 2,
    numbers
)

print(list(result))

# =========================================================
# FILTER
# =========================================================

numbers = [
    10,
    15,
    20,
    25
]

result = filter(
    lambda number: number % 2 == 0,
    numbers
)

print(list(result))

# =========================================================
# 14. SCOPE
# =========================================================
#
# Global Scope
# Local Scope
#

message = "Global Variable"

def show():

    print(message)

show()

# =========================================================
# LOCAL VARIABLE
# =========================================================

def demo():

    value = 100

    print(value)

demo()

# =========================================================
# LOCAL SHADOWS GLOBAL
# =========================================================

name = "Python"

def language():

    name = "Java"

    print(name)

language()

print(name)

# =========================================================
# global KEYWORD
# =========================================================

count = 0

def increment():

    global count

    count += 1

increment()

print(count)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1

def power(
    number,
    exponent=2
):
    return number ** exponent

print(power(5))

print(power(2, 5))

# ---------------------------------------------------------

# Example 2

def average(*numbers):

    return sum(numbers) / len(numbers)

print(
    average(
        10,
        20,
        30,
        40
    )
)

# ---------------------------------------------------------

# Example 3

multiply = lambda a, b: a * b

print(
    multiply(
        6,
        8
    )
)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Default parameter before
# required parameter.

# def demo(a=10, b):
#     pass

# ---------------------------------------------------------

# Mistake 2
#
# Forgetting return.

def add(a, b):

    return a + b

print(add(5, 6))

# ---------------------------------------------------------

# Mistake 3
#
# Accessing local variables
# outside the function.

def sample():

    value = 10

# print(value)

# NameError

# ---------------------------------------------------------

# Mistake 4
#
# Modifying global variables
# without global keyword.

count = 0

# def increase():
#     count += 1

# UnboundLocalError

# =========================================================
# FILE: 13_functions.py
# PART 3
# =========================================================
#
# PYTHON FUNCTIONS
#
# INDEX
#
# 15. Recursion
# 16. Higher-Order Functions
# 17. Decorators (Introduction)
# 18. First-Class Functions
# 19. Closures (Introduction)
# 20. Practical Examples
# 21. Common Beginner Mistakes
# 22. Interview Questions
# 23. Quick Revision
#
# =========================================================
# 15. RECURSION
# =========================================================
#
# Recursion is a technique where a function
# calls itself.
#
# Every recursive function must have:
#
# 1. Base Case
# 2. Recursive Case
#

# =========================================================
# BASIC EXAMPLE
# =========================================================

def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)

countdown(5)

# Output
#
# 5
# 4
# 3
# 2
# 1

# =========================================================
# FACTORIAL
# =========================================================

def factorial(number):

    if number == 0:
        return 1

    return number * factorial(number - 1)

print(factorial(5))

# Output
#
# 120

# =========================================================
# SUM OF N NUMBERS
# =========================================================

def total(number):

    if number == 1:
        return 1

    return number + total(number - 1)

print(total(5))

# Output
#
# 15

# =========================================================
# FIBONACCI
# =========================================================

def fibonacci(number):

    if number <= 1:
        return number

    return (
        fibonacci(number - 1)
        +
        fibonacci(number - 2)
    )

for number in range(10):
    print(fibonacci(number))

# =========================================================
# 16. HIGHER-ORDER FUNCTIONS
# =========================================================
#
# A Higher-Order Function:
#
# • Accepts another function as an argument
# • Returns another function
#

# =========================================================
# FUNCTION AS ARGUMENT
# =========================================================

def greet(name):
    return f"Hello {name}"

def execute(function, value):
    print(function(value))

execute(greet, "Diwakar")

# =========================================================
# RETURNING FUNCTIONS
# =========================================================

def outer():

    def inner():
        print("Inner Function")

    return inner

result = outer()

result()

# =========================================================
# map()
# =========================================================

numbers = [
    1,
    2,
    3,
    4
]

result = map(
    lambda number: number ** 2,
    numbers
)

print(list(result))

# =========================================================
# filter()
# =========================================================

numbers = [
    10,
    15,
    20,
    25
]

result = filter(
    lambda number: number % 2 == 0,
    numbers
)

print(list(result))

# =========================================================
# sorted()
# =========================================================

students = [
    ("Amit", 90),
    ("Rahul", 80),
    ("Rohan", 95)
]

sorted_students = sorted(
    students,
    key=lambda student: student[1]
)

print(sorted_students)

# =========================================================
# 17. DECORATORS (INTRODUCTION)
# =========================================================
#
# Decorators modify or extend the behavior
# of another function.
#

def decorator(function):

    def wrapper():

        print("Before Function")

        function()

        print("After Function")

    return wrapper

@decorator
def hello():
    print("Hello Python")

hello()

# =========================================================
# DECORATOR WITHOUT @
# =========================================================

def greet():
    print("Welcome")

decorated = decorator(greet)

decorated()

# =========================================================
# 18. FIRST-CLASS FUNCTIONS
# =========================================================
#
# Functions are objects in Python.
#

def message():
    print("Hello")

greet_user = message

greet_user()

# =========================================================
# FUNCTIONS INSIDE LISTS
# =========================================================

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

operations = [
    add,
    multiply
]

print(
    operations[0](10, 20)
)

print(
    operations[1](10, 20)
)

# =========================================================
# 19. CLOSURES (INTRODUCTION)
# =========================================================
#
# A closure remembers variables from
# its enclosing scope.
#

def outer(name):

    def inner():
        print(name)

    return inner

hello = outer("Python")

hello()

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1
# Recursive Power

def power(number, exponent):

    if exponent == 0:
        return 1

    return number * power(
        number,
        exponent - 1
    )

print(power(2, 5))

# ---------------------------------------------------------

# Example 2
# Recursive Reverse String

def reverse(text):

    if len(text) == 0:
        return ""

    return (
        reverse(text[1:])
        + text[0]
    )

print(reverse("Python"))

# ---------------------------------------------------------

# Example 3
# Lambda Sorting

employees = [
    {
        "name": "Amit",
        "salary": 50000
    },
    {
        "name": "Rahul",
        "salary": 70000
    },
    {
        "name": "Rohan",
        "salary": 60000
    }
]

employees.sort(
    key=lambda employee: employee["salary"]
)

print(employees)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Forgetting the base case.

# def infinite():
#     return infinite()

# RecursionError

# ---------------------------------------------------------

# Mistake 2
#
# Forgetting to return.

def square(number):
    return number ** 2

print(square(5))

# ---------------------------------------------------------

# Mistake 3
#
# Calling instead of passing a function.

def hello():
    print("Hello")

# Wrong
#
# execute(hello(), "Python")

# Correct
#
# execute(hello, "Python")

# ---------------------------------------------------------

# Mistake 4
#
# Lambda functions can contain
# only one expression.

square = lambda number: number ** 2

print(square(6))

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is recursion?
#
# Answer:
# A function calling itself.
#
# ---------------------------------------------------------
#
# Q2. What is the base case?
#
# Answer:
# The stopping condition of recursion.
#
# ---------------------------------------------------------
#
# Q3. What is a Higher-Order Function?
#
# Answer:
# A function that accepts or returns
# another function.
#
# ---------------------------------------------------------
#
# Q4. What are first-class functions?
#
# Answer:
# Functions treated like any other object.
#
# ---------------------------------------------------------
#
# Q5. What is a decorator?
#
# Answer:
# A function that modifies another function.
#
# ---------------------------------------------------------
#
# Q6. What is a closure?
#
# Answer:
# A nested function that remembers
# variables from its enclosing scope.
#
# ---------------------------------------------------------
#
# Q7. Difference between map() and filter()?
#
# map()
# -----
# Transforms every element.
#
# filter()
# --------
# Keeps only matching elements.
#
# ---------------------------------------------------------
#
# Q8. Can a function return another function?
#
# Answer:
#
# Yes.
#
# ---------------------------------------------------------
#
# Q9. What error occurs in infinite recursion?
#
# Answer:
#
# RecursionError
#
# ---------------------------------------------------------
#
# Q10. Can functions be stored inside
# lists or dictionaries?
#
# Answer:
#
# Yes.
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Functions improve code reuse.
#
# ✓ Parameters receive values.
#
# ✓ Arguments pass values.
#
# ✓ return sends values back.
#
# ✓ Default parameters simplify function calls.
#
# ✓ *args collects positional arguments.
#
# ✓ **kwargs collects keyword arguments.
#
# ✓ Lambda functions are anonymous functions.
#
# ✓ Recursion requires a base case.
#
# ✓ Higher-order functions accept or return functions.
#
# ✓ Decorators modify function behavior.
#
# ✓ Closures remember enclosing variables.
#
# ✓ Functions are first-class objects in Python.
#
# =========================================================
# END OF 13_functions.py
# =========================================================
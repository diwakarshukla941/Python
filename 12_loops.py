# =========================================================
# FILE: 12_loops.py
# PART 1
# =========================================================
#
# PYTHON LOOPS
#
# INDEX
#
# 1. What are Loops?
# 2. Why Loops?
# 3. while Loop
# 4. Infinite Loop
# 5. for Loop
# 6. range()
# 7. Iterating Strings
#
# =========================================================
# 1. WHAT ARE LOOPS?
# =========================================================
#
# Loops allow us to execute a block of code
# repeatedly until a condition becomes False
# or until all elements of an iterable are processed.
#
# Python has two loop types:
#
# • while
# • for
#

# =========================================================
# WHY LOOPS?
# =========================================================
#
# Without loops:
#

print("Hello")
print("Hello")
print("Hello")
print("Hello")
print("Hello")

# With loops:
#

for _ in range(5):
    print("Hello")

# =========================================================
# 2. while LOOP
# =========================================================
#
# Syntax:
#
# while condition:
#     statements
#

count = 1

while count <= 5:
    print(count)
    count += 1

# =========================================================
# COUNTDOWN
# =========================================================

number = 5

while number >= 1:
    print(number)
    number -= 1

print("Blast Off!")

# =========================================================
# SUM OF NUMBERS
# =========================================================

total = 0
number = 1

while number <= 5:
    total += number
    number += 1

print(total)

# Output
#
# 15

# =========================================================
# MULTIPLICATION TABLE
# =========================================================

number = 7
i = 1

while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# =========================================================
# USER INPUT
# =========================================================

password = ""

while password != "python123":
    password = input("Enter Password: ")

print("Access Granted")

# =========================================================
# 3. INFINITE LOOP
# =========================================================
#
# A loop that never ends.
#

# while True:
#     print("Running...")

# Stop using:
#
# Ctrl + C

# =========================================================
# BREAKING AN INFINITE LOOP
# =========================================================

count = 1

while True:

    print(count)

    if count == 5:
        break

    count += 1

# =========================================================
# 4. for LOOP
# =========================================================
#
# Used to iterate over an iterable.
#

languages = [
    "Python",
    "Java",
    "Go"
]

for language in languages:
    print(language)

# =========================================================
# TUPLE
# =========================================================

numbers = (
    10,
    20,
    30
)

for number in numbers:
    print(number)

# =========================================================
# SET
# =========================================================

numbers = {
    1,
    2,
    3
}

for number in numbers:
    print(number)

# =========================================================
# DICTIONARY
# =========================================================

student = {
    "name": "Amit",
    "age": 20
}

for key in student:
    print(key)

# =========================================================
# VALUES
# =========================================================

for value in student.values():
    print(value)

# =========================================================
# ITEMS
# =========================================================

for key, value in student.items():
    print(key, value)

# =========================================================
# 5. range()
# =========================================================
#
# range(stop)
# range(start, stop)
# range(start, stop, step)
#

# =========================================================
# range(stop)
# =========================================================

for number in range(5):
    print(number)

# Output
#
# 0 1 2 3 4

# =========================================================
# range(start, stop)
# =========================================================

for number in range(5, 10):
    print(number)

# =========================================================
# range(start, stop, step)
# =========================================================

for number in range(2, 21, 2):
    print(number)

# =========================================================
# NEGATIVE STEP
# =========================================================

for number in range(10, 0, -1):
    print(number)

# =========================================================
# CONVERT TO LIST
# =========================================================

numbers = list(range(5))

print(numbers)

# =========================================================
# 6. ITERATING STRINGS
# =========================================================

text = "Python"

for character in text:
    print(character)

# =========================================================
# USING enumerate()
# =========================================================

for index, character in enumerate(text):
    print(index, character)

# =========================================================
# USING INDEX
# =========================================================

for index in range(len(text)):
    print(index, text[index])

# =========================================================
# LOOP VARIABLES
# =========================================================

for number in range(3):
    print(number)

print("Finished")

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1
# Print Squares

for number in range(1, 6):
    print(number ** 2)

# ---------------------------------------------------------

# Example 2
# Sum of Even Numbers

total = 0

for number in range(2, 11, 2):
    total += number

print(total)

# ---------------------------------------------------------

# Example 3
# Reverse Countdown

for number in range(5, 0, -1):
    print(number)

print("Done")

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Forgetting to update while variable.

count = 1

# while count <= 5:
#     print(count)

# Infinite Loop

# ---------------------------------------------------------

# Mistake 2
#
# Confusing range(5)

for number in range(5):
    print(number)

# Output:
#
# 0 1 2 3 4

# ---------------------------------------------------------

# Mistake 3
#
# Using range() with strings.

text = "Python"

# range(text)

# TypeError

# =========================================================
# END OF PART 1
# =========================================================
#
# Next Part:
#
# 8. break
# 9. continue
# 10. pass
# 11. Nested Loops
# 12. Loop else
#
# =========================================================


# =========================================================
# FILE: 12_loops.py
# PART 2
# =========================================================
#
# PYTHON LOOPS
#
# INDEX
#
# 8. break Statement
# 9. continue Statement
# 10. pass Statement
# 11. Nested Loops
# 12. else with Loops
# 13. enumerate()
# 14. zip()
#
# =========================================================
# 8. break STATEMENT
# =========================================================
#
# break immediately terminates the loop.
#

# =========================================================
# BASIC EXAMPLE
# =========================================================

for number in range(1, 11):

    if number == 6:
        break

    print(number)

# Output
#
# 1 2 3 4 5

# =========================================================
# while WITH break
# =========================================================

count = 1

while True:

    print(count)

    if count == 5:
        break

    count += 1

# =========================================================
# SEARCH EXAMPLE
# =========================================================

numbers = [
    10,
    20,
    30,
    40,
    50
]

target = 30

for number in numbers:

    if number == target:
        print("Found")
        break

# =========================================================
# PASSWORD EXAMPLE
# =========================================================

while True:

    password = input("Password: ")

    if password == "python123":
        print("Login Successful")
        break

    print("Incorrect Password")

# =========================================================
# 9. continue STATEMENT
# =========================================================
#
# continue skips the current iteration
# and moves to the next one.
#

# =========================================================
# BASIC EXAMPLE
# =========================================================

for number in range(1, 6):

    if number == 3:
        continue

    print(number)

# Output
#
# 1 2 4 5

# =========================================================
# SKIP EVEN NUMBERS
# =========================================================

for number in range(1, 11):

    if number % 2 == 0:
        continue

    print(number)

# =========================================================
# SKIP EMPTY STRINGS
# =========================================================

names = [
    "Amit",
    "",
    "Rahul",
    "",
    "Diwakar"
]

for name in names:

    if name == "":
        continue

    print(name)

# =========================================================
# 10. pass STATEMENT
# =========================================================
#
# pass does nothing.
#
# It acts as a placeholder.
#

for number in range(5):
    pass

print("Loop Completed")

# =========================================================
# FUNCTION
# =========================================================

def future_feature():
    pass

# =========================================================
# CLASS
# =========================================================

class Student:
    pass

# =========================================================
# 11. NESTED LOOPS
# =========================================================
#
# A loop inside another loop.
#

# =========================================================
# BASIC EXAMPLE
# =========================================================

for i in range(1, 4):

    for j in range(1, 4):

        print(i, j)

# =========================================================
# MULTIPLICATION TABLE
# =========================================================

for i in range(1, 6):

    for j in range(1, 6):

        print(i * j, end="\t")

    print()

# =========================================================
# STAR PATTERN
# =========================================================

for row in range(5):

    for column in range(row + 1):

        print("*", end=" ")

    print()

# Output
#
# *
# * *
# * * *
# * * * *
# * * * * *

# =========================================================
# RECTANGLE PATTERN
# =========================================================

rows = 4
columns = 5

for i in range(rows):

    for j in range(columns):

        print("*", end=" ")

    print()

# =========================================================
# 12. LOOP else
# =========================================================
#
# else executes only if the loop
# finishes normally.
#
# If break executes,
# else will NOT run.
#

# =========================================================
# for-else
# =========================================================

for number in range(5):
    print(number)

else:
    print("Loop Completed")

# =========================================================
# break PREVENTS else
# =========================================================

for number in range(5):

    if number == 3:
        break

    print(number)

else:
    print("Completed")

# else does not execute.

# =========================================================
# SEARCH EXAMPLE
# =========================================================

numbers = [
    10,
    20,
    30,
    40
]

target = 50

for number in numbers:

    if number == target:
        print("Found")
        break

else:
    print("Not Found")

# =========================================================
# while-else
# =========================================================

count = 1

while count <= 3:

    print(count)

    count += 1

else:
    print("While Finished")

# =========================================================
# 13. enumerate()
# =========================================================
#
# enumerate() provides index and value.
#

languages = [
    "Python",
    "Java",
    "Go"
]

for index, language in enumerate(languages):

    print(index, language)

# =========================================================
# START VALUE
# =========================================================

for index, language in enumerate(
    languages,
    start=1
):
    print(index, language)

# =========================================================
# 14. zip()
# =========================================================
#
# zip() iterates over multiple iterables.
#

names = [
    "Amit",
    "Rahul",
    "Rohan"
]

marks = [
    90,
    80,
    95
]

for name, mark in zip(names, marks):

    print(name, mark)

# =========================================================
# MULTIPLE LISTS
# =========================================================

cities = [
    "Mumbai",
    "Delhi",
    "Pune"
]

for name, city in zip(names, cities):

    print(name, city)

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1
# Print Only Odd Numbers

for number in range(1, 21):

    if number % 2 == 0:
        continue

    print(number)

# ---------------------------------------------------------

# Example 2
# Stop at First Negative Number

numbers = [
    10,
    20,
    30,
    -5,
    50
]

for number in numbers:

    if number < 0:
        break

    print(number)

# ---------------------------------------------------------

# Example 3
# Student Marks

students = [
    "Amit",
    "Rahul",
    "Diwakar"
]

marks = [
    95,
    88,
    91
]

for student, mark in zip(students, marks):

    print(student, mark)

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Confusing break and continue.

for number in range(5):

    if number == 2:
        continue

    print(number)

# ---------------------------------------------------------

# Mistake 2
#
# Forgetting print() after end=""

for number in range(3):

    print("*", end=" ")

print()

# ---------------------------------------------------------

# Mistake 3
#
# Assuming else always executes.

for number in range(5):

    if number == 2:
        break

else:
    print("Completed")

# else will not execute.


# =========================================================
# FILE: 12_loops.py
# PART 3
# =========================================================
#
# PYTHON LOOPS
#
# INDEX
#
# 15. Comprehensions
# 16. Real-World Examples
# 17. Common Beginner Mistakes
# 18. Interview Questions
# 19. Quick Revision
#
# =========================================================
# 15. COMPREHENSIONS
# =========================================================
#
# Python provides:
#
# • List Comprehension
# • Set Comprehension
# • Dictionary Comprehension
#
# They provide a concise way to create collections.
#

# =========================================================
# LIST COMPREHENSION
# =========================================================

numbers = [
    number
    for number in range(1, 6)
]

print(numbers)

# =========================================================
# SQUARES
# =========================================================

squares = [
    number ** 2
    for number in range(1, 6)
]

print(squares)

# =========================================================
# EVEN NUMBERS
# =========================================================

evens = [
    number
    for number in range(20)
    if number % 2 == 0
]

print(evens)

# =========================================================
# ODD NUMBERS
# =========================================================

odds = [
    number
    for number in range(20)
    if number % 2 != 0
]

print(odds)

# =========================================================
# SET COMPREHENSION
# =========================================================

unique_squares = {
    number ** 2
    for number in range(1, 6)
}

print(unique_squares)

# =========================================================
# DICTIONARY COMPREHENSION
# =========================================================

square_dict = {
    number: number ** 2
    for number in range(1, 6)
}

print(square_dict)

# =========================================================
# CONDITIONAL EXPRESSION
# =========================================================

result = [
    "Even"
    if number % 2 == 0
    else "Odd"
    for number in range(1, 6)
]

print(result)

# =========================================================
# 16. REAL-WORLD EXAMPLES
# =========================================================

# =========================================================
# Example 1
# Sum of Numbers
# =========================================================

total = 0

for number in range(1, 101):
    total += number

print(total)

# =========================================================
# Example 2
# Factorial
# =========================================================

number = 5

factorial = 1

for value in range(1, number + 1):
    factorial *= value

print(factorial)

# =========================================================
# Example 3
# Prime Number
# =========================================================

number = 17

is_prime = True

if number <= 1:
    is_prime = False

else:

    for divisor in range(2, number):

        if number % divisor == 0:
            is_prime = False
            break

print(is_prime)

# =========================================================
# Example 4
# Reverse String
# =========================================================

text = "Python"

reverse = ""

for character in text:
    reverse = character + reverse

print(reverse)

# =========================================================
# Example 5
# Count Vowels
# =========================================================

text = "Programming"

count = 0

for character in text.lower():

    if character in "aeiou":
        count += 1

print(count)

# =========================================================
# Example 6
# Largest Number
# =========================================================

numbers = [
    15,
    70,
    32,
    98,
    54
]

largest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

print(largest)

# =========================================================
# Example 7
# Multiplication Table
# =========================================================

number = 8

for i in range(1, 11):

    print(
        f"{number} x {i} = {number * i}"
    )

# =========================================================
# Example 8
# Fibonacci Series
# =========================================================

first = 0
second = 1

for _ in range(10):

    print(first)

    first, second = second, first + second

# =========================================================
# Example 9
# Count Digits
# =========================================================

number = 123456

count = 0

while number > 0:

    count += 1

    number //= 10

print(count)

# =========================================================
# Example 10
# Guess the Number
# =========================================================

secret = 7

while True:

    guess = int(input("Guess: "))

    if guess == secret:
        print("Correct")
        break

    print("Try Again")

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Infinite while loop.

count = 1

# while count <= 5:
#     print(count)

# Forgot:
#
# count += 1

# ---------------------------------------------------------

# Mistake 2
#
# Confusing break and continue.

for number in range(5):

    if number == 2:
        continue

    print(number)

# ---------------------------------------------------------

# Mistake 3
#
# range(5) ends at 4.

for number in range(5):
    print(number)

# Output:
#
# 0 1 2 3 4

# ---------------------------------------------------------

# Mistake 4
#
# Forgetting loop variable.

# for in range(5):

# SyntaxError

# ---------------------------------------------------------

# Mistake 5
#
# Modifying a list while iterating.

numbers = [
    1,
    2,
    3,
    4
]

# Avoid:
#
# for number in numbers:
#     numbers.remove(number)

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What are the two loop types in Python?
#
# Answer:
#
# while
# for
#
# ---------------------------------------------------------
#
# Q2. Difference between while and for?
#
# while
# -----
# Runs until a condition becomes False.
#
# for
# ---
# Iterates over an iterable.
#
# ---------------------------------------------------------
#
# Q3. Difference between break and continue?
#
# break
# -----
# Exits the loop immediately.
#
# continue
# --------
# Skips the current iteration.
#
# ---------------------------------------------------------
#
# Q4. What does pass do?
#
# Answer:
#
# It acts as a placeholder.
#
# ---------------------------------------------------------
#
# Q5. What is range()?
#
# Answer:
#
# Generates a sequence of numbers.
#
# ---------------------------------------------------------
#
# Q6. What is enumerate()?
#
# Answer:
#
# Returns both index and value.
#
# ---------------------------------------------------------
#
# Q7. What is zip()?
#
# Answer:
#
# Iterates over multiple iterables simultaneously.
#
# ---------------------------------------------------------
#
# Q8. What is loop else?
#
# Answer:
#
# Executes only if the loop
# completes without break.
#
# ---------------------------------------------------------
#
# Q9. What is list comprehension?
#
# Answer:
#
# A concise way to create lists.
#
# ---------------------------------------------------------
#
# Q10. What causes an infinite loop?
#
# Answer:
#
# A loop whose termination condition
# never becomes False.
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Python has:
#   while
#   for
#
# ✓ range() generates sequences.
#
# ✓ break exits a loop.
#
# ✓ continue skips an iteration.
#
# ✓ pass is a placeholder.
#
# ✓ Nested loops are loops inside loops.
#
# ✓ else executes only when
#   no break occurs.
#
# ✓ enumerate() returns index and value.
#
# ✓ zip() iterates over multiple iterables.
#
# ✓ List, Set and Dictionary
#   comprehensions provide concise syntax.
#
# ✓ Always update variables
#   inside while loops.
#
# =========================================================
# END OF 12_loops.py
# =========================================================
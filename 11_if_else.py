# =========================================================
# FILE: 11_if_else.py
# PART 1
# =========================================================
#
# PYTHON CONDITIONAL STATEMENTS (if, elif, else)
#
# INDEX
#
# 1. What is Decision Making?
# 2. Why Conditional Statements?
# 3. if Statement
# 4. if-else Statement
# 5. if-elif-else Statement
# 6. Nested if
# 7. Indentation
#
# =========================================================
# 1. WHAT IS DECISION MAKING?
# =========================================================
#
# Decision making allows a program to execute
# different blocks of code depending on whether
# a condition is True or False.
#
# Python uses:
#
# • if
# • elif
# • else
#

age = 20

if age >= 18:
    print("Eligible to Vote")

# =========================================================
# 2. WHY CONDITIONAL STATEMENTS?
# =========================================================
#
# We use conditions to:
#
# • Validate users
# • Check passwords
# • Decide program flow
# • Handle different situations
# • Perform business logic
#

temperature = 35

if temperature > 30:
    print("It's Hot")

# =========================================================
# BOOLEAN EXPRESSIONS
# =========================================================

print(10 > 5)

print(5 > 10)

print(10 == 10)

print(10 != 20)

# =========================================================
# 3. if STATEMENT
# =========================================================
#
# Syntax:
#
# if condition:
#     statement
#

age = 22

if age >= 18:
    print("Adult")

print("Program Finished")

# =========================================================
# MULTIPLE STATEMENTS
# =========================================================

salary = 50000

if salary >= 30000:
    print("Eligible")

    print("Apply for Loan")

    print("Processing...")

# =========================================================
# if WITHOUT EXECUTION
# =========================================================

age = 15

if age >= 18:
    print("Adult")

print("Done")

# =========================================================
# RELATIONAL OPERATORS
# =========================================================

number = 50

if number > 10:
    print("Greater than 10")

if number >= 50:
    print("Greater than or Equal to 50")

if number != 100:
    print("Not 100")

# =========================================================
# 4. if-else STATEMENT
# =========================================================
#
# Syntax:
#
# if condition:
#     statements
# else:
#     statements
#

age = 16

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

# =========================================================
# EVEN OR ODD
# =========================================================

number = 15

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# =========================================================
# POSITIVE OR NEGATIVE
# =========================================================

number = -5

if number >= 0:
    print("Positive")
else:
    print("Negative")

# =========================================================
# PASS OR FAIL
# =========================================================

marks = 80

if marks >= 35:
    print("Pass")
else:
    print("Fail")

# =========================================================
# PASSWORD CHECK
# =========================================================

password = "python123"

if password == "python123":
    print("Login Successful")
else:
    print("Invalid Password")

# =========================================================
# 5. if-elif-else
# =========================================================
#
# Used when there are multiple conditions.
#
# Syntax:
#
# if condition:
#     ...
# elif condition:
#     ...
# else:
#     ...
#

marks = 87

if marks >= 90:
    print("Grade A+")

elif marks >= 80:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

elif marks >= 35:
    print("Pass")

else:
    print("Fail")

# =========================================================
# MONTH EXAMPLE
# =========================================================

month = 2

if month == 1:
    print("January")

elif month == 2:
    print("February")

elif month == 3:
    print("March")

else:
    print("Invalid Month")

# =========================================================
# AGE GROUP
# =========================================================

age = 45

if age < 13:
    print("Child")

elif age < 20:
    print("Teenager")

elif age < 60:
    print("Adult")

else:
    print("Senior Citizen")

# =========================================================
# 6. NESTED if
# =========================================================
#
# An if statement inside another if statement.
#

age = 22
has_license = True

if age >= 18:

    if has_license:
        print("Can Drive")

# =========================================================
# NESTED if-else
# =========================================================

username = "admin"
password = "1234"

if username == "admin":

    if password == "1234":
        print("Login Successful")

    else:
        print("Wrong Password")

else:
    print("User Not Found")

# =========================================================
# NESTED LOAN EXAMPLE
# =========================================================

salary = 60000
credit_score = 780

if salary >= 50000:

    if credit_score >= 750:
        print("Loan Approved")

    else:
        print("Credit Score Too Low")

else:
    print("Salary Too Low")

# =========================================================
# 7. INDENTATION
# =========================================================
#
# Python uses indentation instead of braces.
#
# Standard indentation:
#
# 4 spaces
#

age = 20

if age >= 18:
    print("Adult")
    print("Eligible")

print("Outside if")

# =========================================================
# INCORRECT INDENTATION
# =========================================================

# if age >= 18:
# print("Adult")

# IndentationError

# =========================================================
# BOOLEAN VARIABLES
# =========================================================

is_logged_in = True

if is_logged_in:
    print("Welcome")

is_admin = False

if is_admin:
    print("Admin Panel")

# =========================================================
# TRUTHY VALUES
# =========================================================

if 100:
    print("Executed")

if "Python":
    print("Executed")

if [1, 2, 3]:
    print("Executed")

# =========================================================
# FALSY VALUES
# =========================================================

if 0:
    print("Will Not Execute")

if "":
    print("Will Not Execute")

if []:
    print("Will Not Execute")

if None:
    print("Will Not Execute")

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

temperature = 32

if temperature > 30:
    print("Hot Weather")
else:
    print("Pleasant Weather")

# ---------------------------------------------------------

balance = 5000

if balance >= 1000:
    print("Transaction Allowed")
else:
    print("Insufficient Balance")

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Missing colon.

# if age >= 18

# SyntaxError

# Correct

if age >= 18:
    print("Adult")

# ---------------------------------------------------------

# Mistake 2
#
# Incorrect indentation.

# if age >= 18:
# print("Adult")

# IndentationError

# ---------------------------------------------------------

# Mistake 3
#
# Using = instead of ==

# if age = 18:

# SyntaxError

# Correct

if age == 18:
    print("Age is 18")

# =========================================================
# FILE: 11_if_else.py
# PART 2
# =========================================================
#
# PYTHON CONDITIONAL STATEMENTS
#
# INDEX
#
# 8. Logical Operators in Conditions
# 9. Conditional (Ternary) Expressions
# 10. pass Statement
# 11. match-case Statement
# 12. Practical Examples
#
# =========================================================
# 8. LOGICAL OPERATORS IN CONDITIONS
# =========================================================
#
# Python provides three logical operators:
#
# • and
# • or
# • not
#

# =========================================================
# and
# =========================================================
#
# Returns True only if all conditions are True.
#

age = 25
salary = 60000

if age >= 18 and salary >= 50000:
    print("Eligible")

# =========================================================
# EXAMPLE
# =========================================================

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

# =========================================================
# or
# =========================================================
#
# Returns True if at least one condition is True.
#

marks = 85
sports_quota = False

if marks >= 90 or sports_quota:
    print("Admission Granted")
else:
    print("Admission Denied")

# =========================================================
# not
# =========================================================
#
# Reverses the boolean value.
#

is_blocked = False

if not is_blocked:
    print("Access Granted")

# =========================================================
# MULTIPLE CONDITIONS
# =========================================================

age = 28
salary = 75000
experience = 5

if (
    age >= 18
    and salary >= 50000
    and experience >= 2
):
    print("Eligible for Interview")

# =========================================================
# RANGE CHECK
# =========================================================

marks = 82

if 35 <= marks <= 100:
    print("Pass")

# =========================================================
# MEMBERSHIP
# =========================================================

language = "Python"

if language in [
    "Python",
    "Java",
    "Go"
]:
    print("Supported")

# =========================================================
# STRING COMPARISON
# =========================================================

city = "Mumbai"

if city == "Mumbai":
    print("Welcome")

# =========================================================
# 9. CONDITIONAL (TERNARY) EXPRESSION
# =========================================================
#
# Syntax:
#
# value_if_true if condition else value_if_false
#

age = 20

status = (
    "Adult"
    if age >= 18
    else "Minor"
)

print(status)

# =========================================================
# EVEN OR ODD
# =========================================================

number = 15

result = (
    "Even"
    if number % 2 == 0
    else "Odd"
)

print(result)

# =========================================================
# MAXIMUM OF TWO NUMBERS
# =========================================================

a = 10
b = 20

maximum = a if a > b else b

print(maximum)

# =========================================================
# MINIMUM OF TWO NUMBERS
# =========================================================

minimum = a if a < b else b

print(minimum)

# =========================================================
# NESTED TERNARY
# =========================================================

marks = 82

grade = (
    "A"
    if marks >= 90
    else "B"
    if marks >= 75
    else "C"
)

print(grade)

# =========================================================
# 10. pass STATEMENT
# =========================================================
#
# pass is a placeholder.
#
# It allows an empty code block.
#

age = 20

if age >= 18:
    pass

print("Program Continues")

# =========================================================
# FUNCTION EXAMPLE
# =========================================================

def future_feature():
    pass

# =========================================================
# CLASS EXAMPLE
# =========================================================

class Student:
    pass

# =========================================================
# LOOP EXAMPLE
# =========================================================

for _ in range(3):
    pass

# =========================================================
# 11. match-case STATEMENT
# =========================================================
#
# Available from Python 3.10+
#
# Similar to switch-case in other languages.
#

day = 3

match day:

    case 1:
        print("Monday")

    case 2:
        print("Tuesday")

    case 3:
        print("Wednesday")

    case 4:
        print("Thursday")

    case 5:
        print("Friday")

    case 6:
        print("Saturday")

    case 7:
        print("Sunday")

    case _:
        print("Invalid Day")

# =========================================================
# MONTH EXAMPLE
# =========================================================

month = 2

match month:

    case 1:
        print("January")

    case 2:
        print("February")

    case 3:
        print("March")

    case _:
        print("Invalid Month")

# =========================================================
# MULTIPLE VALUES
# =========================================================

command = "start"

match command:

    case "run" | "start":
        print("Application Started")

    case "stop" | "exit":
        print("Application Closed")

    case _:
        print("Unknown Command")

# =========================================================
# GUARDS
# =========================================================

number = 20

match number:

    case x if x > 10:
        print("Greater than 10")

    case _:
        print("10 or Less")

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1
# Login Check

username = "admin"
password = "1234"

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Login Failed")

# ---------------------------------------------------------

# Example 2
# Age Verification

age = 17

message = (
    "Eligible"
    if age >= 18
    else "Not Eligible"
)

print(message)

# ---------------------------------------------------------

# Example 3
# Grade Calculation

marks = 92

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")

# ---------------------------------------------------------

# Example 4
# ATM Withdrawal

balance = 5000
withdraw = 3000

if withdraw <= balance:
    print("Transaction Successful")
else:
    print("Insufficient Balance")

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Using = instead of ==

age = 20

# if age = 20:

# SyntaxError

# Correct

if age == 20:
    print("Correct")

# ---------------------------------------------------------

# Mistake 2
#
# Forgetting else in ternary.

result = (
    "Pass"
    if True
    else "Fail"
)

print(result)

# ---------------------------------------------------------

# Mistake 3
#
# Incorrect indentation.

if True:
    print("Correct")

# ---------------------------------------------------------

# Mistake 4
#
# Confusing and/or.

age = 20

salary = 50000

if age >= 18 and salary >= 50000:
    print("Eligible")

# =========================================================
# END OF PART 2
# =========================================================
#
# Next Part:
#
# 13. Truthy & Falsy Values
# 14. Real-World Examples
# 15. Interview Questions
# 16. Quick Revision
#
# =========================================================

# =========================================================
# FILE: 11_if_else.py
# PART 3
# =========================================================
#
# PYTHON CONDITIONAL STATEMENTS
#
# INDEX
#
# 13. Truthy & Falsy Values
# 14. Real-World Examples
# 15. Common Beginner Mistakes
# 16. Interview Questions
# 17. Quick Revision
#
# =========================================================
# 13. TRUTHY & FALSY VALUES
# =========================================================
#
# In Python, every object has a truth value.
#
# Truthy values evaluate to True.
# Falsy values evaluate to False.
#

# =========================================================
# TRUTHY VALUES
# =========================================================

if 1:
    print("1 is Truthy")

if -10:
    print("-10 is Truthy")

if 3.14:
    print("3.14 is Truthy")

if "Python":
    print("Non-empty string is Truthy")

if [1, 2, 3]:
    print("Non-empty list is Truthy")

if {"name": "Amit"}:
    print("Non-empty dictionary is Truthy")

if {1, 2, 3}:
    print("Non-empty set is Truthy")

if (10, 20):
    print("Non-empty tuple is Truthy")

# =========================================================
# FALSY VALUES
# =========================================================

print(bool(0))

print(bool(0.0))

print(bool(""))

print(bool([]))

print(bool(()))

print(bool({}))

print(bool(set()))

print(bool(None))

print(bool(False))

# =========================================================
# USING TRUTHY/FALSY
# =========================================================

name = "Diwakar"

if name:
    print("Name is available")

numbers = []

if not numbers:
    print("List is empty")

# =========================================================
# 14. REAL-WORLD EXAMPLES
# =========================================================

# =========================================================
# Example 1
# Login System
# =========================================================

username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "1234":
    print("Login Successful")
else:
    print("Invalid Credentials")

# =========================================================
# Example 2
# ATM Withdrawal
# =========================================================

balance = 10000
withdraw = 3500

if withdraw <= balance:
    balance -= withdraw
    print("Withdrawal Successful")
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")

# =========================================================
# Example 3
# Student Result
# =========================================================

marks = 76

if marks >= 90:
    grade = "A+"

elif marks >= 80:
    grade = "A"

elif marks >= 70:
    grade = "B"

elif marks >= 60:
    grade = "C"

elif marks >= 35:
    grade = "Pass"

else:
    grade = "Fail"

print("Grade:", grade)

# =========================================================
# Example 4
# Maximum of Three Numbers
# =========================================================

a = 30
b = 20
c = 40

if a >= b and a >= c:
    print("Maximum:", a)

elif b >= a and b >= c:
    print("Maximum:", b)

else:
    print("Maximum:", c)

# =========================================================
# Example 5
# Leap Year
# =========================================================

year = 2024

if (
    (year % 4 == 0 and year % 100 != 0)
    or
    (year % 400 == 0)
):
    print("Leap Year")
else:
    print("Not a Leap Year")

# =========================================================
# Example 6
# Largest Using Ternary
# =========================================================

x = 50
y = 75

largest = x if x > y else y

print("Largest:", largest)

# =========================================================
# Example 7
# Even or Odd
# =========================================================

number = 17

if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# =========================================================
# Example 8
# Voting Eligibility
# =========================================================

age = 22

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible")

# =========================================================
# Example 9
# Positive, Negative, or Zero
# =========================================================

number = -25

if number > 0:
    print("Positive")

elif number < 0:
    print("Negative")

else:
    print("Zero")

# =========================================================
# Example 10
# Password Strength
# =========================================================

password = "Python@123"

if len(password) >= 8:
    print("Strong Password")
else:
    print("Weak Password")

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Forgetting the colon (:)

# if age >= 18

# SyntaxError

# ---------------------------------------------------------

# Mistake 2
#
# Incorrect indentation.

# if True:
# print("Hello")

# IndentationError

# ---------------------------------------------------------

# Mistake 3
#
# Using = instead of ==

age = 20

# if age = 20

# SyntaxError

# Correct

if age == 20:
    print("Age Matched")

# ---------------------------------------------------------

# Mistake 4
#
# Comparing strings with wrong case.

language = "Python"

if language == "python":
    print("Matched")
else:
    print("Case Sensitive")

# ---------------------------------------------------------

# Mistake 5
#
# Confusing Truthy and Falsy values.

numbers = []

if numbers:
    print("Has Data")
else:
    print("Empty")

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is the purpose of the if statement?
#
# Answer:
# It executes a block of code only when
# the specified condition is True.
#
# ---------------------------------------------------------
#
# Q2. Difference between if and if-else?
#
# if
# ---
# Executes code only when the condition is True.
#
# if-else
# -------
# Executes one block if True,
# otherwise executes another block.
#
# ---------------------------------------------------------
#
# Q3. What is elif?
#
# Answer:
# elif allows checking multiple conditions
# after an if statement.
#
# ---------------------------------------------------------
#
# Q4. What is nested if?
#
# Answer:
# An if statement inside another if statement.
#
# ---------------------------------------------------------
#
# Q5. What is a ternary operator?
#
# Answer:
# A one-line conditional expression.
#
# Syntax:
#
# value_if_true if condition else value_if_false
#
# ---------------------------------------------------------
#
# Q6. What does pass do?
#
# Answer:
# It acts as a placeholder and performs no action.
#
# ---------------------------------------------------------
#
# Q7. What is match-case?
#
# Answer:
# A pattern matching statement introduced
# in Python 3.10.
#
# ---------------------------------------------------------
#
# Q8. Name some falsy values.
#
# Answer:
#
# False
# None
# 0
# 0.0
# ""
# []
# ()
# {}
# set()
#
# ---------------------------------------------------------
#
# Q9. Name some truthy values.
#
# Answer:
#
# Non-empty strings
# Non-empty lists
# Non-empty tuples
# Non-empty dictionaries
# Non-empty sets
# Non-zero numbers
#
# ---------------------------------------------------------
#
# Q10. Which version introduced match-case?
#
# Answer:
#
# Python 3.10
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Python uses:
#   if
#   elif
#   else
#
# ✓ Conditions evaluate to True or False.
#
# ✓ Indentation is mandatory.
#
# ✓ Logical operators:
#   and
#   or
#   not
#
# ✓ Ternary expression:
#   value_if_true if condition else value_if_false
#
# ✓ pass is a placeholder statement.
#
# ✓ match-case is available in Python 3.10+.
#
# ✓ Empty collections are falsy.
#
# ✓ Non-empty collections are truthy.
#
# ✓ Use == for comparison.
#
# ✓ Use = for assignment.
#
# ✓ Nested if statements allow multiple levels
#   of decision making.
#
# =========================================================
# END OF 11_if_else.py
# =========================================================
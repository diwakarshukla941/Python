# =========================================================
# FILE: 06_strings.py
# PART 1
# =========================================================
#
# PYTHON STRINGS
#
# INDEX
#
# 1. What is a String?
# 2. Why Strings?
# 3. Creating Strings
# 4. String Characteristics
# 5. String Indexing
# 6. Negative Indexing
# 7. String Slicing
# 8. String Immutability
#
# =========================================================
# 1. WHAT IS A STRING?
# =========================================================
#
# A string is a sequence of Unicode characters.
#
# Strings are enclosed inside:
#
# ""
# ''
# """ """
# ''' '''
#

name = "Amit"

print(name)

print(type(name))

# Output
#
# Amit
# <class 'str'>

# =========================================================
# 2. WHY STRINGS?
# =========================================================
#
# Strings are used to store text data.
#
# Examples:
#
# • Names
# • Email Addresses
# • Passwords
# • Messages
# • URLs
# • JSON Data
# • File Names
#

email = "amit@gmail.com"

url = "https://google.com"

message = "Welcome to Python"

print(email)
print(url)
print(message)

# =========================================================
# 3. CREATING STRINGS
# =========================================================

# Double Quotes

language = "Python"

# Single Quotes

city = 'Mumbai'

# Triple Double Quotes

paragraph = """
Python is easy.
Python is powerful.
"""

# Triple Single Quotes

text = '''
Backend Development
Node.js
Python
'''

print(language)

print(city)

print(paragraph)

print(text)

# =========================================================
# STRING WITH QUOTES
# =========================================================

print("It's Python")

print('He said "Hello".')

print("He said \"Hello\".")

print('It\'s awesome.')

# =========================================================
# MULTI-LINE STRINGS
# =========================================================

message = """
Hello

Welcome

To Python
"""

print(message)

# =========================================================
# EMPTY STRING
# =========================================================

empty = ""

print(empty)

print(len(empty))

# Output
#
# 0

# =========================================================
# STRING CHARACTERISTICS
# =========================================================
#
# Strings are:
#
# ✓ Ordered
# ✓ Immutable
# ✓ Iterable
# ✓ Supports Indexing
# ✓ Supports Slicing
# ✓ Allows Duplicate Characters
#

word = "Programming"

print(word)

# =========================================================
# 4. STRING INDEXING
# =========================================================
#
# Every character has an index.
#

language = "Python"

# Positive Indexing
#
# P  y  t  h  o  n
# 0  1  2  3  4  5

print(language[0])

print(language[1])

print(language[2])

print(language[3])

print(language[4])

print(language[5])

# =========================================================
# NEGATIVE INDEXING
# =========================================================
#
# P  y  t  h  o  n
#-6 -5 -4 -3 -2 -1
#

print(language[-1])

print(language[-2])

print(language[-3])

print(language[-4])

print(language[-5])

print(language[-6])

# =========================================================
# INDEX ERROR
# =========================================================

# print(language[10])

# IndexError

# =========================================================
# ACCESSING FIRST & LAST CHARACTER
# =========================================================

text = "Programming"

print(text[0])

print(text[-1])

# =========================================================
# 5. STRING SLICING
# =========================================================
#
# Syntax
#
# string[start : stop : step]
#

text = "Programming"

print(text[0:6])

# Output
#
# Progra

print(text[3:8])

# gramm

print(text[:5])

# Progr

print(text[5:])

# amming

print(text[:])

# Programming

# =========================================================
# NEGATIVE SLICING
# =========================================================

print(text[-5:])

print(text[:-3])

print(text[-8:-3])

# =========================================================
# STEP VALUE
# =========================================================

text = "ABCDEFGHIJ"

print(text[::2])

# ACEGI

print(text[1::2])

# BDFHJ

print(text[::3])

print(text[2::2])

# =========================================================
# REVERSING A STRING
# =========================================================

language = "Python"

print(language[::-1])

# Output
#
# nohtyP

# =========================================================
# COPYING A STRING
# =========================================================

text = "Backend"

copy = text[:]

print(copy)

# =========================================================
# 6. STRING IMMUTABILITY
# =========================================================
#
# Strings cannot be modified after creation.
#

name = "Python"

# name[0] = "J"

# TypeError
#
# 'str' object does not support item assignment

# =========================================================
# CORRECT WAY
# =========================================================

name = "Python"

name = "Jython"

print(name)

# =========================================================
# CREATING A NEW STRING
# =========================================================

text = "Python"

new_text = "J" + text[1:]

print(new_text)

# Output
#
# Jython

# =========================================================
# id() EXAMPLE
# =========================================================

a = "Python"

print(id(a))

a = "Java"

print(id(a))

# Since strings are immutable,
# a new object is created.

# =========================================================
# STRING LENGTH
# =========================================================

language = "Python"

print(len(language))

print(len("Backend"))

print(len(""))

# =========================================================
# MEMBERSHIP
# =========================================================

text = "Python Programming"

print("Python" in text)

print("Java" in text)

print("Java" not in text)

# =========================================================
# ITERATING OVER STRING
# =========================================================

language = "Python"

for character in language:
    print(character)

# =========================================================
# PRACTICE EXAMPLES
# =========================================================

name = "Diwakar"

print(name[0])

print(name[-1])

print(name[::-1])

print(len(name))

print(name[:4])

print(name[4:])

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1

# text[0] = "A"

# TypeError

# ----------------------------

# Mistake 2

# print(text[100])

# IndexError

# ----------------------------

# Mistake 3

# Forgetting that slicing excludes
# the ending index.

print("Python"[0:2])

# Output
#
# Py


# =========================================================
# FILE: 06_strings.py
# PART 2
# =========================================================
#
# INDEX
#
# 7. String Operators
# 8. Common String Methods
# 9. Searching Methods
# 10. Case Conversion Methods
# 11. Whitespace Methods
# 12. Alignment Methods
#
# =========================================================
# 7. STRING OPERATORS
# =========================================================
#
# Python supports several operators on strings.
#
# • +
# • *
# • in
# • not in
# • ==
# • !=
# • >
# • <
#

# =========================================================
# CONCATENATION (+)
# =========================================================

first_name = "Amit"
last_name = "Sharma"

full_name = first_name + " " + last_name

print(full_name)

# =========================================================
# CONCATENATING MULTIPLE STRINGS
# =========================================================

message = "Welcome" + " " + "to" + " " + "Python"

print(message)

# =========================================================
# STRING REPETITION (*)
# =========================================================

print("Python " * 3)

print("=" * 40)

# =========================================================
# MEMBERSHIP
# =========================================================

text = "Python Programming"

print("Python" in text)

print("Java" in text)

print("Java" not in text)

# =========================================================
# STRING COMPARISON
# =========================================================

print("apple" == "apple")

print("apple" != "banana")

print("apple" < "banana")

print("zebra" > "apple")

print("Python" == "python")

# =========================================================
# LEXICOGRAPHICAL COMPARISON
# =========================================================
#
# Python compares strings based on
# Unicode (ASCII) values.
#

print("A" < "B")

print("a" > "A")

print("10" < "2")

# =========================================================
# ASCII / UNICODE
# =========================================================

print(ord("A"))

print(ord("a"))

print(ord("0"))

print(chr(65))

print(chr(97))

# =========================================================
# 8. COMMON STRING METHODS
# =========================================================

text = "python programming"

# =========================================================
# upper()
# =========================================================

print(text.upper())

# =========================================================
# lower()
# =========================================================

print(text.lower())

# =========================================================
# capitalize()
# =========================================================

print(text.capitalize())

# =========================================================
# title()
# =========================================================

print(text.title())

# =========================================================
# swapcase()
# =========================================================

print(text.swapcase())

# =========================================================
# 9. SEARCHING METHODS
# =========================================================

sentence = "Python Programming"

# =========================================================
# find()
# =========================================================
#
# Returns index.
#
# Returns -1 if not found.
#

print(sentence.find("Python"))

print(sentence.find("Programming"))

print(sentence.find("Java"))

# =========================================================
# rfind()
# =========================================================

text = "apple apple mango"

print(text.rfind("apple"))

# =========================================================
# index()
# =========================================================
#
# Raises ValueError if not found.
#

print(sentence.index("Python"))

# print(sentence.index("Java"))

# =========================================================
# count()
# =========================================================

text = "banana"

print(text.count("a"))

print(text.count("na"))

# =========================================================
# startswith()
# =========================================================

print(sentence.startswith("Python"))

print(sentence.startswith("Java"))

# =========================================================
# endswith()
# =========================================================

print(sentence.endswith("Programming"))

print(sentence.endswith("Python"))

# =========================================================
# 10. WHITESPACE METHODS
# =========================================================

text = "    Python Programming    "

# =========================================================
# strip()
# =========================================================

print(text.strip())

# =========================================================
# lstrip()
# =========================================================

print(text.lstrip())

# =========================================================
# rstrip()
# =========================================================

print(text.rstrip())

# =========================================================
# remove() DOES NOT EXIST
# =========================================================

# Strings do not have remove().

# =========================================================
# 11. REPLACE()
# =========================================================

sentence = "I like Java"

print(sentence.replace("Java", "Python"))

# =========================================================
# REPLACING MULTIPLE OCCURRENCES
# =========================================================

text = "apple apple apple"

print(text.replace("apple", "orange"))

# =========================================================
# SPLIT()
# =========================================================

text = "Python Java C++"

words = text.split()

print(words)

# =========================================================
# SPLIT WITH SEPARATOR
# =========================================================

date = "30-06-2026"

print(date.split("-"))

# =========================================================
# JOIN()
# =========================================================

languages = [
    "Python",
    "Java",
    "Go"
]

print(" ".join(languages))

print(",".join(languages))

print(" -> ".join(languages))

# =========================================================
# PARTITION()
# =========================================================

email = "amit@gmail.com"

print(email.partition("@"))

# Output
#
# ('amit', '@', 'gmail.com')

# =========================================================
# RSPLIT()
# =========================================================

text = "one two three four"

print(text.rsplit(maxsplit=2))

# =========================================================
# 12. ALIGNMENT METHODS
# =========================================================

word = "Python"

# =========================================================
# center()
# =========================================================

print(word.center(20))

print(word.center(20, "-"))

# =========================================================
# ljust()
# =========================================================

print(word.ljust(15))

print(word.ljust(15, "."))

# =========================================================
# rjust()
# =========================================================

print(word.rjust(15))

print(word.rjust(15, "."))

# =========================================================
# zfill()
# =========================================================

number = "25"

print(number.zfill(5))

# Output
#
# 00025

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

name = "  diwakar shukla  "

print(name.strip())

print(name.title())

print(name.upper())

print(name.lower())

print(name.replace("diwakar", "amit"))

email = "admin@gmail.com"

print(email.endswith(".com"))

print(email.startswith("admin"))

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Strings are immutable.

text = "Python"

text.replace("P", "J")

print(text)

# Output
#
# Python

# Correct

text = text.replace("P", "J")

print(text)

# ---------------------------------------------------------

# Mistake 2
#
# find() vs index()

print("Python".find("Java"))

# Output
#
# -1

# index() would raise ValueError.

# ---------------------------------------------------------

# Mistake 3
#
# split() returns a list.

text = "Python Java"

result = text.split()

print(result)

print(type(result))

# ---------------------------------------------------------

# Mistake 4
#
# join() works on iterables.

languages = [
    "Python",
    "Java",
    "Go"
]

print(", ".join(languages))

# =========================================================
# FILE: 06_strings.py
# PART 3
# =========================================================
#
# INDEX
#
# 13. String Validation Methods
# 14. String Formatting
# 15. Encoding & Decoding
# 16. Escape Characters
# 17. Useful Built-in Functions
# 18. Common Beginner Mistakes
# 19. Interview Questions
# 20. Quick Revision
#
# =========================================================
# 13. STRING VALIDATION METHODS
# =========================================================
#
# These methods return either:
#
# True
# False
#

# =========================================================
# isalpha()
# =========================================================
#
# Returns True if all characters
# are alphabets.
#

print("Python".isalpha())

print("Python3".isalpha())

print("123".isalpha())

# =========================================================
# isdigit()
# =========================================================
#
# Returns True if all characters
# are digits.
#

print("12345".isdigit())

print("12A45".isdigit())

# =========================================================
# isnumeric()
# =========================================================

print("123".isnumeric())

print("Python".isnumeric())

# =========================================================
# isalnum()
# =========================================================
#
# Letters + Numbers
#

print("Python3".isalnum())

print("Python 3".isalnum())

print("Python_3".isalnum())

# =========================================================
# islower()
# =========================================================

print("python".islower())

print("Python".islower())

# =========================================================
# isupper()
# =========================================================

print("PYTHON".isupper())

print("Python".isupper())

# =========================================================
# istitle()
# =========================================================

print("Python Programming".istitle())

print("python Programming".istitle())

# =========================================================
# isspace()
# =========================================================

print("   ".isspace())

print(" Python ".isspace())

# =========================================================
# isidentifier()
# =========================================================
#
# Checks whether a string is a
# valid Python identifier.
#

print("student_name".isidentifier())

print("student1".isidentifier())

print("1student".isidentifier())

print("student-name".isidentifier())

# =========================================================
# VALIDATING USER INPUT
# =========================================================

age = "25"

print(age.isdigit())

username = "Diwakar"

print(username.isalpha())

# =========================================================
# 14. STRING FORMATTING
# =========================================================

name = "Amit"

age = 20

# =========================================================
# f-Strings (Recommended)
# =========================================================

print(f"Name: {name}")

print(f"Age: {age}")

print(f"{name} is {age} years old.")

# =========================================================
# Expressions
# =========================================================

a = 10
b = 20

print(f"Sum = {a + b}")

print(f"Average = {(a + b) / 2}")

# =========================================================
# Decimal Formatting
# =========================================================

pi = 3.1415926535

print(f"{pi:.2f}")

print(f"{pi:.4f}")

# =========================================================
# Width Formatting
# =========================================================

number = 25

print(f"{number:5}")

print(f"{number:05}")

# =========================================================
# Left Alignment
# =========================================================

print(f"|{'Python':<15}|")

# =========================================================
# Right Alignment
# =========================================================

print(f"|{'Python':>15}|")

# =========================================================
# Center Alignment
# =========================================================

print(f"|{'Python':^15}|")

# =========================================================
# str.format()
# =========================================================

print("Hello {}".format(name))

print("Age = {}".format(age))

print(
    "{} is {} years old.".format(
        name,
        age
    )
)

# =========================================================
# % Formatting (Legacy)
# =========================================================

print("Name = %s" % name)

print("Age = %d" % age)

print("Pi = %.2f" % pi)

# =========================================================
# 15. ENCODING & DECODING
# =========================================================
#
# Computers store strings as bytes.
#

text = "Python"

encoded = text.encode("utf-8")

print(encoded)

# Output
#
# b'Python'

decoded = encoded.decode("utf-8")

print(decoded)

# =========================================================
# ASCII VALUES
# =========================================================

print(ord("A"))

print(ord("a"))

print(ord("0"))

print(chr(65))

print(chr(97))

print(chr(48))

# =========================================================
# 16. ESCAPE CHARACTERS
# =========================================================

print("Hello\nPython")

print("Hello\tPython")

print("C:\\Users\\Admin")

print("It's Python")

print("He said \"Hello\"")

# =========================================================
# RAW STRING
# =========================================================
#
# r"" ignores escape sequences.
#

path = r"C:\Users\Admin\Python"

print(path)

# =========================================================
# MULTILINE STRING
# =========================================================

message = """
Python
Java
Go
Rust
"""

print(message)

# =========================================================
# 17. USEFUL BUILT-IN FUNCTIONS
# =========================================================

text = "Programming"

print(len(text))

print(max(text))

print(min(text))

print(sorted(text))

print(reversed(text))

print(list(reversed(text)))

# =========================================================
# STRING TO LIST
# =========================================================

print(list("Python"))

# =========================================================
# LIST TO STRING
# =========================================================

letters = [
    "P",
    "y",
    "t",
    "h",
    "o",
    "n"
]

print("".join(letters))

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

email = "admin@gmail.com"

print(email.split("@"))

username, domain = email.split("@")

print(username)

print(domain)

# ---------------------------------------------------------

filename = "notes.txt"

print(filename.endswith(".txt"))

# ---------------------------------------------------------

sentence = "Python is easy"

print(sentence.replace("easy", "powerful"))

# ---------------------------------------------------------

password = "Python123"

print(password.isalnum())

# ---------------------------------------------------------

name = "diwakar"

print(name.capitalize())

print(name.title())

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Strings are immutable.

text = "Python"

text.upper()

print(text)

# Output
#
# Python

# Correct

text = text.upper()

print(text)

# ---------------------------------------------------------

# Mistake 2
#
# Using join() incorrectly.

letters = [
    "A",
    "B",
    "C"
]

print("".join(letters))

# ---------------------------------------------------------

# Mistake 3
#
# Assuming split() returns a string.

text = "Python Java"

result = text.split()

print(type(result))

# Output
#
# list

# ---------------------------------------------------------

# Mistake 4
#
# Forgetting strings are case-sensitive.

print("Python" == "python")

# Output
#
# False

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is a string?
#
# Answer:
# A string is an immutable sequence of
# Unicode characters.
#
# ---------------------------------------------------------
#
# Q2. Are strings mutable?
#
# Answer:
#
# No.
#
# Strings are immutable.
#
# ---------------------------------------------------------
#
# Q3. Difference between find() and index()?
#
# Answer:
#
# find()
# Returns -1 if not found.
#
# index()
# Raises ValueError if not found.
#
# ---------------------------------------------------------
#
# Q4. Difference between split() and join()?
#
# Answer:
#
# split()
# Converts a string into a list.
#
# join()
# Joins an iterable into a string.
#
# ---------------------------------------------------------
#
# Q5. Difference between upper() and capitalize()?
#
# upper()
# Converts all letters to uppercase.
#
# capitalize()
# Converts only the first letter to uppercase.
#
# ---------------------------------------------------------
#
# Q6. Which method removes spaces from both sides?
#
# Answer:
#
# strip()
#
# ---------------------------------------------------------
#
# Q7. Which method checks whether a string
# contains only digits?
#
# Answer:
#
# isdigit()
#
# ---------------------------------------------------------
#
# Q8. How do you reverse a string?
#
# Answer:
#
# text[::-1]
#
# ---------------------------------------------------------
#
# Q9. Which formatting method is recommended?
#
# Answer:
#
# f-Strings
#
# ---------------------------------------------------------
#
# Q10. What does len() return?
#
# Answer:
#
# The number of characters in a string.
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Strings are immutable.
#
# ✓ Strings support indexing and slicing.
#
# ✓ Positive and negative indexing are supported.
#
# ✓ Common operators:
#   +
#   *
#   in
#   not in
#
# ✓ Common methods:
#   upper()
#   lower()
#   capitalize()
#   title()
#   swapcase()
#
# ✓ Searching methods:
#   find()
#   index()
#   count()
#   startswith()
#   endswith()
#
# ✓ Whitespace methods:
#   strip()
#   lstrip()
#   rstrip()
#
# ✓ Validation methods:
#   isalpha()
#   isdigit()
#   isnumeric()
#   isalnum()
#   islower()
#   isupper()
#   istitle()
#   isspace()
#   isidentifier()
#
# ✓ split() converts string → list.
#
# ✓ join() converts iterable → string.
#
# ✓ Strings are encoded using encode().
#
# ✓ Bytes are converted back using decode().
#
# ✓ f-Strings are the recommended way to format strings.
#
# =========================================================
# END OF 06_strings.py
# =========================================================
# =========================================================
# FILE: 14_modules_packages.py
# PART 1
# =========================================================
#
# PYTHON MODULES & PACKAGES
#
# INDEX
#
# 1. What is a Module?
# 2. Why Modules?
# 3. Importing Modules
# 4. Different Import Styles
# 5. Built-in Modules
# 6. Creating Your Own Module
# 7. __name__ Variable
#
# =========================================================
# 1. WHAT IS A MODULE?
# =========================================================
#
# A module is simply a Python (.py) file
# containing variables, functions, classes,
# and executable code.
#
# Examples:
#
# math.py
# random.py
# os.py
# my_module.py
#
# Benefits:
#
# • Code Reusability
# • Better Organization
# • Easier Maintenance
#

# =========================================================
# IMPORTING A MODULE
# =========================================================

import math

print(math.sqrt(25))

print(math.pi)

# =========================================================
# 2. WHY MODULES?
# =========================================================
#
# Without Modules:
#
# Everything is written in one file.
#
# Problems:
#
# • Difficult to manage
# • Difficult to debug
# • Difficult to reuse
#
# With Modules:
#
# Separate files for separate functionality.
#

# math_utils.py
#
# add()
# subtract()
#
# string_utils.py
#
# capitalize()
# reverse()

# =========================================================
# 3. IMPORTING MODULES
# =========================================================

# =========================================================
# import module
# =========================================================

import math

print(math.factorial(5))

# =========================================================
# import multiple modules
# =========================================================

import math
import random

print(math.ceil(5.3))

print(random.randint(1, 10))

# =========================================================
# import using comma
# =========================================================

import math, random

print(math.floor(5.9))

print(random.choice(["Python", "Java"]))

# =========================================================
# 4. DIFFERENT IMPORT STYLES
# =========================================================

# =========================================================
# from module import name
# =========================================================

from math import sqrt

print(sqrt(64))

# =========================================================
# Import Multiple Members
# =========================================================

from math import pi, factorial

print(pi)

print(factorial(6))

# =========================================================
# Alias
# =========================================================

import math as m

print(m.sqrt(81))

# =========================================================
# Alias Function
# =========================================================

from math import factorial as fact

print(fact(5))

# =========================================================
# Import Everything
# =========================================================

from math import *

print(sin(0))

print(cos(0))

# Avoid in production code.

# =========================================================
# 5. BUILT-IN MODULES
# =========================================================

# =========================================================
# math
# =========================================================

import math

print(math.pi)

print(math.e)

print(math.sqrt(144))

print(math.pow(2, 5))

print(math.floor(5.8))

print(math.ceil(5.2))

print(math.factorial(5))

print(math.gcd(20, 30))

# =========================================================
# random
# =========================================================

import random

print(random.random())

print(random.randint(1, 100))

print(random.uniform(1, 10))

print(
    random.choice(
        [
            "Python",
            "Java",
            "Go"
        ]
    )
)

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)

# =========================================================
# datetime
# =========================================================

import datetime

today = datetime.datetime.now()

print(today)

print(today.year)

print(today.month)

print(today.day)

# =========================================================
# os
# =========================================================

import os

print(os.getcwd())

# print(os.listdir())

# =========================================================
# sys
# =========================================================

import sys

print(sys.version)

print(sys.platform)

# =========================================================
# statistics
# =========================================================

import statistics

marks = [
    90,
    85,
    95,
    80
]

print(statistics.mean(marks))

print(statistics.median(marks))

# =========================================================
# 6. CREATING YOUR OWN MODULE
# =========================================================
#
# math_utils.py
#
# ------------------------
#
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# ------------------------
#
# main.py
#
# import math_utils
#
# print(math_utils.add(10,20))
#

# Example

# math_utils.py

# def add(a,b):
#     return a+b

# main.py

# import math_utils

# print(math_utils.add(5,10))

# =========================================================
# 7. __name__ VARIABLE
# =========================================================
#
# Every Python module has a built-in
# variable called __name__.
#

print(__name__)

# If this file is executed directly,
#
# __name__ == "__main__"

# =========================================================
# __main__ CHECK
# =========================================================

def main():
    print("Main Function")

if __name__ == "__main__":
    main()

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1

import math

radius = 5

area = math.pi * radius ** 2

print(area)

# ---------------------------------------------------------

# Example 2

import random

otp = random.randint(1000, 9999)

print(otp)

# ---------------------------------------------------------

# Example 3

import statistics

numbers = [
    10,
    20,
    30,
    40
]

print(statistics.mean(numbers))

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Forgetting import.

# print(math.sqrt(25))

# NameError

# Correct

import math

print(math.sqrt(25))

# ---------------------------------------------------------

# Mistake 2
#
# Wrong alias.

import math as m

print(m.pi)

# ---------------------------------------------------------

# Mistake 3
#
# Using import * unnecessarily.

# from math import *

# Not recommended.

# =========================================================
# FILE: 14_modules_packages.py
# PART 2
# =========================================================
#
# PYTHON MODULES & PACKAGES
#
# INDEX
#
# 8. What is a Package?
# 9. Package Structure
# 10. Absolute vs Relative Imports
# 11. Python Standard Library
# 12. pip (Package Manager)
# 13. Virtual Environments
# 14. Installing Third-Party Packages
#
# =========================================================
# 8. WHAT IS A PACKAGE?
# =========================================================
#
# A package is a collection of related
# Python modules organized inside
# a directory.
#
# Packages help organize large projects.
#
# Example:
#
# project/
# │
# ├── app.py
# ├── database/
# │   ├── __init__.py
# │   ├── connection.py
# │   └── models.py
# │
# └── utils/
#     ├── __init__.py
#     ├── helpers.py
#     └── validators.py
#

# =========================================================
# WHY PACKAGES?
# =========================================================
#
# Benefits:
#
# • Better organization
# • Avoid name conflicts
# • Reusable code
# • Easier maintenance
#

# =========================================================
# __init__.py
# =========================================================
#
# Marks a directory as a package.
#
# Modern Python supports namespace packages,
# but __init__.py is still commonly used.
#

# Example
#
# utils/
#     __init__.py
#     helper.py

# =========================================================
# IMPORTING MODULES FROM PACKAGES
# =========================================================

# utils/helper.py

# def greet():
#     print("Hello")

# main.py

# from utils.helper import greet

# greet()

# =========================================================
# IMPORT ENTIRE MODULE
# =========================================================

# import utils.helper

# utils.helper.greet()

# =========================================================
# 9. PACKAGE STRUCTURE
# =========================================================

# ecommerce/
#
# ecommerce/
# │
# ├── __init__.py
# ├── products.py
# ├── users.py
# ├── orders.py
# ├── payments.py
# └── inventory.py

# =========================================================
# IMPORT EXAMPLES
# =========================================================

# from ecommerce.products import get_products

# from ecommerce.orders import create_order

# =========================================================
# SUB-PACKAGES
# =========================================================

# project/
#
# project/
# │
# ├── app.py
# ├── backend/
# │
# ├── database/
# │   ├── __init__.py
# │   └── mongo.py
# │
# └── auth/
#     ├── __init__.py
#     └── jwt.py

# =========================================================
# 10. ABSOLUTE vs RELATIVE IMPORTS
# =========================================================

# =========================================================
# ABSOLUTE IMPORT
# =========================================================

# from backend.database.mongo import connect

# Recommended.

# =========================================================
# RELATIVE IMPORT
# =========================================================

# from .mongo import connect

# from ..database.mongo import connect

# Used mainly inside packages.

# =========================================================
# IMPORT ORDER (PEP 8)
# =========================================================
#
# 1. Standard Library
# 2. Third-party Packages
# 3. Local Imports
#

import os

import requests

# from utils.helper import greet

# =========================================================
# 11. PYTHON STANDARD LIBRARY
# =========================================================
#
# Python comes with hundreds
# of built-in modules.
#

# Common Standard Library Modules:
#
# os
# sys
# math
# random
# statistics
# datetime
# pathlib
# json
# csv
# collections
# itertools
# functools
# re
# hashlib
# sqlite3
# threading
# multiprocessing
# asyncio

# =========================================================
# pathlib
# =========================================================

from pathlib import Path

current = Path.cwd()

print(current)

# =========================================================
# json
# =========================================================

import json

student = {
    "name": "Amit",
    "age": 20
}

json_data = json.dumps(student)

print(json_data)

dictionary = json.loads(json_data)

print(dictionary)

# =========================================================
# csv
# =========================================================

import csv

# with open("students.csv") as file:
#     reader = csv.reader(file)
#
#     for row in reader:
#         print(row)

# =========================================================
# collections
# =========================================================

from collections import Counter

text = [
    "Python",
    "Java",
    "Python"
]

counter = Counter(text)

print(counter)

# =========================================================
# itertools
# =========================================================

import itertools

numbers = [1, 2, 3]

for item in itertools.permutations(numbers):
    print(item)

# =========================================================
# functools
# =========================================================

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(
    lambda x, y: x + y,
    numbers
)

print(result)

# =========================================================
# 12. pip (PACKAGE MANAGER)
# =========================================================
#
# pip installs third-party packages.
#

# Check pip version

# pip --version

# Install package

# pip install requests

# Install specific version

# pip install requests==2.32.0

# Upgrade package

# pip install --upgrade requests

# Uninstall package

# pip uninstall requests

# Show package info

# pip show requests

# List installed packages

# pip list

# Freeze dependencies

# pip freeze

# Save dependencies

# pip freeze > requirements.txt

# Install from requirements

# pip install -r requirements.txt

# =========================================================
# 13. VIRTUAL ENVIRONMENTS
# =========================================================
#
# A virtual environment creates an isolated
# Python environment for a project.
#

# Create

# python -m venv .venv

# Windows

# .venv\Scripts\activate

# macOS / Linux

# source .venv/bin/activate

# Deactivate

# deactivate

# =========================================================
# WHY USE VIRTUAL ENVIRONMENTS?
# =========================================================
#
# • Different package versions
# • Project isolation
# • Cleaner development
#

# =========================================================
# 14. INSTALLING THIRD-PARTY PACKAGES
# =========================================================

# Install

# pip install requests

# Import

import requests

# Example

response = requests.get(
    "https://example.com"
)

print(response.status_code)

# =========================================================
# BeautifulSoup
# =========================================================

# pip install beautifulsoup4

# from bs4 import BeautifulSoup

# =========================================================
# NumPy
# =========================================================

# pip install numpy

# import numpy as np

# =========================================================
# Pandas
# =========================================================

# pip install pandas

# import pandas as pd

# =========================================================
# Flask
# =========================================================

# pip install flask

# =========================================================
# Django
# =========================================================

# pip install django

# =========================================================
# FastAPI
# =========================================================

# pip install fastapi

# =========================================================
# PRACTICAL EXAMPLES
# =========================================================

# Example 1

from math import sqrt

print(sqrt(100))

# ---------------------------------------------------------

# Example 2

import random

otp = random.randint(
    100000,
    999999
)

print(otp)

# ---------------------------------------------------------

# Example 3

from datetime import datetime

print(datetime.now())

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Installing packages globally
# instead of inside a virtual
# environment.

# ---------------------------------------------------------

# Mistake 2
#
# Forgetting to activate
# the virtual environment.

# ---------------------------------------------------------

# Mistake 3
#
# Confusing pip with import.

# pip install requests

# import requests

# Both are different steps.

# ---------------------------------------------------------

# Mistake 4
#
# Forgetting requirements.txt.

# pip freeze > requirements.txt

# =========================================================
# FILE: 14_modules_packages.py
# PART 3
# =========================================================
#
# PYTHON MODULES & PACKAGES
#
# INDEX
#
# 15. __main__ Module
# 16. Python Import System
# 17. Module Search Path
# 18. Best Practices
# 19. Real-World Backend Examples
# 20. Common Beginner Mistakes
# 21. Interview Questions
# 22. Quick Revision
#
# =========================================================
# 15. __main__ MODULE
# =========================================================
#
# Every Python file has a built-in variable
# called __name__.
#
# If a file is executed directly:
#
# __name__ == "__main__"
#
# If it is imported:
#
# __name__ == module_name
#

# =========================================================
# EXAMPLE
# =========================================================

print(__name__)

# Running directly:
#
# __main__

# Imported:
#
# module_name

# =========================================================
# __main__ CHECK
# =========================================================

def main():
    print("Application Started")

if __name__ == "__main__":
    main()

# =========================================================
# WHY USE __main__?
# =========================================================
#
# Prevents test code from executing
# when the module is imported.
#

# calculator.py
#
# def add(a, b):
#     return a + b
#
# if __name__ == "__main__":
#     print(add(10, 20))
#
# main.py
#
# import calculator
#
# Test code does not execute.

# =========================================================
# 16. PYTHON IMPORT SYSTEM
# =========================================================
#
# When Python executes:
#
# import math
#
# It performs:
#
# 1. Checks sys.modules
# 2. Searches module
# 3. Loads module
# 4. Executes module
# 5. Caches module
#

import math

print(math.sqrt(25))

# =========================================================
# IMPORT HAPPENS ONLY ONCE
# =========================================================

import math
import math
import math

print(math.pi)

# Python loads the module only once.

# =========================================================
# MODULE CACHE
# =========================================================

import sys

print("math" in sys.modules)

# =========================================================
# MODULE SEARCH PATH
# =========================================================
#
# Python searches modules in:
#
# 1. Current Directory
# 2. Standard Library
# 3. Site Packages
# 4. PYTHONPATH
#

print(sys.path)

# =========================================================
# IMPORTING YOUR OWN MODULE
# =========================================================

# project/
#
# app.py
# helper.py
#
# helper.py
#
# def greet():
#     print("Hello")
#
# app.py
#
# import helper
#
# helper.greet()

# =========================================================
# 17. MODULE SEARCH PATH
# =========================================================

import sys

for path in sys.path:
    print(path)

# =========================================================
# ADDING A PATH
# =========================================================

# import sys
#
# sys.path.append("C:/projects")

# =========================================================
# FINDING MODULE LOCATION
# =========================================================

import math

print(math.__file__)

# Some built-in modules may not expose __file__.

# =========================================================
# MODULE INFORMATION
# =========================================================

print(math.__name__)

print(math.__doc__)

# =========================================================
# dir()
# =========================================================
#
# Lists all members of a module.
#

print(dir(math))

# =========================================================
# help()
# =========================================================
#
# Opens module documentation.
#

# help(math)

# =========================================================
# 18. BEST PRACTICES
# =========================================================
#
# ✓ Keep modules small.
#
# ✓ One responsibility per module.
#
# ✓ Avoid circular imports.
#
# ✓ Avoid import *.
#
# ✓ Follow PEP 8.
#
# ✓ Use meaningful module names.
#
# ✓ Group imports properly.
#

# Good

import os
import sys

from math import sqrt

# Bad

# from math import *

# =========================================================
# IMPORT ORDER
# =========================================================
#
# 1. Standard Library
# 2. Third-party Libraries
# 3. Local Modules
#

import os

import requests

# from app.utils import helper

# =========================================================
# 19. REAL-WORLD BACKEND EXAMPLES
# =========================================================

# =========================================================
# Example 1
# Node.js Style Structure in Python
# =========================================================

#
# backend/
#
# backend/
# │
# ├── app.py
# ├── routes.py
# ├── database.py
# ├── auth.py
# ├── models.py
# └── config.py
#

# =========================================================
# Example 2
# Flask Project
# =========================================================

#
# app/
#
# app/
# │
# ├── app.py
# ├── routes.py
# ├── models.py
# ├── config.py
# ├── templates/
# └── static/
#

# =========================================================
# Example 3
# Django Project
# =========================================================

#
# myproject/
#
# manage.py
#
# myproject/
#     settings.py
#     urls.py
#     wsgi.py
#
# app/
#     models.py
#     views.py
#     urls.py
#     admin.py
#

# =========================================================
# Example 4
# Utility Package
# =========================================================

#
# utils/
#
# utils/
# │
# ├── __init__.py
# ├── validator.py
# ├── formatter.py
# └── logger.py
#

# =========================================================
# Example 5
# Configuration
# =========================================================

#
# config.py
#
# DATABASE_URL
# SECRET_KEY
# DEBUG
#

# =========================================================
# COMMON BEGINNER MISTAKES
# =========================================================

# Mistake 1
#
# Naming your file
# math.py
#
# It shadows the real module.

# ---------------------------------------------------------

# Mistake 2
#
# Naming your file
# random.py

# Causes import conflicts.

# ---------------------------------------------------------

# Mistake 3
#
# Using import *.

# Avoid.

# ---------------------------------------------------------

# Mistake 4
#
# Circular imports.
#
# A imports B
# B imports A

# Causes ImportError or
# partially initialized modules.

# ---------------------------------------------------------

# Mistake 5
#
# Forgetting __main__.

# =========================================================
# INTERVIEW QUESTIONS
# =========================================================
#
# Q1. What is a module?
#
# Answer:
#
# A Python file containing code.
#
# ---------------------------------------------------------
#
# Q2. What is a package?
#
# Answer:
#
# A collection of related modules.
#
# ---------------------------------------------------------
#
# Q3. Difference between module and package?
#
# Module
# -------
# Single .py file.
#
# Package
# --------
# Directory containing modules.
#
# ---------------------------------------------------------
#
# Q4. What does __name__ do?
#
# Answer:
#
# Identifies how the module is executed.
#
# ---------------------------------------------------------
#
# Q5. What is __main__?
#
# Answer:
#
# The entry point when a Python file
# is executed directly.
#
# ---------------------------------------------------------
#
# Q6. Why avoid import *?
#
# Answer:
#
# It pollutes the namespace and
# reduces readability.
#
# ---------------------------------------------------------
#
# Q7. What is pip?
#
# Answer:
#
# Python's package manager.
#
# ---------------------------------------------------------
#
# Q8. Why use virtual environments?
#
# Answer:
#
# To isolate project dependencies.
#
# ---------------------------------------------------------
#
# Q9. Where does Python search for modules?
#
# Answer:
#
# Current directory
# Standard library
# site-packages
# PYTHONPATH
#
# ---------------------------------------------------------
#
# Q10. What is sys.modules?
#
# Answer:
#
# A cache of imported modules.
#
# =========================================================
# QUICK REVISION
# =========================================================
#
# ✓ Module = Single Python file.
#
# ✓ Package = Collection of modules.
#
# ✓ Import styles:
#   import module
#   from module import name
#   import module as alias
#
# ✓ __name__ identifies module execution.
#
# ✓ __main__ runs only when executed directly.
#
# ✓ Python caches imports in sys.modules.
#
# ✓ sys.path stores module search locations.
#
# ✓ pip installs third-party packages.
#
# ✓ Virtual environments isolate dependencies.
#
# ✓ Avoid import *.
#
# ✓ Avoid naming files after built-in modules.
#
# ✓ Organize projects using packages.
#
# =========================================================
# END OF 14_modules_packages.py
# =========================================================


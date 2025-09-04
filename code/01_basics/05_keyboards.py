"""
This module provides an overview of Python keywords, also known as reserved words, in the Python programming language.

Key Features:
-------------
- Explains the concept of a "keyword" in the context of Python programming, clarifying the distinction between the physical keyboard device and Python's reserved keywords.
- Describes how user input can be received via the keyboard using the built-in `input()` function.
- Lists all Python keywords for Python 3.6+ and highlights additional keywords and built-in functions specific to Python 2.x.
- Notes the case-sensitivity of Python keywords and the importance of consulting official documentation for version-specific keyword lists.

Intended Audience:
------------------
- Beginners learning about Python syntax and reserved words.
- Developers seeking a reference for Python keywords across different versions.

References:
-----------
- Python Official Documentation: https://docs.python.org/3/reference/lexical_analysis.html#keywords

## List of all keywords as per versions:

## Python 3.6 and above:
- class, def, return, if, else, elif, while, for, in, try, except, finally, with, as, lambda, import, from, global, nonlocal, assert, break, continue, pass, yield, raise, del, not, and, or, is, None, True, False

## Python 2.x:
- class, def, return, if, else, elif, while, for, in, try, except, finally, with, as, lambda, import, from, global, nonlocal, assert, break, continue, pass, yield, raise, del, not, and, or, is, None, True, False
- print, exec, unicode, basestring, long, xrange, raw_input

## Note:
- The keywords in Python are case-sensitive, meaning that `if` and `If` would be considered different identifiers.
- The list of keywords may vary slightly between different versions of Python, so it's always a good idea to refer to the official documentation for the specific version you are using.

"""

# Example of using the input() function to get user input from the keyboard
user_name = input("Enter your name: ")  # Prompts the user to enter their name
print(f"Hello, {user_name}!")  # Greets the user with their name
print(
    f"The type of user_name is '{type(user_name)}'"
)  # prints the data type of user_name which is <class 'str'>

# List of Python keywords for Python 3.6 and above
python_keywords = [
    "class",
    "def",
    "return",
    "if",
    "else",
    "elif",
    "while",
    "for",
    "in",
    "try",
    "except",
    "finally",
    "with",
    "as",
    "lambda",
    "import",
    "from",
    "global",
    "nonlocal",
    "assert",
    "break",
    "continue",
    "pass",
    "yield",
    "raise",
    "del",
    "not",
    "and",
    "or",
    "is",
    "None",
    "True",
    "False",
]

print("\nPython Keywords (Python 3.6+):")
for keyword in python_keywords:
    print(f" - {keyword}")
# Note: The keywords are case-sensitive, so 'if' and 'If' would be considered different identifiers.

# For Python 2.x, additional keywords include:
python2_keywords = [
    "print",
    "exec",
    "unicode",
    "basestring",
    "long",
    "xrange",
    "raw_input",
]
print("\nAdditional Python Keywords (Python 2.x):")
for keyword in python2_keywords:
    print(f" - {keyword}")
# Note: The list of keywords may vary slightly between different versions of Python.
# Always refer to the official documentation for the specific version you are using.

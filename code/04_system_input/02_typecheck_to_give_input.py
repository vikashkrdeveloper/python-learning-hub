"""
In python, type checking is a way to ensure that variables and function arguments are of the expected data types. This can help catch errors early in the development process and improve code readability. Python provides several ways to perform type checking, including using built-in functions like isinstance() and type(), as well as leveraging type hints introduced in Python 3.5.
"""

userInput = input("Enter your name: ")

if isinstance(userInput, str):
    print(f"Hello, {userInput}!")
else:
    print("Invalid input. Please enter a valid name.")


# Type cast the userInput to int
ageInput = input("Enter your age: ")

# It's better to use try-except block to handle potential conversion errors
print()
print(f"Using `try-except` for error handling:")
try:
    age = int(ageInput)
    print(f"You are {age} years old.")
except ValueError:
    print("Invalid input. Please enter a valid age.")

# Using `isinstance()` for type checking
print()
print(
    f"Using `isinstance()` for type checking: {isinstance(ageInput, int)}"
)  # This will print True if age is an int
if isinstance(ageInput, int):
    print(f"Your age is {ageInput}.")
else:
    print("Invalid input. Please enter a valid age.")

# Using `type()` for type checking
print()
print(f"Using `type()` for type checking: {type(ageInput)}")  # This will print <class 'int'>
if type(ageInput) is int:
    print(f"Your age is {ageInput}.")
else:
    print("Invalid input. Please enter a valid age.")

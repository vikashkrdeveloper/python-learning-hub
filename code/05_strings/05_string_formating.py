"""
Python String Formatting Examples
---------------------------------
This file demonstrates:
1. F-Strings
2. str.format() method
"""

# 1. F-Strings

print("\n--- F-Strings ---")

name = input("Enter your name: ")

# Simple usage
print(f"Hey {name}, you're great!")

# Math inside f-string
age = 21
print(f"{name}, next year you will be {age + 1} years old.")

# Formatting numbers
pi = 3.14159
print(f"Pi rounded to 2 decimals: {pi:.2f}")

# Inline expressions
print(f"Uppercase name: {name.upper()}")
print(f"Characters in your name: {len(name)}")

# Alignment and padding with f-strings
print(f"|{name:<10}|  (Left aligned)")
print(f"|{name:^10}|  (Centered)")
print(f"|{name:>10}|  (Right aligned)")

# 2. str.format() Method

print("\n--- str.format() Method ---")

# Simple usage
greeting = "Hello, {}. Welcome to {}.".format(name, "Python")
print(greeting)

# Positional arguments
positional = "My name is {0} and I love {1}. {0} says hi!".format(name, "coding")
print(positional)

# Named arguments
named = "This is {lang}, created by {creator}.".format(
    lang="Python", creator="Guido van Rossum"
)
print(named)

# Formatting numbers
pi_format = "Pi rounded to 3 decimals: {:.3f}".format(pi)
print(pi_format)

# Alignment and padding
align_left = "|{:<10}|  (Left aligned)".format(name)
align_center = "|{:^10}|  (Centered)".format(name)
align_right = "|{:>10}|  (Right aligned)".format(name)

print(align_left)
print(align_center)
print(align_right)

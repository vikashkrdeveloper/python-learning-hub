"""
# Identity Operators in Python
Identity operators are used to compare the memory locations of two objects. The two identity operators are:
- `is`    : Returns True if two variables point to the same object
- `is not`: Returns True if two variables do not point to the same object
"""

# Example usage of identity operators
a = [1, 2, 3]  # Ignore this line for this time only
b = a
c = a[:]

print()
print("a is b:", a is b)  # True
print("a is c:", a is c)  # False
print("a is not b:", a is not b)  # False
print("a is not c:", a is not c)  # True
print()

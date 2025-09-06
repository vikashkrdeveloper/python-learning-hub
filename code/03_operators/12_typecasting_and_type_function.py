"""
# Type Casting and Type Functions
Type casting is the process of converting a variable from one data type to another. Python provides several built-in functions for type casting:
- `int()`    : Converts a value to an integer
- `float()`  : Converts a value to a floating-point number
- `str()`    : Converts a value to a string
- `list()`   : Converts a value to a list
- `tuple()`  : Converts a value to a tuple
- `set()`    : Converts a value to a set
- `dict()`   : Converts a value to a dictionary (if possible)
- `bool()`   : Converts a value to a boolean (True or False)
Additionally, Python provides the `type()` function to check the data type of a variable.
"""

# Example usage of type casting and type function
a = "123"
b = 45.67
print()
print("Original a (string):", a, "Type:", type(a))  # Type: <class 'str'>
a_int = int(a)
print("After int(a):", a_int, "Type:", type(a_int))  # Type: <class 'int'>
b_int = int(b)
print("After int(b):", b_int, "Type:", type(b_int))  # Type: <class 'int'>

"""
Tuples are similar to lists in Python, but they are immutable (cannot be changed).
Tuples are defined using parentheses () instead of square brackets [].
Tuples can contain elements of different data types.
"""

# Creating a tuple
my_tuple = (1, 2, 3, "a", "b", "c")
print("Tuple:", my_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

# Tuple methods
print("Count of 'a':", my_tuple.count("a"))  # Output: 1
print("Index of 'b':", my_tuple.index("b"))  # Output: 4
# Note: Tuples have only two built-in methods: count() and index()

# Tuples are immutable
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)  # Output: Error: 'tuple' object does not support item assignment

# However, you can concatenate tuples
new_tuple = my_tuple + (4, 5, 6)
print("Concatenated tuple:", new_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c', 4, 5, 6)
# You can also repeat tuples
repeated_tuple = my_tuple * 2
print(
    "Repeated tuple:", repeated_tuple
)  # Output: (1, 2, 3, 'a', 'b', 'c', 1, 2, 3, 'a', 'b', 'c')
# You can convert a list to a tuple
list_to_tuple = tuple([1, 2, 3])
print("List to tuple:", list_to_tuple)  # Output: (1, 2, 3)
# You can convert a string to a tuple
string_to_tuple = tuple("hello")
print("String to tuple:", string_to_tuple)  # Output: ('h', 'e', 'l', 'l', 'o')
# You can unpack tuples
a, b, c, d, e, f = my_tuple
print("Unpacked values:", a, b, c, d, e, f)  # Output: 1 2 3 a b c

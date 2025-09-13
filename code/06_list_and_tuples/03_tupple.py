"""
# Tuples
Tuples are similar to lists, but they are immutable (cannot be changed). They are defined using parentheses ().

"""

# Creating a tuple
my_tuple = (1, 2, 3, "a", "b", "c")
print("Tuple:", my_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c')

# Accessing elements
print("First element:", my_tuple[0])  # Output: 1
print("Last element:", my_tuple[-1])  # Output: 'c'

# Slicing
print("Slice from index 1 to 4:", my_tuple[1:4])  # Output: (2, 3, 'a')

# Tuples are immutable
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError as e:
    print("Error:", e)  # Output: Error: 'tuple' object does not support item assignment
# However, you can concatenate tuples
new_tuple = my_tuple + (4, 5, 6)
print("Concatenated tuple:", new_tuple)  # Output: (1, 2, 3, 'a', 'b', 'c', 4, 5, 6)

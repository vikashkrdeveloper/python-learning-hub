"""
# List in Python
A list is a collection which is ordered and changeable. In Python, lists are written with square brackets.


# Propertices of Lists
# 1. Ordered: The items in a list have a defined order, and that order will not change unless you explicitly change it.
# 2. Changeable: You can change, add, and remove items in a list after it has been created.
# 3. Allows Duplicate Values: Since lists are indexed, they can have items with the same value.
# 4. Heterogeneous: A list can contain items of different data types, including other lists.
# 5. Dynamic: Lists can grow and shrink in size as needed.
"""


# Creating a List
my_list = [1, 2, 3, "Hello", 5.5, True]
print("Initial List:", my_list)
# Output: Initial List: [1, 2, 3, 'Hello', 5.5, True]

# Accessing List Items
print("First Item:", my_list[0])  # Output: First Item: 1
print("Last Item:", my_list[-1])   # Output: Last Item: True
print("Sliced List:", my_list[1:4])  # Output: Sliced List: [2, 3, 'Hello']

# Modifying List Items
my_list[3] = "World"
print("Modified List:", my_list)  # Output: Modified List: [1, 2, 3, 'World', 5.5, True]

"""
Set methods in Python
This script demonstrates various methods available for sets in Python.
"""

# Creating a set
my_set = {1, 2, 3, 4, 5}

# Adding an element
my_set.add(6)

# Removing an element
my_set.remove(4)

# Discarding an element
my_set.discard(3)

# Popping an element
popped_element = my_set.pop()

# Clearing the set
my_set.clear()

# Copying the set
new_set = my_set.copy()
print("Copied Set:", new_set)


# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
union_set = set_a | set_b
print("Union:", union_set)

# Intersection
intersection_set = set_a & set_b
print("Intersection:", intersection_set)

# Difference
difference_set = set_a - set_b
print("Difference:", difference_set)

# Symmetric Difference
symmetric_difference_set = set_a ^ set_b
print("Symmetric Difference:", symmetric_difference_set)

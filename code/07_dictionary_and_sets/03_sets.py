"""
# What is a set?
# A set is an unordered collection of unique elements.
# Sets are defined using curly braces {} or the set() function.
# Sets do not allow duplicate values.
"""

# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)

# Adding elements to a set
my_set.add(6)
print("Set after adding 6:", my_set)
my_set.add(3)  # Adding a duplicate element
print("Set after adding duplicate 3:", my_set)
my_set.update([7, 8, 9])
print("Set after updating with [7, 8, 9]:", my_set)
my_set.update({10, 11})
print("Set after updating with {10, 11}:", my_set)
my_set.update((12, 13))
print("Set after updating with (12, 13):", my_set)

# Removing elements from a set
my_set.remove(5)
print("Set after removing 5:", my_set)
my_set.discard(15)  # Discarding a non-existing element
print("Set after discarding non-existing 15:", my_set)
popped_element = my_set.pop()  # Removes and returns an arbitrary element
print("Popped Element:", popped_element)
print("Set after popping an element:", my_set)
my_set.clear()
print("Set after clearing:", my_set)

# Set methods
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print("Set A:", set_a)
print("Set B:", set_b)
print("Union of A and B:", set_a.union(set_b))
print("Intersection of A and B:", set_a.intersection(set_b))
print("Difference of A and B (A - B):", set_a.difference(set_b))
print("Symmetric Difference of A and B:", set_a.symmetric_difference(set_b))
print("Is A a subset of B?:", set_a.issubset(set_b))
print("Is A a superset of B?:", set_a.issuperset(set_b))
print("Are A and B disjoint?:", set_a.isdisjoint(set_b))
print("Length of Set A:", len(set_a))
print("Copy of Set A:", set_a.copy())
print("Frozenset Example:", frozenset([1, 2, 3]))
print("Set Comprehension Example:", {x**2 for x in range(5)})
print("Set after comprehension:", {x**2 for x in range(5)})

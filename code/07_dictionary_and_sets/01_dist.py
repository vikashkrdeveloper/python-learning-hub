"""
Dictionaries are mutable (can be changed) and unordered collections of key-value pairs.
Dictionaries are defined using curly braces {}.
Keys must be unique and immutable (e.g., strings, numbers, tuples).
Values can be of any data type and can be duplicated.
"""

# Creating a dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}
print("Dictionary:", my_dict)

# Accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

# Adding a new key-value pair
my_dict["email"] = "alice@example.com"
print("Updated Dictionary:", my_dict)

# Removing a key-value pair
del my_dict["age"]
print("After Deletion:", my_dict)

# Dictionary methods
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())

# Looping through a dictionary
for key, value in my_dict.items():
    print(key, ":", value)

"""
# Dictionary Methods
In this example, we will explore various dictionary methods in Python.
"""

# Creating a dictionary
my_dict = {"name": "Vikash", "age": 22, "city": "Jhanjharpur"}
print("Original Dictionary:", my_dict)

# Accessing values
print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

# Adding a new key-value pair
my_dict["email"] = "vikash@example.com"
print("Updated Dictionary:", my_dict)

# Removing a key-value pair
del my_dict["age"]
print("Dictionary after deletion:", my_dict)

# Dictionary methods
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
print("Items:", my_dict.items())
print("Get Name:", my_dict.get("name"))
print("Pop City:", my_dict.pop("city"))
print("Dictionary after pop:", my_dict)
print("Popitem:", my_dict.popitem())
print("Dictionary after popitem:", my_dict)
print("Length of Dictionary:", len(my_dict))
print("Clear Dictionary:", my_dict.clear())
print("Dictionary after clear:", my_dict)
print("Copy of Dictionary:", my_dict.copy())
print("Fromkeys Example:", dict.fromkeys(["a", "b", "c"], 0))
print("Setdefault Example:", my_dict.setdefault("name", "Unknown"))
print("After Setdefault:", my_dict)
print("Update Example:", my_dict.update({"name": "Vikash", "age": 22}))
print("Dictionary after update:", my_dict)
print("Is 'name' in Dictionary?:", "name" in my_dict)

# Looping through a dictionary
for key, value in my_dict.items():
    print(key, ":", value)

print("Looping through keys:")
for key in my_dict.keys():
    print(key)

print("Looping through values:")
for value in my_dict.values():
    print(value)

print("Looping through items:")
for item in my_dict.items():
    print(item)

print("Looping through items with unpacking:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("Dictionary comprehension:")
squared_dict = {x: x**2 for x in range(5)}
print("Squared Dictionary:", squared_dict)

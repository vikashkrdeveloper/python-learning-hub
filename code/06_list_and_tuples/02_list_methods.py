"""
# List Methods
Lists come with a variety of built-in methods that allow you to manipulate and interact with the list data. Here are some commonly used list methods:
my_list.append("New Item")
print("After Append:", my_list)  # Output: After Append: [1, 2, 3, 'World', 5.5, True, 'New Item']
my_list.remove(2)
print("After Remove:", my_list)  # Output: After Remove: [1, 3, 'World', 5.5, True, 'New Item']
my_list.insert(1, "Inserted Item")
print("After Insert:", my_list)  # Output: After Insert: [1, 'Inserted Item', 3, 'World', 5.5, True, 'New Item']
my_list.pop()
print("After Pop:", my_list)  # Output: After Pop: [1, 'Inserted Item', 3, 'World', 5.5, True]
my_list.sort(key=str)  # Sorting with key to handle mixed types
print("After Sort:", my_list)  # Output: After Sort: [1, 3, 5.5, True, 'Inserted Item', 'World']
"""

my_list = [1, 2, 3, "Hello", 5.5, True]
print("Initial List:", my_list)
my_list.append("New Item")
print("After Append:", my_list)
my_list.remove(2)
print("After Remove:", my_list)
my_list.insert(1, "Inserted Item")
print("After Insert:", my_list)
my_list.pop()
print("After Pop:", my_list)
my_list.sort(key=str)  # Sorting with key to handle mixed types
print("After Sort:", my_list)
my_list.reverse()
print("After Reverse:", my_list)

# Output:
# Initial List: [1, 2, 3, 'Hello', 5.5, True]
# After Append: [1, 2, 3, 'Hello',  5.5, True, 'New Item']
# After Remove: [1, 3, 'Hello', 5.5, True, 'New Item']
# After Insert: [1, 'Inserted Item', 3, 'Hello', 5.5, True, 'New Item']
# After Pop: [1, 'Inserted Item', 3, 'Hello', 5.5, True]
# After Sort: [1, 3, 5.5, True, 'Hello', 'Inserted Item']

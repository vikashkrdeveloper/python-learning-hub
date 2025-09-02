"""
# What is a data type?
## A data type is a classification that specifies which type of value a variable can hold. It determines the operations that can be performed on the data and how the data is stored in memory.
## In Python, data types are dynamic, meaning you don't have to explicitly declare the data type of a variable when you create it. Python automatically infers the data type based on the value assigned to the variable.

# Common data types in Python
1. Integer (int): Whole numbers, e.g., 5, -10, 0
2. Floating-point (float): Decimal numbers, e.g., 3.14, -0.001, 2.0
3. String (str): Textual data, e.g., "Hello, World!", 'Python'
4. Boolean (bool): Represents True or False values
5. List: Ordered collection of items, e.g., [1, 2, 3], ['apple', 'banana']
6. Tuple: Immutable ordered collection of items, e.g., (1, 2, 3), ('a', 'b', 'c')
7. Dictionary (dict): Collection of key-value pairs, e.g., {'name': 'Alice', 'age': 30}
8. Set: Unordered collection of unique items, e.g., {1, 2, 3}, {'apple', 'banana'}
9. NoneType: Represents the absence of a value, e.g., None
10. Complex: Complex numbers, e.g., 1 + 2j

# Example of different data types in Python
x = 10          # Integer
y = 3.14        # Floating-point
name = "Alice"  # String
is_student = True  # Boolean
fruits = ['apple', 'banana', 'cherry']  # List
point = (2, 3)  # Tuple
person = {'name': 'Bob', 'age': 25}  # Dictionary
unique_numbers = {1, 2, 3}  # Set
nothing = None  # NoneType
complex_number = 1 + 2j  # Complex
print(x, y, name, is_student, fruits, point, person, unique_numbers, nothing, complex_number)
"""

# Example of using variables with different data types
a = 10  # a is an integer variable
b = 3.14  # b is a floating-point variable
name = "Alice"  # name is a string variable
is_student = True  # is_student is a boolean variable
fruits = ["apple", "banana", "cherry"]  # fruits is a list variable
point = (2, 3)  # point is a tuple variable
person = {"name": "Bob", "age": 25}  # person is a dictionary variable
unique_numbers = {1, 2, 3}  # unique_numbers is a set variable
nothing = None  # nothing is a NoneType variable
complex_number = 1 + 2j  # complex_number is a complex variable


print(f"\nThe value of a is '{a}'")  # prints the value of a which is 10
print(f"\nThe value of b is '{b}'")  # prints the value of b which is 3.14
print(f"\nThe value of name is '{name}'")  # prints the value of name which is "Alice"
print(
    f"\nThe value of is_student is '{is_student}'"
)  # prints the value of is_student which is True
print(
    f"\nThe value of fruits is '{fruits}'"
)  # prints the value of fruits which is ['apple', 'banana', 'cherry']
print(f"\nThe value of point is '{point}'")  # prints the value of point which is (2, 3)
print(
    f"\nThe value of person is '{person}'"
)  # prints the value of person which is {'name': 'Bob', 'age': 25}
print(
    f"\nThe value of unique_numbers is '{unique_numbers}'"
)  # prints the value of unique_numbers which is {1, 2, 3}
print(
    f"\nThe value of nothing is '{nothing}'"
)  # prints the value of nothing which is None
print(
    f"\nThe value of complex_number is '{complex_number}'"
)  # prints the value of complex_number which is (1+2j)

# Checking the data types of the variables
print(
    f"The type of a is '{type(a)}'"
)  # prints the data type of a which is <class 'int'>
print(
    f"The type of b is '{type(b)}'"
)  # prints the data type of b which is <class 'float'>
print(
    f"The type of name is '{type(name)}'"
)  # prints the data type of name which is <class 'str'>
print(
    f"The type of is_student is '{type(is_student)}'"
)  # prints the data type of is_student which is <class 'bool'>
print(
    f"The type of fruits is '{type(fruits)}'"
)  # prints the data type of fruits which is <class 'list'>
print(
    f"The type of point is '{type(point)}'"
)  # prints the data type of point which is <class 'tuple'>
print(
    f"The type of person is '{type(person)}'"
)  # prints the data type of person which is <class 'dict'>
print(
    f"The type of unique_numbers is '{type(unique_numbers)}'"
)  # prints the data type of unique_numbers which is <class 'set'>
print(
    f"The type of nothing is '{type(nothing)}'"
)  # prints the data type of nothing which is <class 'NoneType'>
print(
    f"The type of complex_number is '{type(complex_number)}'"
)  # prints the data type of complex_number which is <class 'complex'>

# Performing operations based on data types
sum_ab = a + b  # Adding integer and float
print(f"The sum of a and b is '{sum_ab}'")  # prints the value of sum_ab which is 13.14

greeting = "Hello, " + name  # Concatenating strings
print(
    f"The greeting message is '{greeting}'"
)  # prints the value of greeting which is "Hello, Alice"

fruits.append("orange")  # Adding an item to the list

# prints the updated list of fruits which is ['apple', 'banana', 'cherry', 'orange']
print(f"The updated list of fruits is '{fruits}'")

person["city"] = "Bangalore"  # Adding a key-value pair to the dictionary
# prints the updated dictionary which is {'name':'Vikash', age:21, 'city': 'Bangalore'}
print(f"The updated dictionary is '{person}'")


# Checking membership in a set
print(
    f"The membership of 2 in unique_numbers is '{2 in unique_numbers}'"
)  # prints True as 2 is present in the set unique_numbers
print(
    f"The membership of 5 in unique_numbers is '{5 in unique_numbers}'"
)  # prints False as 5 is not present in the set unique_numbers

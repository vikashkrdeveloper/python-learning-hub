"""
# Operators in Python

Operators are special symbols in Python that perform operations on variables and values. They are used to manipulate data and variables.

## Types of Operators

1. **Arithmetic Operators**
    Perform mathematical operations:
    - `+`  : Addition
    - `-`  : Subtraction
    - `*`  : Multiplication
    - `/`  : Division
    - `%`  : Modulus (remainder)
    - `**` : Exponentiation (power)
    - `//` : Floor Division (quotient without remainder)

2. **Comparison (Relational) Operators**
    Compare two values:
    - `==`  : Equal to
    - `!=`  : Not equal to
    - `>`   : Greater than
    - `<`   : Less than
    - `>=`  : Greater than or equal to
    - `<=`  : Less than or equal to

3. **Logical Operators**
    Combine conditional statements:
    - `and` : Logical AND
    - `or`  : Logical OR
    - `not` : Logical NOT

4. **Bitwise Operators**
    Perform bit-level operations:
    - `&`   : Bitwise AND
    - `|`   : Bitwise OR
    - `^`   : Bitwise XOR
    - `~`   : Bitwise NOT
    - `<<`  : Left Shift
    - `>>`  : Right Shift

5. **Assignment Operators**
    Assign values to variables (and combine with operations):
    - `=`    : Assignment
    - `+=`   : Add and assign
    - `-=`   : Subtract and assign
    - `*=`   : Multiply and assign
    - `/=`   : Divide and assign
    - `%=`   : Modulus and assign
    - `**=`  : Exponentiation and assign
    - `//=`  : Floor division and assign
    - `&=`   : Bitwise AND and assign
    - `|=`   : Bitwise OR and assign
    - `^=`   : Bitwise XOR and assign
    - `<<=`  : Left shift and assign
    - `>>=`  : Right shift and assign

6. **Membership Operators**
    Test membership in a sequence (list, tuple, string, etc.):
    - `in`      : True if value is present in the sequence
    - `not in`  : True if value is not present in the sequence

7. **Identity Operators**
    Compare memory locations of two objects:
    - `is`      : True if both variables point to the same object
    - `is not`  : True if they do not point to the same object

8. **Special Operators**
    Used for specific operations:
    - `lambda`  : Create anonymous functions
    - `yield`   : Return a generator from a function
    - `await`   : Pause coroutine execution until awaited task completes
    - `del`     : Delete a variable or object
    - `:`       : Specify a range (slicing)
    - `...`     : Ellipsis, used in advanced slicing and type hinting
    - `@`       : Decorators and matrix multiplication
    - `:=`      : Walrus operator (assignment expression)
    - `,`       : Separate items in lists, tuples, and arguments
    - `.`       : Access attributes and methods of objects
    - `()`      : Group expressions and call functions
    - `[]`      : Define lists and access elements by index
    - `{}`      : Define dictionaries and sets

"""

# Example usage of some operators
a = 10
b = 3

# Arithmetic Operators Example
print("Arithmetic Operators:")
print("Addition:", a + b)  # 13
print("Subtraction:", a - b)  # 7
print("Multiplication:", a * b)  # 30
print("Division:", a / b)  # 3.3333...
print("Modulus:", a % b)  # 1
print("Exponentiation:", a**b)  # 1000
print("Floor Division:", a // b)  # 3
print()

# Comparison Operators Example
print("Comparison Operators:")
print("Equal to:", a == b)  # False
print("Not equal to:", a != b)  # True
print("Greater than:", a > b)  # True
print("Less than:", a < b)  # False
print("Greater than or equal to:", a >= b)  # True
print("Less than or equal to:", a <= b)  # False
print()

# Logical Operators Example
print("Logical Operators:")
print("Logical AND:", (a > 5) and (b < 5))  # True
print("Logical OR:", (a > 5) or (b > 5))  # True
print("Logical NOT:", not (a > 5))  # False
print()

# Bitwise Operators Example
print("Bitwise Operators:")
print("Bitwise AND:", a & b)  # 2
print("Bitwise OR:", a | b)  # 11
print("Bitwise XOR:", a ^ b)  # 9
print("Bitwise NOT:", ~a)  # -11
print("Left Shift:", a << 1)  # 20
print("Right Shift:", a >> 1)  # 5
print()

# Assignment Operators Example
print("Assignment Operators:")
c = a
print("Initial value of c:", c)  # 10
c += b
print("After c += b:", c)  # 13
c -= b
print("After c -= b:", c)  # 10
c *= b
print("After c *= b:", c)  # 30
c /= b
print("After c /= b:", c)  # 10.0
print()

# Membership Operators Example
print("Membership Operators:")
my_list = [1, 2, 3, 4, 5]
print("Is 3 in my_list?", 3 in my_list)  # True
print("Is 6 not in my_list?", 6 not in my_list)  # True
print()

# Identity Operators Example
print("Identity Operators:")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print("x is y:", x is y)  # True
print("x is z:", x is z)  # False
print("x is not z:", x is not z)  # True
print()

# Special Operators Example
print("Special Operators:")
# Lambda operator
square = lambda x: x * x
print("Square of 5 using lambda:", square(5))  # 25
print()

# Walrus operator
if (n := 10) > 5:
    print("n is greater than 5:", n)  # 10
    print("Value of n:", n)
print()


# Decorator example
def decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")

    return wrapper


@decorator
def say_hello():
    print("Hello!")


say_hello()

# Using del operator
x = 10
print("Value of x before deletion:", x)  # 10
del x
# print(x)  # This will raise an error since x is deleted
print("x has been deleted.")
print()

"""
# Assignment Operators in Python
Assignment operators are used to assign values to variables. The most common assignment operator is the equal sign (=).

Here are the common assignment operators:
- `=`    : Assigns a value to a variable
- `+=`   : Adds a value to a variable and assigns the result to that variable
- `-=`   : Subtracts a value from a variable and assigns the result to that variable
- `*=`   : Multiplies a variable by a value and assigns the result to that variable
- `/=`   : Divides a variable by a value and assigns the result to that variable
- `%=`   : Takes the modulus of a variable by a value and assigns the result to that variable
- `**=`  : Raises a variable to the power of a value and assigns the result to that variable
- `//=`  : Performs floor division on a variable by a value and assigns the result to that variable
- `&=`   : Performs bitwise AND on a variable with a value and assigns the result to that variable
- `|=`   : Performs bitwise OR on a variable with a value and assigns the result to that variable
- `^=`   : Performs bitwise XOR on a variable with a value and assigns the result to that variable
- `<<=`  : Performs left shift on a variable by a value and assigns the result to that variable
- `>>=`  : Performs right shift on a variable by a value and assigns the result to that variable
"""

# Example usage of assignment operators
a = 10
b = 3

print()
print(f"Given a = {a} and b = {b}\n")
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
c %= b
print("After c %= b:", c)  # 1.0
c **= b
print("After c **= b:", c)  # 1.0
c //= b
print("After c //= b:", c)  # 0.0
print()
# Note: Bitwise assignment operators (like &=, |=, ^=, <<=, >>=)
# are typically used with integer types. Since c is now a float,

# we will reset it to an integer value for demonstration.
c = int(c)  # Ensure c is an integer before bitwise operations
c &= b
print("After c &= b:", c)  # 2
c |= b
print("After c |= b:", c)  #  3
c ^= b
print("After c ^= b:", c)  # 0
c <<= 1
print("After c <<= 1:", c)  # 0
c >>= 1
print("After c >>= 1:", c)  # 0
print()

# Note: The output of bitwise operations may vary based on the current value of c.

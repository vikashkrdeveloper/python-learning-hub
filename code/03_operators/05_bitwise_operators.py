"""
# Bitwise Operators in Python
Bitwise operators are used to perform bit-level operations on integers. They operate on the binary representations of the numbers.

Here are the common bitwise operators:
- `&`   : Bitwise AND
- `|`   : Bitwise OR
- `^`   : Bitwise XOR
- `~`   : Bitwise NOT
- `<<`  : Left Shift
- `>>`  : Right Shift

"""

# Example usage of bitwise operators
a = 10  # In binary: 1010
b = 3   # In binary: 0011

print()
print(f"Given a = {a} (binary: {a:04b}) and b = {b} (binary: {b:04b})\n")
print("Bitwise AND (a & b):", a & b)  # 2
print("Bitwise OR (a | b):", a | b)   # 11
print("Bitwise XOR (a ^ b):", a ^ b)  # 9
print("Bitwise NOT (~a):", ~a)         # -11
print("Left Shift (a << 1):", a << 1)  # 20
print("Right Shift (a >> 1):", a >> 1) # 5
print()

# Note: The bitwise NOT operator (~) inverts all bits and is equivalent to -(x + 1) for any integer x.

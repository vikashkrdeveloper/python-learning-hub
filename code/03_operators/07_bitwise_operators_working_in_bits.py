"""
# Bitwise Operators in Python

Bitwise operators work directly on the binary representation (bits) of integers.

## Interpret as signed 32-bit (two’s complement)

Rule:
- If the MSB (most significant bit, leftmost) = 0 → number is positive, convert normally.
- If MSB = 1 → number is negative, so we must decode two’s complement.

Here, MSB = 1, so it’s negative.


1. &  (Bitwise AND)
   - Each bit is 1 only if both bits are 1.
   Example:  1010 & 0011 = 0010

2. |  (Bitwise OR)
   - Each bit is 1 if at least one of the bits is 1.
   Example:  1010 | 0011 = 1011

3. ^  (Bitwise XOR)
   - Each bit is 1 if the bits are different.
   Example:  1010 ^ 0011 = 1001

4. ~  (Bitwise NOT)
   - Flips every bit (1 → 0, 0 → 1).
   Example:  ~1010 = ...11110101 (in 32-bit two’s complement)

   Important:
   - Python integers are infinite precision, but for demonstration we assume **32-bit signed integers**.
   - Negative numbers are stored in **two’s complement** form:
     1. Start with the positive number’s binary.
     2. Flip all bits (one’s complement).
     3. Add 1 → gives two’s complement (negative number representation).
   - Example:
     - A = 10 → 00000000000000000000000000001010
     - ~A = 11111111111111111111111111110101
     - This looks like 4294967285 in unsigned decimal.
     - In signed 32-bit: Interpret MSB=1 as negative →
       Take two’s complement:
       Flip bits → 00000000000000000000000000001010
       Add 1   → 00000000000000000000000000001011 (11)
       ⇒ Result = -11

5. << (Left Shift)
   - Shifts bits to the left, filling with 0s on the right.
   Example:  1010 << 1 = 10100

6. >> (Right Shift)
   - Shifts bits to the right, filling with 0s on the left (for positive numbers).
   Example:  1010 >> 1 = 0101 
"""


# Helper function to convert integers to 32-bit binary representation
def to_32bit_array(n: int) -> list[int]:
    """Convert integer to 32-bit binary list."""
    return [(n >> i) & 1 for i in reversed(range(32))]


def from_32bit_array(bits: list[int]) -> int:
    """Convert 32-bit binary list back to integer (signed 32-bit)."""
    value = sum(bit << (31 - i) for i, bit in enumerate(bits))
    # Check MSB for negative
    if bits[0] == 1:
        value -= 1 << 32  # Adjust to signed
    return value


def print_bits(label: str, bits: list[int], value: int):
    """Pretty print bits with label and decimal value."""
    print(f"{label:<8} ({value:>11}): {''.join(map(str, bits))}")


# Example usage of bitwise operators with detailed bit representation
x, y = 10, 3  # x = 1010, y = 0011 in binary

A = to_32bit_array(x)
B = to_32bit_array(y)

print("\nBitwise Operations on 32-bit representations:\n")
print_bits("A", A, x)
print_bits("B", B, y)

# Bitwise Operations
results = {
    "A & B": [A[i] & B[i] for i in range(32)],
    "A | B": [A[i] | B[i] for i in range(32)],
    "A ^ B": [A[i] ^ B[i] for i in range(32)],
    "~A": [1 - A[i] for i in range(32)],
    "~B": [1 - B[i] for i in range(32)],
    "A << 1": to_32bit_array(x << 1),
    "A >> 1": to_32bit_array(x >> 1),
}

# Print Results
print()
for label, bits in results.items():
    print_bits(label, bits, from_32bit_array(bits))

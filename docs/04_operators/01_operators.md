# Python Operators

Operators are used to perform operations on variables and values.

In the example below, we use the `+` operator to add together two values:

```python
print(10 + 5)
```

## Types of Operators

Python divides the operators into the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

---

## Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name           | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `x + y`  |
| `-`      | Subtraction    | `x - y`  |
| `*`      | Multiplication | `x * y`  |
| `/`      | Division       | `x / y`  |
| `%`      | Modulus        | `x % y`  |
| `**`     | Exponentiation | `x ** y` |
| `//`     | Floor division | `x // y` |

---

## Assignment Operators

Assignment operators are used to assign values to variables:

| Operator | Example         | Same As           |
| -------- | --------------- | ----------------- |
| `=`      | `x = 5`         | `x = 5`           |
| `+=`     | `x += 3`        | `x = x + 3`       |
| `-=`     | `x -= 3`        | `x = x - 3`       |
| `*=`     | `x *= 3`        | `x = x * 3`       |
| `/=`     | `x /= 3`        | `x = x / 3`       |
| `%=`     | `x %= 3`        | `x = x % 3`       |
| `//=`    | `x //= 3`       | `x = x // 3`      |
| `**=`    | `x **= 3`       | `x = x ** 3`      |
| `&=`     | `x &= 3`        | `x = x & 3`       |
| `|=`     | `x |= 3`        | `x = x &#124; 3`  |
| `^=`     | `x ^= 3`        | `x = x ^ 3`       |
| `>>=`    | `x >>= 3`       | `x = x >> 3`      |
| `<<=`    | `x <<= 3`       | `x = x << 3`      |
| `:=`     | `print(x := 3)` | `x = 3; print(x)` |

---

## Comparison Operators

Comparison operators are used to compare two values:

| Operator | Name                     | Example  |
| -------- | ------------------------ | -------- |
| `==`     | Equal                    | `x == y` |
| `!=`     | Not equal                | `x != y` |
| `>`      | Greater than             | `x > y`  |
| `<`      | Less than                | `x < y`  |
| `>=`     | Greater than or equal to | `x >= y` |
| `<=`     | Less than or equal to    | `x <= y` |

---

## Logical Operators

Logical operators are used to combine conditional statements:

| Operator | Description                                   | Example                 |
| -------- | --------------------------------------------- | ----------------------- |
| `and`    | Returns True if both statements are true      | `x < 5 and x < 10`      |
| `or`     | Returns True if one of the statements is true | `x < 5 or x < 4`        |
| `not`    | Reverse the result                            | `not(x < 5 and x < 10)` |

---

## Identity Operators

Identity operators compare the objects, not if they are equal, but if they are actually the same object (same memory location):

| Operator | Description                                    | Example      |
| -------- | ---------------------------------------------- | ------------ |
| `is`     | True if both variables are the same object     | `x is y`     |
| `is not` | True if both variables are not the same object | `x is not y` |

---

## Membership Operators

Membership operators test if a sequence is present in an object:

| Operator | Description                                                | Example      |
| -------- | ---------------------------------------------------------- | ------------ |
| `in`     | True if a sequence with the specified value is present     | `x in y`     |
| `not in` | True if a sequence with the specified value is not present | `x not in y` |

---

## Bitwise Operators

Bitwise operators compare (binary) numbers:

| Operator | Name        | Description                                          | Example      |
| -------- | ----------- | ---------------------------------------------------- | ------------ |
| `&`      | AND         | Sets each bit to 1 if both bits are 1                | `x & y`      |
| `&#124;` | OR          | Sets each bit to 1 if one of two bits is 1           | `x &#124; y` |
| `^`      | XOR         | Sets each bit to 1 if only one of two bits is 1      | `x ^ y`      |
| `~`      | NOT         | Inverts all the bits                                 | `~x`         |
| `<<`     | Left shift  | Shift left by pushing zeros in from the right        | `x << 2`     |
| `>>`     | Right shift | Shift right by pushing copies of the leftmost bit in | `x >> 2`     |

---

## Operator Precedence

Operator precedence describes the order in which operations are performed.

**Example:**  
Parentheses have the highest precedence, so expressions inside parentheses are evaluated first:

```python
print((6 + 3) - (6 + 3))
```

**Example:**  
Multiplication `*` has higher precedence than addition `+`, so multiplications are evaluated before additions:

```python
print(100 + 5 * 3)
```

The precedence order is described below, starting with the highest precedence:

| Operator                              | Description                                       |
| ------------------------------------- | ------------------------------------------------- |
| `()`                                  | Parentheses                                       |
| `**`                                  | Exponentiation                                    |
| `+x -x ~x`                            | Unary plus, unary minus, and bitwise NOT          |
| `* / // %`                            | Multiplication, division, floor division, modulus |
| `+ -`                                 | Addition and subtraction                          |
| `<< >>`                               | Bitwise left and right shifts                     |
| `&`                                   | Bitwise AND                                       |
| `^`                                   | Bitwise XOR                                       |
| `&#124;`                              | Bitwise OR                                        |
| `== != > >= < <= is is not in not in` | Comparisons, identity, membership                 |
| `not`                                 | Logical NOT                                       |
| `and`                                 | AND                                               |
| `or`                                  | OR                                                |

If two operators have the same precedence, the expression is evaluated from left to right.

**Example:**  
Addition `+` and subtraction `-` have the same precedence, so the expression is evaluated from left to right:

```python
print(5 + 4 - 7 + 3)
```

---

## Exercise

What will be the result of the following code?

```python
x = 5
x += 3
print(x)
```

**Answer:**  
`8`

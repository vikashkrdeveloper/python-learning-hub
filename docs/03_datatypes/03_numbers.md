# Python Numbers

This document provides an overview of numeric types in Python, including examples and usage.

## Numeric Types in Python

There are three numeric types in Python:

- `int`
- `float`
- `complex`

Variables of numeric types are created when you assign a value to them:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex
```

To verify the type of any object in Python, use the `type()` function:

```python
print(f"The type of x is:", type(x))
print(f"The type of y is:", type(y))
print(type(z))
```

---

## int

**Int**, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

**Examples:**

```python
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))
```

---

## float

**Float**, or "floating point number", is a number, positive or negative, containing one or more decimals.

**Examples:**

```python
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))
```

Float can also be scientific numbers with an "e" to indicate the power of 10:

```python
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
```

---

## complex

**Complex** numbers are written with a "j" as the imaginary part.

**Examples:**

```python
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
```

---

## Type Conversion

You can convert from one type to another with the `int()`, `float()`, and `complex()` methods:

```python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Convert from int to float:
a = float(x)

# Convert from float to int:
b = int(y)

# Convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
```

> **Note:** You cannot convert complex numbers into another number type.

---

## Random Numbers

Python does not have a `random()` function to make a random number, but Python has a built-in module called `random` that can be used to make random numbers.

**Example:** Import the random module, and display a random number from 1 to 9:

```python
import random

print(random.randrange(1, 10))
```

For more information, see the [Random Module Reference](https://docs.python.org/3/library/random.html).

---

## Exercise

**Which is NOT a legal numeric data type in Python?**

- int
- long
- float
- complex
  > The correct answer is `long`. In Python 3, there is no separate `long` type; all integers are of type `int`, which can handle long integers automatically.

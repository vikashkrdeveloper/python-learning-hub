# Python Casting

## Specify a Variable Type

There may be times when you want to specify a type for a variable. This can be done with casting. Python is an object-oriented language, and as such, it uses classes to define data types, including its primitive types.

Casting in Python is done using constructor functions:

- `int()` - Constructs an integer number from an integer literal, a float literal (by removing all decimals), or a string literal (if the string represents a whole number).
- `float()` - Constructs a float number from an integer literal, a float literal, or a string literal (if the string represents a float or an integer).
- `str()` - Constructs a string from a wide variety of data types, including strings, integer literals, and float literals.

## Examples

### Integers

```python
x = int(1)     # x will be 1
y = int(2.8)   # y will be 2
z = int("3")   # z will be 3
```

### Floats

```python
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
```

### Strings

```python
x = str("s1 ==> ") # x will be 's1'
y = str("2 ==> ")    # y will be '2'
z = str(3.0)  # z will be '3.0'
```

## Exercise

What will be the result of the following code?

```python
print(int(35.88))
```

- 35
- 35.88
- 36

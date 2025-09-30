# Python - Output Variables

This document explains how to output variables in Python using the `print()` function.

## Output Variables

The Python `print()` function is commonly used to display variables.

### Example

```python
x = "Python is awesome"
print(x)
```

You can output multiple variables by separating them with commas in the `print()` function:

```python
x = "Python ==> "
y = "is"
z = "awesome ==> "
print(x, y, z)
```

You can also use the `+` operator to concatenate string variables:

```python
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
```

> **Note:** Notice the space character after `"Python "` and `"is "`. Without them, the result would be `"Pythonisawesome"`.

For numbers, the `+` operator performs mathematical addition:

```python
x = 5
y = 10
print(x + y)
```

If you try to combine a string and a number with the `+` operator, Python will raise an error:

```python
x = 5
y = "John"
print(x + y)  # This will cause an error
```

The best way to output multiple variables of different data types is to separate them with commas in the `print()` function:

```python
x = 5
y = "John"
print(x, y)
```

## Exercise

Consider the following code:

```python
print('Hello', 'World')
```

What will be the printed result?

- Hello, World
- Hello World
- HelloWorld
- Hello-World

  > Correct answer: Hello World

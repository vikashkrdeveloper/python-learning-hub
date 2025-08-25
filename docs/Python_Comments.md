# Python Comments

Comments can be used to explain Python code, make the code more readable, and prevent execution when testing code.

## Creating a Comment

Comments start with a `#`, and Python will ignore them:

```python
# This is a comment
print("Hello, World!")
```

Comments can also be placed at the end of a line:

```python
print("Hello, World!")  # This is a comment
```

A comment does not have to be text that explains the code; it can also be used to prevent Python from executing code:

```python
# print("Hello, World!")
print("Cheers, Mate!")
```

## Multiline Comments

Python does not have a specific syntax for multiline comments. To add a multiline comment, you can insert a `#` for each line:

```python
# This is a comment
# written in
# more than just one line
print("Hello, World!")
```

Alternatively, you can use a multiline string (triple quotes). Since Python will ignore string literals that are not assigned to a variable, you can use them as comments:

```python
"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")
```

As long as the string is not assigned to a variable, Python will read the code but ignore the string, effectively making it a multiline comment.

## Exercise

**Which character is used to define a Python comment?**

- `'`
- `//`
- `#`
- `/*`

  > Correct answer: `#`

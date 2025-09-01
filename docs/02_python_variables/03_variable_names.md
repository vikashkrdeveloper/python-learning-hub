# Python - Variable Names

## Overview

A variable can have a short name (like `x` and `y`) or a more descriptive name (such as `age`, `carname`, `total_volume`).

## Rules for Python Variables

- A variable name must start with a letter or the underscore character (`_`)
- A variable name cannot start with a number
- A variable name can only contain alpha-numeric characters and underscores (`A-z`, `0-9`, and `_`)
- Variable names are case-sensitive (`age`, `Age`, and `AGE` are three different variables)
- A variable name cannot be any of the Python keywords

## Examples

### Legal Variable Names

```python
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
```

### Illegal Variable Names

```python
2myvar = "John"
my-var = "John"
my var = "John"
```

> **Note:** Variable names are case-sensitive.

---

## Multi-Word Variable Names

Variable names with more than one word can be difficult to read. Here are several techniques to improve readability:

### Camel Case

Each word, except the first, starts with a capital letter:

```python
myVariableName = "John"
```

### Pascal Case

Each word starts with a capital letter:

```python
MyVariableName = "John"
```

### Snake Case

Each word is separated by an underscore character:

```python
my_variable_name = "John"
```

---

## Exercise

**Which is NOT a legal variable name?**

- [ ] my-var = 20
- [ ] my_var = 20
- [ ] Myvar = 20
- [ ] \_myvar = 20

> Correct answer: `my-var = 20`

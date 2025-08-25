# Python Format Strings

## String Format

As we learned in the Python Variables chapter, you cannot combine strings and numbers directly:

```python
age = 36
# This will produce an error:
txt = "My name is John, I am " + age
print(txt)
```

To combine strings and numbers, use **f-strings** or the `format()` method.

---

## F-Strings

F-strings were introduced in Python 3.6 and are now the preferred way to format strings.

To create an f-string, prefix the string with `f` and use curly braces `{}` as placeholders for variables or expressions.

**Example: Create an f-string**

```python
age = 36
txt = f"My name is John, I am {age}"
print(txt)
```

---

## Placeholders and Modifiers

A placeholder can contain variables, operations, functions, and modifiers to format the value.

**Example: Add a placeholder for the price variable**

```python
price = 59
txt = f"The price is {price} dollars"
print(txt)
```

A placeholder can include a modifier to format the value. For example, `:.2f` formats a number as a fixed-point number with 2 decimals.

**Example: Display the price with 2 decimals**

```python
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
```

You can also perform operations inside placeholders:

**Example: Perform a math operation in the placeholder**

```python
txt = f"The price is {20 * 59} dollars"
print(txt)
```

---

## Exercise

If `x = 9`, what is the correct syntax to print `'The price is 9.00 dollars'`?

- `print(f'The price is {x:.2f} dollars')`
- `print(f'The price is {x:2} dollars')`
- `print(f'The price is {x:format(2)} dollars')`

<details>
<summary>Show Answer</summary>

```python
print(f'The price is {x:.2f} dollars')
```

</details>

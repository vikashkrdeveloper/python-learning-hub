# Python - Escape Characters

## Overview

Escape characters in Python allow you to insert characters that are otherwise illegal in a string. An escape character is a backslash (`\`) followed by the character you want to insert.

## Why Use Escape Characters?

For example, to include a double quote inside a string that is surrounded by double quotes, you need to use an escape character. Otherwise, you will get a syntax error.

```python
# This will cause an error
txt = "We are the so-called "Vikings" from the north."
```

To fix this, use the escape character `\"`:

```python
# Correct usage with escape character
txt = "We are the so-called \"Vikings\" from the north."
```

## Common Escape Characters in Python

| Code   | Result          |
| ------ | --------------- |
| `\'`   | Single Quote    |
| `\\`   | Backslash       |
| `\n`   | New Line        |
| `\r`   | Carriage Return |
| `\t`   | Tab             |
| `\b`   | Backspace       |
| `\f`   | Form Feed       |
| `\ooo` | Octal value     |
| `\xhh` | Hex value       |

## Example

```python
# Using several escape characters
txt = "Line1\nLine2\tTabbed\\Backslash\'SingleQuote\"DoubleQuote"
print(txt)
```

---

> **Tip:** Use escape characters to handle special characters in your Python strings safely.

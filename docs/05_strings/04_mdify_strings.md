# Python - Modify Strings

Python provides a set of built-in methods to manipulate strings. This guide covers some common string modification techniques.

## Upper Case

The `upper()` method returns the string in upper case:

```python
a = "Hello, World! ==> "
print(a.upper())
```

## Lower Case

The `lower()` method returns the string in lower case:

```python
a = "Hello, World! ==> "
print(a.lower())
```

## Remove Whitespace

Whitespace is the space before and/or after the actual text. The `strip()` method removes any whitespace from the beginning or the end:

```python
a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"
```

## Replace String

The `replace()` method replaces a string with another string:

```python
a = "Hello, World!"
print(a.replace("H", "J"))
```

## Split String

The `split()` method splits the string into substrings if it finds instances of the separator, returning a list:

```python
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']
```

> Learn more about lists in the [Python Lists chapter](#).

## String Methods

Explore more string methods in the [String Methods Reference](#).

---

## Exercise

**What is the correct syntax to print a string in upper case letters?**

- `'Welcome'.upper()`
- `'Welcome'.toUpper()`
- `'Welcome'.toUpperCase()`

<details>
<summary>Show Answer</summary>

The correct syntax is:

```python
'Welcome'.upper()
```

</details>

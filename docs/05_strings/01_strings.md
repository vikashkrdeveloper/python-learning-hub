# Python Strings

## Introduction

Strings in Python are surrounded by either single quotation marks or double quotation marks.

`'hello'` is the same as `"hello"`.

You can display a string literal with the `print()` function:

```python
print("Hello ==> Hello")
print('Hello ==> Hello')
```

## Quotes Inside Strings

You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

```python
print("It's alright ==> Its alright")
print("He is called 'Johnny' ==> He is called 'Johnny'")
print('He is called "Johnny" ==> He is called "Johnny"')
```

## Assign String to a Variable

Assigning a string to a variable is done with the variable name followed by an equal sign and the string:

```python
a = "Hello ==> Hello"
print(a)
```

## Multiline Strings

You can assign a multiline string to a variable by using three quotes.

**Using three double quotes:**

```python
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
```

**Or three single quotes:**

```python
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
```

> **Note:** In the result, the line breaks are inserted at the same position as in the code.

## Strings are Arrays

Strings in Python are arrays of Unicode characters. Python does not have a character data type; a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

**Example:** Get the character at position 1 (remember that the first character has the position 0):

```python
a = "Hello, World! ==> "
print(a[1])
```

## Looping Through a String

Since strings are arrays, you can loop through the characters in a string with a `for` loop.

**Example:** Loop through the letters in the word `"banana"`:

```python
for x in "banana":
    print(x)
```

Learn more about For Loops in the Python For Loops chapter.

## String Length

To get the length of a string, use the `len()` function.

```python
a = "Hello, World!"
print(len(a))
```

## Check if String Contains a Substring

To check if a certain phrase or character is present in a string, use the keyword `in`.

**Example:** Check if `"free"` is present in the following text:

```python
txt = "The best things in life are free!"
print("free" in txt)
```

Use it in an `if` statement:

```python
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
```

Learn more about If statements in the Python If...Else chapter.

## Check if String Does NOT Contain a Substring

To check if a certain phrase or character is **not** present in a string, use the keyword `not in`.

**Example:** Check if `"expensive"` is **not** present in the following text:

```python
txt = "The best things in life are free!"
print("expensive" not in txt)
```

Use it in an `if` statement:

```python
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
```

## Exercise

What will be the result of the following code?

```python
x = 'Welcome'
print(x[3])
```

- W
- e
- l
- c
- Welcome
- Welcome Welcome Welcome

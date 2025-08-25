# Python Syntax

## Execute Python Syntax

As we learned in the previous page, Python syntax can be executed by writing directly in the Command Line:

```python
>>> print("Hello, World!")
Hello, World!
```

Or by creating a Python file on the server, using the `.py` file extension, and running it in the Command Line:

```shell
C:\Users\Your Name>python myfile.py
```

---

## Python Indentation

Indentation refers to the spaces at the beginning of a code line.

In other programming languages, indentation is for readability only. In Python, indentation is very important and is used to indicate a block of code.

**Example:**

```python
if 5 > 2:
    print("Five is greater than two!")
```

Python will give you an error if you skip the indentation:

**Syntax Error Example:**

```python
if 5 > 2:
print("Five is greater than two!")
```

The number of spaces is up to you as a programmer. The most common use is four spaces, but it has to be at least one.

**Examples:**

```python
if 5 > 2:
 print("Five is greater than two!")

if 5 > 2:
        print("Five is greater than two!")
```

You must use the same number of spaces in the same block of code, otherwise Python will give you an error:

**Syntax Error Example:**

```python
if 5 > 2:
 print("Five is greater than two!")
        print("Five is greater than two!")
```

---

## Python Variables

In Python, variables are created when you assign a value to them:

**Example:**

```python
x = 5
y = "Hello, World!"
```

Python has no command for declaring a variable.

You will learn more about variables in the Python Variables chapter.

---

## Comments

Python has commenting capability for the purpose of in-code documentation.

Comments start with a `#`, and Python will render the rest of the line as a comment:

**Example:**

```python
# This is a comment.
print("Hello, World!")
```

---

## Exercise

**True or False:** Indentation in Python is for readability only.

- [ ] True
- [ ] False

  > Correct answer: False

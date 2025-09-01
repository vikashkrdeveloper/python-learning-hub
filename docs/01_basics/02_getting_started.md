# Python Getting Started

## Python Install

Many PCs and Macs will have Python already installed.

To check if you have Python installed on a Windows PC, search in the Start menu for Python or run the following command in Command Prompt:

```sh
python --version
```

To check if you have Python installed on Linux or Mac, open the terminal and type:

```sh
python --version
```

If Python is not installed, you can download it for free from the [official Python website](https://www.python.org/).

---

## Python Quickstart

Python is an interpreted programming language. As a developer, you write Python (`.py`) files in a text editor and then execute them using the Python interpreter.

Let's write our first Python file, called `hello.py`:

```python
print("Hello, World!")
```

Save your file. Open your command line, navigate to the directory where you saved your file, and run:

```sh
python hello.py
```

The output should be:

```
Hello, World!
```

Congratulations, you have written and executed your first Python program!

---

## Online Python Editor

You can execute your own Python code and see the result using an online Python editor, such as the one provided by W3Schools.

Example:

```python
print("Hello, World!")
```

This editor will be used throughout the tutorial to demonstrate different aspects of Python.

---

## Python Version

To check the Python version in your environment, you can use the `sys` module:

```python
import sys
print(sys.version)
```

You will learn more about importing modules in the Python Modules chapter.

---

## The Python Command Line

To quickly test a small amount of code, you can run Python interactively from the command line.

Type the following in the Windows, Mac, or Linux command line:

```sh
python
```

Or, if the `python` command does not work, try:

```sh
py
```

From there, you can write any Python code, including the hello world example:

```python
print("Hello, World!")
```

To exit the Python command line interface, type:

```python
exit()
```

---

## Exercise

**What is the correct file extension for Python files?**

- `.pp`
- `.pt`
- `.py`
- `.pyt`

  > Correct answer: `.py`

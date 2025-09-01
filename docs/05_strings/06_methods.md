# Python - String Methods

This document provides an overview of Python's built-in string methods. All string methods return new values and do not modify the original string.

## Table of Contents

- [Python - String Methods](#python---string-methods)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [String Methods](#string-methods)

## Overview

Python has a set of built-in methods that you can use on strings. These methods help you manipulate and analyze string data efficiently.

> **Note:** All string methods return new values. They do not change the original string.

## String Methods

| Method           | Description                                                              |
| ---------------- | ------------------------------------------------------------------------ |
| `capitalize()`   | Converts the first character to upper case                               |
| `casefold()`     | Converts string into lower case                                          |
| `center()`       | Returns a centered string                                                |
| `count()`        | Returns the number of times a specified value occurs in a string         |
| `encode()`       | Returns an encoded version of the string                                 |
| `endswith()`     | Returns `True` if the string ends with the specified value               |
| `expandtabs()`   | Sets the tab size of the string                                          |
| `find()`         | Searches the string for a specified value and returns the position found |
| `format()`       | Formats specified values in a string                                     |
| `format_map()`   | Formats specified values in a string                                     |
| `index()`        | Searches the string for a specified value and returns the position found |
| `isalnum()`      | Returns `True` if all characters in the string are alphanumeric          |
| `isalpha()`      | Returns `True` if all characters in the string are in the alphabet       |
| `isascii()`      | Returns `True` if all characters in the string are ASCII characters      |
| `isdecimal()`    | Returns `True` if all characters in the string are decimals              |
| `isdigit()`      | Returns `True` if all characters in the string are digits                |
| `isidentifier()` | Returns `True` if the string is an identifier                            |
| `islower()`      | Returns `True` if all characters in the string are lower case            |
| `isnumeric()`    | Returns `True` if all characters in the string are numeric               |
| `isprintable()`  | Returns `True` if all characters in the string are printable             |
| `isspace()`      | Returns `True` if all characters in the string are whitespaces           |
| `istitle()`      | Returns `True` if the string follows the rules of a title                |
| `isupper()`      | Returns `True` if all characters in the string are upper case            |
| `join()`         | Joins the elements of an iterable to the end of the string               |
| `ljust()`        | Returns a left justified version of the string                           |
| `lower()`        | Converts a string into lower case                                        |
| `lstrip()`       | Returns a left trim version of the string                                |
| `maketrans()`    | Returns a translation table to be used in translations                   |
| `partition()`    | Returns a tuple where the string is parted into three parts              |
| `replace()`      | Returns a string where a specified value is replaced with another value  |
| `rfind()`        | Searches the string for a specified value and returns the last position  |
| `rindex()`       | Searches the string for a specified value and returns the last position  |
| `rjust()`        | Returns a right justified version of the string                          |
| `rpartition()`   | Returns a tuple where the string is parted into three parts              |
| `rsplit()`       | Splits the string at the specified separator, and returns a list         |
| `rstrip()`       | Returns a right trim version of the string                               |
| `split()`        | Splits the string at the specified separator, and returns a list         |
| `splitlines()`   | Splits the string at line breaks and returns a list                      |
| `startswith()`   | Returns `True` if the string starts with the specified value             |
| `strip()`        | Returns a trimmed version of the string                                  |
| `swapcase()`     | Swaps cases, lower case becomes upper case and vice versa                |
| `title()`        | Converts the first character of each word to upper case                  |
| `translate()`    | Returns a translated string                                              |
| `upper()`        | Converts a string into upper case                                        |
| `zfill()`        | Fills the string with a specified number of 0 values at the beginning    |

---

For more details, refer to the [official Python documentation](https://docs.python.org/3/library/stdtypes.html#string-methods).

# Python Variables - Assign Multiple Values

## Many Values to Multiple Variables

Python allows you to assign values to multiple variables in one line:

```python
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
```

> **Note:** Make sure the number of variables matches the number of values, or else you will get an error.

---

## One Value to Multiple Variables

You can assign the same value to multiple variables in one line:

```python
x = y = z = "Orange"
print(x)
print(y)
print(z)
```

---

## Unpack a Collection

If you have a collection of values in a list, tuple, etc., Python allows you to extract the values into variables. This is called unpacking.

**Example: Unpack a list**

```python
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
```

Learn more about unpacking in our **Unpack Tuples** chapter.

---

## Exercise

What is a correct syntax to add the value `'Hello World'` to 3 variables in one statement?

- `x, y, z = 'Hello World'`
- `x = y = z = 'Hello World'`
- `x|y|z = 'Hello World'`
- `x = y = z == 'Hello World'`

  > Correct answer: `x = y = z = 'Hello World'`

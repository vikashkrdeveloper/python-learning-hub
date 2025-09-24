# Python Booleans

Booleans represent one of two values: `True` or `False`.

## Boolean Values

In programming, you often need to know if an expression is `True` or `False`.  
You can evaluate any expression in Python and get one of two answers: `True` or `False`.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:

```python
print(10 > 9)
print(10 == 9)
print(10 < 9)
```

When you run a condition in an `if` statement, Python returns `True` or `False`:

```python
a = 200
b = 33

if b > a:
    print("b is greater than a ==> True")
else:
    print("b is not greater than a ==> False")
```

## Evaluate Values and Variables

The `bool()` function allows you to evaluate any value and gives you `True` or `False` in return.

**Example: Evaluate a string and a number**

```python
print(f"The types of bool(\"Hello\") is {type(bool(\"Hello\"))}")
print(f"The types of bool(15) is {type(bool(15))}")
```

**Example: Evaluate two variables**

```python
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
```

## Most Values are True

Almost any value is evaluated to `True` if it has some sort of content.

- Any string is `True`, except empty strings.
- Any number is `True`, except `0`.
- Any list, tuple, set, and dictionary are `True`, except empty ones.

**Example: The following will return True**

```python
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
```

## Some Values are False

There are not many values that evaluate to `False`, except empty values, such as `()`, `[]`, `{}`, `""`, the number `0`, and the value `None`.  
Of course, the value `False` evaluates to `False`.

**Example: The following will return False**

```python
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
```

One more value, or object in this case, evaluates to `False` if you have an object that is made from a class with a `__len__` function that returns `0` or `False`:

```python
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))
```

## Functions can Return a Boolean

You can create functions that return a Boolean value.

**Example: Print the answer of a function**

```python
def myFunction():
    return True

print(myFunction())
```

You can execute code based on the Boolean answer of a function:

**Example: Print "YES!" if the function returns True, otherwise print "NO!"**

```python
def myFunction():
    return True

if myFunction():
    print("YES!")
else:
    print("NO!")
```

Python also has many built-in functions that return a Boolean value, like the `isinstance()` function, which can be used to determine if an object is of a certain data type:

**Example: Check if an object is an integer or not**

```python
x = 200
print(isinstance(x, int))
```

## Exercise

What will be the result of the following syntax?

```python
print(5 > 3)
```

- [ ] True
- [ ] False
- [ ] 5 > 3
- [ ] Error

> Correct answer: True

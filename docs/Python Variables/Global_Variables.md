# Python - Global Variables

## Global Variables

Variables that are created outside of a function are known as **global variables**. Global variables can be used by everyone, both inside and outside of functions.

### Example

Create a variable outside of a function, and use it inside the function:

```python
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()
```

### Local vs Global Variables

If you create a variable with the same name inside a function, this variable will be **local** and can only be used inside the function. The global variable with the same name will remain unchanged.

#### Example

Create a variable inside a function, with the same name as the global variable:

```python
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)
```

### The `global` Keyword

Normally, when you create a variable inside a function, that variable is local. To create or modify a global variable inside a function, use the `global` keyword.

#### Example: Creating a Global Variable Inside a Function

```python
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
```

#### Example: Changing a Global Variable Inside a Function

```python
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)
```

## Exercise

Consider the following code:

```python
x = 'awesome'
def myfunc():
    x = 'fantastic'
myfunc()
print('Python is ' + x)
```

### What will be the printed result?

- Python is awesome
- Python is fantastic

<details>
<summary>Show Answer</summary>

**Python is awesome**

</details>

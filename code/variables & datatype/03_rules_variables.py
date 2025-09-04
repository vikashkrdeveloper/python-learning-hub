"""
## Rules for Variables in Python
1. Variable names must start with a letter or an underscore (_).
2. Variable names can only contain letters, numbers, and underscores.
3. Variable names are case-sensitive (e.g., myVar and myvar are different variables).
4. Avoid using Python keywords (e.g., def, class, if) as variable names.
print(
    f"The type of name is '{type(name)}'"
)  # prints the data type of name which is <class 'str'>
print(
    f"The type of is_student is '{type(is_student)}'"
)  # prints the data type of is_student which is <class 'bool'>
print(
    f"The type of fruits is '{type(fruits)}'"
)  # prints the data type of fruits which is <class 'list'>
"""

# Valid variable names
my_variable = 10
_variable = 20
variable1 = 30
myVar = 40
MYVAR = 50  # Different from myVar
var_123 = 60
_var_name = 70
print(f"my_variable: {my_variable}")
print(f"_variable: {_variable}")
print(f"variable1: {variable1}")
print(f"myVar: {myVar}")
print(f"MYVAR: {MYVAR}")
print(f"var_123: {var_123}")
print(f"_var_name: {_var_name}")

# Invalid variable names (uncommenting these will cause errors)
# 1variable = 10  # Starts with a number
# my-variable = 20  # Contains a hyphen
# my variable = 30  # Contains a space
# def = 40  # Uses a Python keyword
# class = 50  # Uses a Python keyword
# my@var = 60  # Contains a special character
# my$var = 70  # Contains a special character
# my%var = 80  # Contains a special character
# my#var = 90  # Contains a special character
# my!var = 100  # Contains a special character
# my^var = 110  # Contains a special character
# my&var = 120  # Contains a special character
# my*var = 130  # Contains a special character
# my(var) = 140  # Contains parentheses
# my[var] = 150  # Contains brackets
# my{var} = 160  # Contains braces
# my;var = 170  # Contains a semicolon
# my:var = 180  # Contains a colon
# my,var = 190  # Contains a comma
# my.var = 200  # Contains a period
# my?var = 210  # Contains a question mark
# my/var = 220  # Contains a forward slash
# my\var = 230  # Contains a backslash
# my<var> = 240  # Contains angle brackets
# my~var = 250  # Contains a tilde
# my`var = 260  # Contains a backtick
# my'var = 270  # Contains a single quote
# my"var = 280  # Contains a double quote
# my=var = 290  # Contains an equals sign
# my+var = 300  # Contains a plus sign
# my-var = 310  # Contains a minus sign
# ...  and so on for other special characters

# Note: The invalid variable names are commented out to prevent syntax errors.
# The above invalid variable names will raise SyntaxError if uncommented.

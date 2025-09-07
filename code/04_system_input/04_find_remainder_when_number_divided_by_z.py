number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

remainder = number1 % number2  # Finding the remainder
print(
    "The remainder when {0} is divided by {1} is {2}".format(
        number1, number2, remainder
    )
)  # Displaying the remainder

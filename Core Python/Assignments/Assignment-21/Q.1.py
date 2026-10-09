# 1. Develop a simple calculator program that performs basic arithmetic operations (+,
# -, *, /) on two numbers provided by the user. The program should ask the user for
# the numbers and the operator. However, the program should handle the following
# exceptions:
# a. Invalid Number: If the user enters a number that is not valid, catch the
# exception and display an error message.
# b. Invalid Operator: If the user enters an operator other than "+", "-", "*", or
# "/", catch the exception and display an error message.
# c. Division by Zero: If the user tries to divide by zero, catch the exception and
# display an error message.
# Write a program that performs the requested arithmetic operation and
# handles the exceptions as described above.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    if operator == "+":
        print("Result:", num1 + num2)

    elif operator == "-":
        print("Result:", num1 - num2)

    elif operator == "*":
        print("Result:", num1 * num2)

    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        print("Result:", num1 / num2)

    else:
        raise ValueError("Invalid operator!")

except ValueError as e:
    print("Error:", e)

except ZeroDivisionError as e:
    print("Error:", e)


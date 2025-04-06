# Python Program to Make a Simple Calculator

def multiplication(num1, num2):
    return num1 * num2


def addition(num1, num2):
    return num1 + num2


def subtraction(num2, num1):
    return num1 - num2


def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Division by zero")

again = True

while again:
    print("""
    Simple calculator:
    1. addition
    2. subtraction
    3. multiplication
    4. division
    5. exit
    """)
    operation = input("chose operation or exit: ")

    if operation == "5":
        print("Bye")
        again = False

    elif operation in ["1", "2", "3", "4"]:

        x=float(input("first number"))
        y=float(input("second number"))


        if operation == "1":
            print(x, "+", y, "=", addition(x,y)) # x + y
        elif operation == "2":
            print(x, "-", y, "=", subtraction(x,y)) # x - y
        elif operation == "3":
            print(x, "*", y, "=", multiplication(x,y)) # x * y
        elif operation == "4":
            print(x, "/", y, "=", divide(x,y)) # x / y

        else:
            print("Error, enter a number 1-5")

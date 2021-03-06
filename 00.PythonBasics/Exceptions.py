import math


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("You can not divide by 0.")
        return "Wrong operation."


while True:
    try:
        op1 = (int(input("Enter the first number: ")))
        op2 = (int(input("Enter the second number: ")))
        break
    except ValueError:
        print("The entered values are not correct, try again: ")

operation = input("Enter the operation to be performed (sum, subtract, multiply, divide): ")

if operation == "sum":
    print(addition(op1, op2))
elif operation == "subtract":
    print(subtraction(op1, op2))
elif operation == "multiply":
    print(multiplication(op1, op2))
elif operation == "divide":
    print(division(op1, op2))
else:
    print("Operation not covered.")

print("Operation executed. Continuation of execution of the program.")


def divide():
    try:
        op3 = (float(input("Enter the first number: ")))
        op4 = (float(input("Enter the second number: ")))
        print("The division is: " + str(op3 / op4))

    except ValueError:
        print("The entered value is not correct.")
    except ZeroDivisionError:
        print("You can not divide by 0.")

    finally:
        print("Calculation completed.")


divide()


# Using raise
def evaluate_age(age):
    if age < 0:
        raise ZeroDivisionError("Negative ages are not allowed.")

    if age < 20:
        return "You are very young"
    elif age < 40:
        return "You are young"
    elif age < 65:
        return "You are mature"
    elif age < 100:
        return "Take care of yourself"


print(evaluate_age(-15))


def calculate_square_root(num1):
    if num1 < 0:
        raise ValueError("The number cannot be negative.")
    else:
        return math.sqrt(num1)


op5 = (int(input("Enter a number: ")))
try:
    print(calculate_square_root(op5))
except ValueError as NegativeNumberError:
    print(NegativeNumberError)

print("Finished program")

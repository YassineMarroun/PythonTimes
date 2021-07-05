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


op1 = (int(input("Enter the first number: ")))
op2 = (int(input("Enter the second number: ")))
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

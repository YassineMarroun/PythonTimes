# Iterative way
def iterative_fibonacci(n):
    num1 = 0
    num2 = 1

    for i in range(n):
        result = num1 + num2
        num1 = num2
        num2 = result

    return num2


print("Iterative Fibonacci")
for k in range(20):
    print(iterative_fibonacci(k))
print("-------------------")


# Recursive way
def recursive_fibonacci(n):
    if n < 2:
        return n

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)


print("Recursive Fibonacci")
for k in range(20):
    print(recursive_fibonacci(k))
print("-------------------")

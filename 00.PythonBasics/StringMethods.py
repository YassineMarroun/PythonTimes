username = input("Enter your username: ")

print("The name is: ", username.upper())
print("The name is: ", username.lower())
print("The name is: ", username.capitalize())

age = input("Enter your age: ")

while not age.isdigit():
    print("Please enter a numerical value.")
    age = input("Enter your age: ")

if int(age) < 18:
    print("You can not pass.")
else:
    print("You can pass.")

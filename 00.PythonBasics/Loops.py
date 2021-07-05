import math

# For loop
for i in [1, 2, 3]:
    print("Hello")

for j in ["one", "two", "three", "four"]:
    print(j)

for k in ["one", "two", "three", "four"]:
    print(k, end=" ")

for m in "number_of_characters":
    print("Letter", end=" ")

counter = 0
myEmail = input("Enter your email address: ")

for i in myEmail:
    if i == "@" or i == ".":
        counter = counter + 1

if counter == 2:
    print("Email is correct")
else:
    print("Email is incorrect")

for c in range(5, 50, 3):
    print(f"Variable value {c}")

valid = False
myEmail = input("Enter your email address: ")

for i in range(len(myEmail)):
    if myEmail[i] == "@":
        valid = True
if valid:
    print("Email is correct")
else:
    print("Email is incorrect")


# While loop
i = 1
while i <= 10:
    print("Execution " + str(i))
    i = i + 1
print("Execution ended")

age = int(input("Enter your age, please: "))
while age < 5 or age > 100:
    print("You have entered an incorrect age. Try again")
    age = int(input("Enter your age, please: "))

print("Thanks for your cooperation, you can pass.")
print("Applicant's age: " + str(age))


print("Square root calculation program")
number = int(input("Please enter a number: "))
attempts = 0

while number < 0:
    print("Cannot calculate the root of a negative number")

    if attempts == 2:
        print("You have consumed too many attempts. The program has ended.")
        break

    number = int(input("Please enter a new number: "))
    if number < 0:
        attempts = attempts + 1

if attempts < 2:
    solution = math.sqrt(number)
    print("The square root of " + str(number) + " is " + str(solution))


# Using continue, pass and else
for letter in "Python":
    if letter == "h":
        continue
    print("Seeing the letter: " + letter)


name = "Another sentence"
counter = 1

for i in name:
    if i == " ":
        continue
    counter += 1

print(counter)


email = input("Enter your email address: ")

for i in email:
    if i == "@":
        at = True
        break
else:
    at = False

print(at)

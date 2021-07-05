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


for c in range(5):
    print(c)

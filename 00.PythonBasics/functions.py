def suma(num1, num2):
    result = num1 + num2

    return result


store_result = suma(5, 7)
print(store_result)

# lists
myList1 = ["Peter", "Ana", "Michael", "Thomas"]
myList2 = ["Erik", 8, 2.16]
myList3 = myList1 + myList2
print(myList3[:])

# tuples
myTuple = ("Paul", 12, 2, 1992, 12)
print(myTuple[3])

myList = list(myTuple)
print(myTuple)

myTuple = tuple(myList)
print(myList)

print("Paul" in myTuple)
print(myTuple.count(12))
print(len(myTuple))

myTuple2 = ("David", 24, 9, 1985)
name, day, month, year = myTuple2

print(myTuple2)
print(name)
print(year)

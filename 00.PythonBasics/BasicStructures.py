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

# dictionaries
myDictionary = {"Germany": "Berlin", "France": "Paris", "United Kingdom": "London", "Spain": "Madrid",
                "Italy": "Lisbon"}
print(myDictionary)

myDictionary["Italy"] = "Rome"
print(myDictionary)

del myDictionary["United Kingdom"]
print(myDictionary)

myTuple3 = ["Spain", "France", "United Kingdom", "Germany"]
myDictionary2 = {myTuple3[0]: "Madrid", myTuple3[1]: "Paris", myTuple3[2]: "London", myTuple3[3]: "Berlin"}
print(myDictionary2)

myDictionary3 = {23: "Jordan", "Name": "Michael", "Team": "Chicago",
                 "Rings": {"seasons": [1991, 1992, 1993, 1996, 1997, 1998]}}
print(myDictionary3)
print(myDictionary3["Rings"])

print(myDictionary3.keys())
print(myDictionary3.values())
print(len(myDictionary3))

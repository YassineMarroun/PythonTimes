"""Sort a list from lowest to highest"""


def bubble_sort(myList):
    for i in range(0, len(myList) - 1):
        for j in range(0, len(myList) - 1 - i):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]
    return myList


theList = ['b', 'd', 'f', 'a', 'c', 'e']
print(bubble_sort(theList))

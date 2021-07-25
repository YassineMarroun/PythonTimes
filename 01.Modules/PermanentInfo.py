import pickle


class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        print("A new person has been created with the name of", self.name)

    def __str__(self):
        return "{} {} {}".format(self.name, self.gender, self.age)


class PeopleList:
    people = []

    def __init__(self):
        list_of_people = open("externalFile", "ab+")
        list_of_people.seek(0)

        try:
            self.people = pickle.load(list_of_people)
            print("{} people were uploaded from the external file".format(len(self.people)))
        except:
            print("The file is empty")
        finally:
            list_of_people.close()
            del list_of_people

    def add_people(self, person):
        self.people.append(person)

    def show_people(self):
        for person in self.people:
            print(person)


myList = PeopleList()
"""
p = Person("Anna", "Female", 29)
myList.add_people(p)
p = Person("Tonny", "Male", 39)
myList.add_people(p)
p = Person("Rachael", "Female", 19)
myList.add_people(p)
"""

class Car:

    def __init__(self):
        self.__longChassis = 250
        self.__widthChassis = 120
        self.__wheels = 4
        self.__ongoing = False

    def start(self, starting):
        self.__ongoing = starting

        if self.__ongoing:
            check = self.__internal_check()

        if self.__ongoing and check:
            return "The car is running."

        elif self.__ongoing and check == False:
            return "Something went wrong with the checkup. The car cannot start"

        else:
            return "The car is stopped."

    def state(self):
        print("The car has", self.__wheels, "wheels. A width of", self.__widthChassis,
              "and a length of", self.__longChassis)

    def __internal_check(self):
        print("Performing internal check")

        self.gasoline = "Ok"
        self.oil = "Ok"
        self.doors = "Closed"

        if self.gasoline == "Ok" and self.oil == "Ok" and self.doors == "Closed":
            return True
        else:
            return False


myCar = Car()
print(myCar.start(True))
myCar.state()

print("-- Next we create a second object -- ")

myCar2 = Car()
print(myCar2.start(False))
myCar2.state()

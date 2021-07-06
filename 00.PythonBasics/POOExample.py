class Car:

    def __init__(self):
        self.__longChassis = 250
        self.__widthChassis = 120
        self.__wheels = 4
        self.__ongoing = False

    def start(self, starting):
        self.__ongoing = starting

        if self.__ongoing:
            return "The car is running."
        else:
            return "The car is stopped."

    def state(self):
        print("The car has", self.__wheels, "wheels. A width of", self.__widthChassis,
              "and a length of", self.__longChassis)


myCar = Car()
print(myCar.start(True))
myCar.state()

print("-- Next we create a second object -- ")

myCar2 = Car()
print(myCar2.start(False))
myCar2.wheels = 2
myCar2.state()

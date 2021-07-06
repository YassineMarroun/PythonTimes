class Car:
    longChassis = 250
    widthChassis = 120
    wheels = 4
    ongoing = False

    def start(self):
        self.ongoing = True

    def state(self):
        if self.ongoing:
            return "The car is running."
        else:
            return "The car is stopped."


myCar = Car()
print("The length of the car is:", myCar.longChassis)
print("The car has", myCar.wheels, "wheels")
myCar.start()
print(myCar.state())

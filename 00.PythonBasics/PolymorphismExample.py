class Car:

    def displacement(self):
        print("I move using four wheels.")


class Motorcycle:

    def displacement(self):
        print("I move using two wheels.")


class Truck:

    def displacement(self):
        print("I move using six wheels.")


def vehicle_displacement(vehicle):
    vehicle.displacement()


myVehicle = Truck()
vehicle_displacement(myVehicle)

myVehicle2 = Car()
vehicle_displacement(myVehicle2)

myVehicle3 = Motorcycle()
vehicle_displacement(myVehicle3)

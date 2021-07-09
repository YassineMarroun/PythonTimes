class Vehicles:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.ongoing = False
        self.accelerate = False
        self.brake = False

    def start(self):
        self.ongoing = True

    def speed_up(self):
        self.accelerate = True

    def slow_down(self):
        self.brake = True

    def state(self):
        print("Brand:", self.brand, "\nModel:", self.model, "\nOn going:", self.ongoing,
              "\nAccelerating:", self.accelerate, "\nBraking:", self.brake)


class Van(Vehicles):

    def load(self, loading):
        self.loaded = loading
        if self.loaded:
            return "The van is loaded."
        else:
            return "The van is not loaded."


class Motorcycle(Vehicles):
    doing_wheelie = ""

    def wheelie(self):
        self.doing_wheelie = "Bike doing wheelie."

    def state(self):
        print("Brand:", self.brand, "\nModel:", self.model, "\nOn going:", self.ongoing,
              "\nAccelerating:", self.accelerate, "\nBraking:", self.brake, "\n", self.doing_wheelie)


class ElectricVehicles:
    def __init__(self):
        super()
        self.autonomy = 100

    def charge_energy(self):
        self.charging = True


print("----- Motorcycle -----")
myMotorcycle = Motorcycle("Honda", "CBR")
myMotorcycle.wheelie()
myMotorcycle.state()
print("----- Van -----")
myVan = Van("Renault", "Kangoo")
myVan.start()
myVan.state()
print(myVan.load(True))


class ElectricBicycle(ElectricVehicles, Vehicles):
    pass


myBicycle = ElectricBicycle()

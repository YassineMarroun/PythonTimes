import pickle

"""
name_list = ["Peter", "Marc", "Michael", "Jhon"]

binary_file = open("name_list", "wb")
pickle.dump(name_list, binary_file)
binary_file.close()

del binary_file

file = open("name_list", "rb")

n_list = pickle.load(file)
print(n_list)
"""


class Vehicle:
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


car1 = Vehicle("Mazda", "MX5")
car2 = Vehicle("Seat", "Leon")
car3 = Vehicle("Renault", "Megane")

cars = [car1, car2, car3]
file = open("theCars", "wb")
pickle.dump(cars, file)
file.close()
del file

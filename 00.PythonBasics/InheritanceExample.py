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
        print("Brand:", self.brand, "\nModel:", self.model, "\nOn going:", self.ongoing, "\nAccelerating:", self.
        Braking")

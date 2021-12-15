class ElectricCar:
    def __init__(self, model, list):
        self.model = model
        self.list = list

    def getBatteryLevel(self):
        return((self.list[0] + self.list[1] + self.list[2] + self.list[3]) / 4)

    def charge(self, level):
        self.list[0] += level
        self.list[1] += level
        self.list[2] += level
        self.list[3] += level
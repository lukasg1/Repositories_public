from battery_cell import BatteryCell
from electric_car import ElectricCar

car = ElectricCar("Resla Toadster", [50, 50, 50, 50])
print(car.getBatteryLevel())

car.charge(10.0)

print(car.getBatteryLevel())
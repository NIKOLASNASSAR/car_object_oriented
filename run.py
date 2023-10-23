from car import Car
from electric_car import ElectricCar

# car1 = Car("Ka","Ford", 
#            "Black", "2021")
# print(car1.mileage)
# car1.start()
# car1.drive(3)
# print(car1.mileage)

ele = ElectricCar("Suv","BYD", "Red", "2023", 1.5)
# print(ele.mileage)

print("Battery:", ele.battery_level)
ele.start()
ele.drive(60)
# print(ele.mileage)
print("Battery:", ele.battery_level)
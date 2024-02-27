def sum_nums(a, b=0):
    return a + b


print(sum_nums(5))


class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []



mileage = int(input())

car = Vehicle(mileage, 150)


print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)


class Phone:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def turn_on(self):
        return 'The phone is turned on'

p1 = Phone("green", 2)
p2 = Phone("red", 10)
p3 = Phone("green", 2)

print(p3.turn_on())
print(turn_on())
print(id(p1))
print(id(p2))


class ImageArea:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    # def __eq__(self, other):
    #     return self.get_area() == other.get_area()



a1 = ImageArea(7, 10)
a2 = ImageArea(7, 10)
a3 = ImageArea(8, 9)

print(id(a1))
print(id(a2))
print(a1 != a2)

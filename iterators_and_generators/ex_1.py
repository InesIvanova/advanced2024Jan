class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = self.start - 1

    # def __iter__(self):
    #     return self
    #
    # def __next__(self):
    #     self.current += 1
    #     if self.current <= self.end:
    #         return self.current
    #     # self.current = self.start - 1
    #     raise StopIteration

    def iterate(self):
        ...
cr = custom_range(1, 5)

for obj in cr:
    print(obj)


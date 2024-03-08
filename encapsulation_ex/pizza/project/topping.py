class Topping:
    def __init__(self, topping_type: str, weight: float):
        self.topping_type = topping_type
        self.weight = weight
        # self.asd = 6

    @property
    def topping_type(self):
        return self.__topping_type

    @topping_type.setter
    def topping_type(self, value: str):
        if value == "":
            raise ValueError("The topping type cannot be an empty string")
        self.__topping_type = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value: float):
        if value <= 0:
            raise ValueError("The weight cannot be less or equal to zero")
        self.__weight = value


    # @property
    # def asd(self):
    #     return self.__asd
    #
    # @asd.setter
    # def asd(self, value):
    #     if value == "":
    #         raise ValueError
    #     self.__asd = value



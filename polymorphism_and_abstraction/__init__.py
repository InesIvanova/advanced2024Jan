class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def create_pepperoni(cls):
        return cls(["pepperoni", "tomato", "cheese"])

    @classmethod
    def create_margarita(cls):
        return cls(["cheese2", "tomato", "cheese"])


pizza = Pizza(['1', '2', '3'])
margarita = Pizza.create_margarita()
print(margarita)





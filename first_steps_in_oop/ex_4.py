class Car:
    def __init__(self, name, model, engine):
        self.name = name
        self.model = model
        self.engine = engine

    def get_info(self):
        return f"This is {self.name} {self.model} with engine {self.engine}"

    def change_name(self, new_name):
        if new_name.strip() == "":
            raise ValueError("Name can not be empty")
        self.name = new_name

    def __str__(self):
        return f"This is a car with name {self.name}"

    def __repr__(self):
        return f"This is a car with name {self.name}"



car = Car("Test", "test", "1.6")
print(car)

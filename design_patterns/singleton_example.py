def singleton(cls):
    instance = [None]
    def wrapper(*args, **kwargs):
        if instance[0] is None:
            instance[0] = cls(*args, **kwargs)
        return instance[0]

    return wrapper



class Person:
    def __init__(self):
        self.name = "Test"

    # def __new__(cls):
    #     if not hasattr(cls, 'instance'):
    #         cls.instance = super(Person, cls).__new__(cls)
    #     return cls.instance


class PersonFactory:
    def get_person(self):
        return Person()



p = PersonFactory().get_person()
print(p)
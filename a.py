class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        return 'eating..'


person = Person("Test", 12)
p2 = Person("Test", 20)

a = [1,2,3]
b = a
print(id(person))
print(id(p2))

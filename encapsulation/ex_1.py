class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def get_age(self):
        return self.__age


    def get_name(self):
        return self._name


class Student(Person):
    def say_something(self):
        return f"{self._name}"


person = Person("George", 32)
s = Student("George", 32)
print(hasattr(s, "_name"))

class Animal:
    pass

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'


class Student(Person):
    def __init__(self, first_name, last_name, fac_number):
        super().__init__(first_name, last_name)
        # Person.__init__(self, first_name, last_name)
        self.fac_number = fac_number

    def go_to_school(self):
        return f"Walking to school"

    def display_info(self):
        return f"{Person.get_full_name(self)} with fac number {self.fac_number}"

    def get_full_name(self):
        return f"{self.last_name} {self.first_name}"


class FitnessInstructor(Person):
    pass


p = Person("Test", "Testov")
s = Student("Test", "Testov","111")


print(p.get_full_name())
print(s.display_info())
# print(s.first_name)
# print(s.last_name)
# print(s.get_full_name())
# print(s.go_to_school())
# print(s.display_info())


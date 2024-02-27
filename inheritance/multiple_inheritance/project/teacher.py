from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

    def some_method(self):
        return f"{Person.sleep(self)} + something else"

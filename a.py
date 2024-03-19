def uppercase(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return result.upper()
    return wrapper



class Person:
    @uppercase
    def say_hi(self):
        return "hi"


p = Person()
print(p.say_hi())
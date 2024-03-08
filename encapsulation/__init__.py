class A:
    def say(self):
        return "A"

class B(A):
    def say(self):
        return f"{super().say()} B"

b = B()
print(b.__class__.__base__.say(b))



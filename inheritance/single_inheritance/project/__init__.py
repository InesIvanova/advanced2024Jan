class Parent:
    def say_hi(self):
        return "from parent class"

class FirstChild(Parent):
    # pass
    def say_hi(self):
        return "from FirstChild class"

class SecondChild(Parent):
    SOME_SOME = "a"
    def say_hi(self):
        return "from SecondChild class"

class GrandChild(SecondChild, FirstChild):
    SOME_SOME = "b"

    def say_hi(self):
        return FirstChild.say_hi(self)


g = GrandChild()
print(g.SOME_SOME)
print(g.say_hi())
print(GrandChild.mro())

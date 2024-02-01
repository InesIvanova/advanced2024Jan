from functools import reduce

def operate(operator, *args):
    if 0 in args and operator == "-":
        return
    return reduce(lambda x,y: eval(f"{x}{operator}{y}"), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
def sum_nums(a, b):
    return a + b


def divide_nums(a, b):
    return a/b


sign = input()


sign_mapper = {
    "+": lambda x, y: x +y,
    "/": divide_nums
}

print(sign_mapper[sign](3, 5))
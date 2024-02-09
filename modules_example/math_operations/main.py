from math import floor

from modules_example.math_operations.actions import execute_expression


def truncate(f, n):
    return floor(f * 10 ** n) / 10 ** n


expression = input()

result = execute_expression(expression)
print(f"{truncate(result, 2)}")
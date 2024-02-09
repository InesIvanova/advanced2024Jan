from math import log


number = int(input())

try:
    base = int(input())
    print(f"{log(number, base):.2f}")
except ValueError:
    print(f"{log(number):.2f}")

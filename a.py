import os

path = os.path.join("my_example.txt")


with open(path) as file:
    lines = file.readlines()
    print(file.closed)

print(file.closed)
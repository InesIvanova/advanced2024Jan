import os

path = os.path.join("resources", "just_created.txt")

try:
    os.remove(path)
except FileNotFoundError:
    print("File is already deleted")


if os.path.exists(path):
    os.remove(path)
else:
    print("File is already deleted")



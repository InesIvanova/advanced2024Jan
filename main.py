import os

path = os.path.join("file_handling", "resources", "just_created.txt")

with open(path, "a") as file:
    file.write("Some content")
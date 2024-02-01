import os


ABSOLUTE_DIR_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
file_name = "text.txt"
path = os.path.join("..", "..", "nested_folder", file_name)


try:
    file = open("text.txt", "r")
    print("File found")
except FileNotFoundError:
    print("File is not found")
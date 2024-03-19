def reverse_text(string: str):
    current_index = len(string) -1
    while current_index >= 0:
        yield string[current_index]
        current_index -= 1


for char in reverse_text("step"):
    print(char, end='')

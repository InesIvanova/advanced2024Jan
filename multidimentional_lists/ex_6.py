n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

searched_element = input()

for row_index in range(n):
    for col_index in range(len(matrix[row_index])):
        if matrix[row_index][col_index] == searched_element:
            print(f"({row_index}, {col_index})")
            exit()

print(f"{searched_element} does not occur in the matrix")


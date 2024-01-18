row = int(input())

matrix = []

for _ in range(row):
    matrix.append([int(el) for el in input().split()])


diagonal_sum = 0
for row_index in range(row):
    diagonal_sum += matrix[row_index][row_index]
print(diagonal_sum)
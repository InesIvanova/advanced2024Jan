row, col = [int(el) for el in input().split(", ")]

matrix = []
print(matrix)
for _ in range(row):
    row_nums = [int(el) for el in input().split()]
    matrix.append(row_nums)


for col_index in range(col):
    col_total = 0
    for row_index in range(row):
        col_total += matrix[row_index][col_index]
    print(col_total)

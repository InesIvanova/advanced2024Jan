row, col = [int(el) for el in input().split(", ")]

total_amount = 0
matrix = []
for i in range(row):
    row_data = [int(el) for el in input().split(", ")]
    total_amount += sum(row_data)
    matrix.append(row_data)

matrix = []
for i in range(row):
    data = input().split(", ")
    sub_list = []
    for j in range(col):
        current_element = int(data[j])
        total_amount += current_element
        sub_list.append(current_element)
    matrix.append(sub_list)

print(total_amount)
print(matrix)

a = []


row = int(input())

flatten = []
for i in range(row):
    row_data = [int(el) for el in input().split(", ")]
    flatten.extend(row_data)
print(flatten)


# flatten = []
# for row in matrix:
#     for el in row:
#         flatten.append(el)
#
# flatten = [el for row in matrix for el in row]

expression = input()
paren_indexes = []

for index in range(0, len(expression)):
    if expression[index] == "(":
        paren_indexes.append(index)
    elif expression[index] == ")":
        start_index = paren_indexes.pop()
        end_index = index + 1
        print(expression[start_index:end_index])



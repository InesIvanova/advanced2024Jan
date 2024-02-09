def get_next_position(position, direction_mapper, direction, matrix):
    current_row_index, current_col_index = position
    row_movement, col_movement = direction_mapper[direction]
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    # if 0 <= desired_row_index < len(matrix) and 0 <= desired_col_index < len(matrix):
    #     return desired_row_index, desired_col_index

    desired_row_index = (desired_row_index + len(matrix)) % len(matrix)
    desired_col_index = (desired_col_index + len(matrix)) % len(matrix)

    # if desired_row_index < 0:
    #     desired_row_index = len(matrix) - 1
    # elif desired_row_index >= len(matrix):
    #     desired_row_index = 0
    #
    # if desired_col_index < 0:
    #     desired_col_index = len(matrix) - 1
    # elif desired_col_index >= len(matrix):
    #     desired_col_index = 0

    return desired_row_index, desired_col_index


n = int(input())

direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "right": (0, 1),
    "left": (0, -1),
}

matrix = []
position = None

for row_index in range(n):
    data = list(input())

    if "S" in data:
        current_col = data.index("S")
        position = [row_index, current_col]
    matrix.append(data)


command = input()
collected_fish = 0

while command != "collect the nets":
    current_row_index, current_col_index = position
    next_row_index, next_col_index = get_next_position(position, direction_mapper, command, matrix)

    symbol = matrix[next_row_index][next_col_index]
    matrix[next_row_index][next_col_index] = "S"
    matrix[current_row_index][current_col_index] = "-"
    position = [next_row_index, next_col_index]

    if symbol.isdigit():
        collected_fish += int(symbol)
    elif symbol == "W":
        print(f"You fell into a whirlpool! "
              f"The ship sank and you lost the fish you caught. "
              f"Last coordinates of the ship: [{position[0]},{position[1]}]")
        exit()

    command = input()


if collected_fish >= 20:
    print(f"Success! You managed to reach the quota!")
else:
    print(f"You didn't catch enough fish and didn't reach the quota! "
          f"You need {20 - collected_fish} tons of fish more.")

if collected_fish > 0:
    print(f"Amount of fish caught: {collected_fish} tons.")

for row in matrix:
    print(f"{''.join(row)}")

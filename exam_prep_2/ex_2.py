def is_in_boundaries(row_index, col_index, n):
    return 0 <= row_index < n and 0 <= col_index < n


def print_board(board):
    for row in board:
        print(''.join(row))


direction_mapper = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

n = int(input())

board = []
player_position = None

for row_index in range(n):
    data = list(input())

    if "G" in data:
        col_index = data.index("G")
        player_position = [row_index, col_index]
    board.append(data)


direction = input()
money = 100

while direction != "end":
    current_row_index, current_col_index = player_position
    row_movement, col_movement = direction_mapper[direction]
    desired_row_index = current_row_index + row_movement
    desired_col_index = current_col_index + col_movement

    if not is_in_boundaries(desired_row_index, desired_col_index, n):
        print("Game over! You lost everything!")
        exit()

    symbol = board[desired_row_index][desired_col_index]
    board[desired_row_index][desired_col_index] = "G"
    board[current_row_index][current_col_index] = "-"
    player_position = [desired_row_index, desired_col_index]

    if symbol == "W":
        money += 100
    elif symbol == "P":
        money -= 200
        if money <= 0:
            money = 0
            print(f"Game over! You lost everything!")
            exit()
    elif symbol == "J":
        money += 100000
        print(f"You win the Jackpot!")
        print(f"End of the game. Total amount: {money}$")
        print_board(board)
        exit()

    direction = input()

print(f"End of the game. Total amount: {money}$")
print_board(board)

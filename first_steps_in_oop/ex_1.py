n = int(input())


def print_row(size, row):
    print(f"{' '*(size - row)}{'* ' * row}")


def print_upper_rhombus_part(size):
    for row in range(1, size + 1):
        print_row(size, row)


def print_bottom_rhombus_part(size):
    for row in range(size-1, 0, -1):
        print_row(size, row)


def print_rhombus(size):
    print_upper_rhombus_part(size)
    print_bottom_rhombus_part(size)


print_rhombus(n)
# def my_gen(n):
#     current = 1
#     while current <= n:
#         yield current
#         current += 1
#
#
#
# def my_gen2():
#     n = 1
#     print('This is printed first')
#     return n
#
#     n += 1
#     print('This is printed second')
#     return n
#
#     n += 1
#     print('This is printed at last')
#     return n
#
#
# a = my_gen(3)
#
# for el in a:
#     print(el)


def square_even(n):
    current = 1
    while current <= n:
        if current %2 ==0:
            yield current * 5
        current+=1

# result = (i * 5 for i in range(1, 5) if i%2==0)
result = square_even(5)
for el in result:
    print(el)

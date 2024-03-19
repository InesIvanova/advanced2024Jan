def nums_recursion(n):
    if n <= 0:
        return 1
    return nums_recursion(n - 1)

print(nums_recursion(5))



def genrange(start, end):
    while start <= end:
        yield start
        start += 1


print(list(genrange(1, 10)))

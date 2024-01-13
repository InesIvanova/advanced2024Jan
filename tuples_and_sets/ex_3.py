n = int(input())

names = set()

for _ in range(n):
    name = input()
    names.add(name)

for name in names:
    print(name)
arr = []

a, b = map(int, input().split())

for i in range(3):
    arr.append(a)

for i in range(4, 6):
    arr.append(b)

for i in range(6, 9):
    arr.append(a + b)

print(*arr)
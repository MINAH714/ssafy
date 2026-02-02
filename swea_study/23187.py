arr = [0] * 8

for i in range(4):
    arr[i] = 7
for j in range(4, 8):
    arr[j] = 15

print(*arr)
arr = [2, 5, 1, 6, 4, 3]

num = 0
for i in range(6):
    num += arr[i]
print(num)

max_v = arr[0]
for i in range(1, 6):
        if max_v < arr[i]:
            max_v = arr[i]

min_v = arr[0]
for i in range(1, 6):
        if min_v > arr[i]:
            min_v = arr[i]

print(max_v - min_v)
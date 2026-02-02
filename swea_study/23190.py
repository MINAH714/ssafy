arr = []
'''
for i in range(10, -3, -3):
    arr.append(i)
'''

t = 10

for _ in range(5): # 5번 반복하는 반복문
    arr.append(t)
    t -= 3

print(*arr)
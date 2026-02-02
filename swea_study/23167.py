n = int(input())

# if n % 2 == 0:
#     for i in range(n, n+11, 2):
#         print(i, end= ' ')
# else:
#     for j in range(n, n+31, 3):
#         print(j, end= ' ' )
#

if n % 2 == 0:
    for i in range(6):
        print(n + i*2, end= ' ')
else:
    for i in range(11):
        print(n + i*3, end= ' ')
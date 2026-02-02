# for 문 이론1
# n번 반복하는 반복문

n = int(input())
for i in range(n):
    print(i, end = '') # 0, 1, 2, 3 ... n-1 까지


# for문 이론 2

# 1. start < end (증가하는 경우)
for i in range(start, end + 1, step):
# 2. start > end (감소하는 경우)
for i in range(start, end - 1, step):
# 거꾸로 순회
for i in range(start, end - 1, -1):
# 핵심 : 수직선 상에서 항상 end를 포함하지 않는다.

# 리스트 이론1
# 가변시퀀스 (순서가있다)
# 인덱싱 O, 슬라이싱 O, 순회 O

arr = [1, 2, 3, 4, 5]
# 인덱싱 : 항상 0부터 시작
# 마지막 원소를 인덱싱
print(arr[-1], arr[len(arr) - 1])
# 슬라이싱(start:end:step)
# 거꾸로 슬라이싱
print(arr[::-1])


# 리스트 방법 2번
# 0으로 채워진 길이가 6인 리스트
arr = [0] * 6
# 10 부터 15까지 채워진 리스트를 만들어라

# 1. 첫 번째 방법(append)
arr = []
for i in range(10, 16):
    arr.append(i)

# 2. 두 번쨰 방법
# 0으로 이루어진 배열을 초기화하고 인덱싱
arr = [0] * 6
t = 10
for i in range(6):
    arr[i] = t
    t += 1
print(*arr)
## 두가지 방법 다 알고있고 능숙하게 풀어야 한다
import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
sum = 0
min_length = sys.maxsize

while True :
    if sum >= M:
        min_length = min(min_length, right-left)
        sum -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        sum += arr[right]
        right += 1

if min_length == sys.maxsize:
    print(0)
else:
    print(min_length)
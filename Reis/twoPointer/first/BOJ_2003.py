import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = list(map(int, input().split()))

left = 0
right = 1
cnt = 0
sum_value = A[left]

while True :
    if sum_value < M :
        if right < N :
            sum_value += A[right]
            right +=1
        else :
            break
    else :
        if sum_value == M :
            cnt +=1
        sum_value -= A[left]
        left += 1
print(cnt)

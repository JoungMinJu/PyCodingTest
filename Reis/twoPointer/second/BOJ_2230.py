import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
A = []
for _ in range(N) :
    A.append(int(input()))
A.sort()

left, right = 0, 1
answer = float('inf')

while left < N and right < N :
    tmp = A[right] - A[left]
    if tmp == M :
        answer = M
        break
    if tmp < M :
        right += 1
    else :
        left += 1
        answer = min(answer, tmp)
print(answer)
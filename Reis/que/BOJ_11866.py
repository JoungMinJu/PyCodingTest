from collections import deque
import sys

input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
que = deque()
for i in range(1, N+1) :
    que.append(i)
answer = []
for _ in range(N) :
    for _ in range(K-1) :
        que.append(que.popleft())
    answer.append(str(que.popleft()))
print("<", end = "")
print(", ".join(answer), end="")
print(">")
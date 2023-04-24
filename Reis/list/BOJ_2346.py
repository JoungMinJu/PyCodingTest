import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
que = deque(enumerate(map(int, input().split()))) # 맞네
ans = []
while que :
    idx, paper = que.popleft()
    ans.append(idx+1)
    if paper > 0 :
        que.rotate(-(paper-1))
    else :
        que.rotate(-paper)
print(" ".join(map(str, ans)))
import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()

N, M = map(int, input().split()) # N개의 원소 포함. 양방향 순환 큐
position = list(map(int, input().split()))
que = deque([i for i in range(1, N+1)])

count = 0
for pos in position :
    while True :
        if que[0] == pos :
            que.popleft()
            break
        else :
            if que.index(pos) < len(que)/2 :
                while que[0] != pos :
                    que.append(que.popleft())
                    count += 1
            else :
                while que[0] != pos :
                    que.appendleft(que.pop())
                    count += 1
print(count)
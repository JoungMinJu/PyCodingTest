import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split()) # N 큐의 크기, M 뽑아내려는 수의 개수
position = list(map(int, input().split()))
dq = deque([i for i in range(1, N+1)])

count = 0
for pos in position:
    while True:
        if dq[0] == pos:
            dq.popleft()
            break
        else:
            if dq.index(pos) < len(dq)/2 :
                while dq[0] != pos :
                    dq.append(dq.popleft())
                    count+=1
            else:
                while dq[0] != pos:
                    dq.appendleft(dq.pop())
                    count +=1
print(count)
import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def bfs(start) :
    que = deque()
    que.append((start, 0))
    visited[start] = 1
    while que :
        now, cost = que.popleft()
        if cost > T :
            return "ANG"
        if now == G :
            return cost
        if now + 1 < INF and not visited[now+1] :
            que.append((now+1, cost+1))
            visited[now+1] = 1
        if now * 2 < INF :
            tmp = str(now*2)
            if now !=  0 :
                tmp = str(int(tmp[0])-1) + tmp[1:]
            if not visited[int(tmp)] :
                que.append((int(tmp), cost+1))
                visited[int(tmp)] = 1
    return "ANG"


N, T, G = map(int, input().split())
INF = 100000
visited = [0] * (INF+1)
success = 1

print(bfs(N))
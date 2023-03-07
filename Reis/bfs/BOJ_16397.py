import sys
from collections import deque

input = sys.stdin.readline

def bfs(start) :
    q = deque()
    q.append((start, 0))
    visited[start] = True

    while q :
        now, cost = q.popleft()
        if cost > T :
            return "ANG"
        if now == G :
            return cost
        if now + 1 < INF and not visited[now+1]:
            q.append((now+1, cost+1))
            visited[now+1] = True
        if now * 2 < INF :
            tmp = str(now*2)
            if int(tmp) != 0 :
                tmp = str(int(tmp[0])-1) + tmp[1:]
            if not visited[int(tmp)] :
                q.append((int(tmp), cost+1))
                visited[int(tmp)] = True
    return "ANG"


N, T, G = map(int, input().split())
INF = 100000
visited = [False for _ in range(INF+1)]
success = True

print(bfs(N))
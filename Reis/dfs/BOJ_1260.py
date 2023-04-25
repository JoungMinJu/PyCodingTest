import sys
from collections import deque
input = lambda : sys.stdin.readline().rstrip()

def bfs(start) :
    que = deque()
    que.append(start)
    bfs_visited[start] = 1
    while que :
        now = que.popleft()
        bfs_answer.append(str(now+1))
        links = linked[now]
        for link in links :
            if not bfs_visited[link] :
                que.append(link)
                bfs_visited[link] = 1

def dfs(start) :
    dfs_answer.append(str(start+1))
    dfs_visited[start] = 1
    links = linked[start]
    for link in links :
        if not dfs_visited[link] :
            dfs(link)

N, M, V = map(int, input().split())
dfs_visited = [0] * N
bfs_visited = [0] * N
dfs_answer = []
bfs_answer = []

linked = [[] for _ in range(N)]

for _ in range(M) :
    a, b = map(int,input().split())
    linked[a-1].append(b-1)
    linked[b-1].append(a-1)

for link in linked:
    link.sort()

bfs(V-1)
dfs(V-1)

print(" ".join(dfs_answer))
print(" ".join(bfs_answer))


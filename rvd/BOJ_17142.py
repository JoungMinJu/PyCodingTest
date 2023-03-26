import copy
from collections import deque

dR = [1, -1, 0, 0]
dC = [0, 0, 1, -1]

valid_range = lambda row, col: 0 <= row < N and 0 <= col < N


def bfs(active):
    q = deque()
    visited = [[-1] * N for _ in range(N)]
    result = 0

    for x, y in active:
        q.append((x, y))
        visited[x][y] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x + dR[i], y + dC[i]

            if 0 <= nx < N and 0 <= ny < N:
                if graph[nx][ny] == 0 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
                    result = max(result, visited[nx][ny])
                elif graph[nx][ny] == 2 and visited[nx][ny] == -1:
                    q.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1

    if list(sum(visited, [])).count(-1) != wall_cnt:
        return float('inf')
    return result


def dfs(idx, active):
    global ans
    if len(active) == M:
        ans = min(ans, bfs(active))
        return
    if idx >= len(candidates):
        return
    active = copy.deepcopy(active)
    active.append(candidates[idx])
    dfs(idx + 1, active)
    active.pop()
    dfs(idx + 1, active)


N, M = map(int, input().split())
graph = []

candidates = []
wall_cnt = 0
for row in range(N):
    lst = list(map(int, input().split()))
    for col in range(N):
        if lst[col] == 2:
            candidates.append([row, col])
        elif lst[col] == 1:
            wall_cnt += 1
    graph.append(lst)

ans = float('inf')

dfs(0, [])
print(ans if ans != float('inf') else -1)

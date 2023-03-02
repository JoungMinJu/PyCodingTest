from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, list(input()))) for _ in range(n)]
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
found = False

q = deque([(0, 0, 0)])
while q:
    x, y, b = q.popleft()
    if (x, y) == (n - 1, m - 1):
        found = True
        print(visited[x][y][b])
        break
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if nx in range(n) and ny in range(m):
            if graph[nx][ny] and not b: # 다음이 벽 + 아직 벽 부수기 전
                visited[nx][ny][1] = visited[x][y][0] + 1
                q.append((nx, ny, 1))
            elif not graph[nx][ny] and not visited[nx][ny][b]: # 다음이 벽x + 방문 전
                visited[nx][ny][b] = visited[x][y][b] + 1
                q.append((nx, ny, b))
if not found: print(-1)
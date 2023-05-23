from collections import deque

def valid_range(a, b):
    return 0 <= a < N and 0 <= b < M


def bfs(x, y, z):
    que = deque()
    que.append([x, y, z])
    while que:
        a, b, c = que.popleft()
        if [a, b] == [N - 1, M - 1]:  # 도착점이면
            return visited[a][b][c]
        for idx in range(4):
            next_a, next_b = a + dR[idx], b + dC[idx]
            if not valid_range(next_a, next_b) :
                continue
            if board[next_a][next_b] == '1' and c == 0 :
                visited[next_a][next_b][1] = visited[a][b][0] + 1
                que.append([next_a, next_b, 1])
            elif board[next_a][next_b] == '0' and visited[next_a][next_b][c] == 0 :
                visited[next_a][next_b][c] = visited[a][b][c] + 1
                que.append([next_a, next_b, c])
    return -1


N, M = map(int, input().split())
# visited[x][y][0] = 안 부순 경로
# visited[x][y][1] = 부순 경로
board = [list(input()) for _ in range(N)]

visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1  # 처음부터 센다고 했음

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]
print(bfs(0,0,0))
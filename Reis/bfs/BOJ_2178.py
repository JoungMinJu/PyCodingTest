from collections import deque
import sys
input = lambda : sys.stdin.readline().rstrip()

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

def valid_range(row, col) :
    return 0 <= row < N and 0 <= col < M

def bfs(start_row, start_col) :
    que = deque()
    visited = [[0] * M for _ in range(N)]
    que.append([start_row, start_col])
    visited[start_row][start_col] = 1
    while que :
        now_row, now_col= que.popleft()
        for idx in range(4) :
            next_row, next_col = now_row + dR[idx], now_col + dC[idx]
            if not valid_range(next_row, next_col) :
                continue
            if (next_row, next_col) == (N-1, M-1) :
                return visited[now_row][now_col] + 1
            if not visited[next_row][next_col] and board[next_row][next_col] :
                visited[next_row][next_col] = visited[now_row][now_col] + 1
                que.append([next_row, next_col])


N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]

for row in range(N) :
    tmp = list(input())
    for col in range(M) :
        board[row][col] = int(tmp[col])

print(bfs(0,0))
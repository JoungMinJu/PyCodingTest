from collections import deque

def valid_range(row, col) :
    return 0 <= row < M and 0 <= col < N

'''
벽이 없는 곳을 만남 => 먼저 가게 함 appendleft
벽이 있는 곳을 만남 => append
'''

def bfs(row,col):
    visited = [[-1]*N for _ in range(M)]
    visited[row][col] = 0
    que = deque()
    que.append([row, col])
    while que :
        now_row, now_col = que.popleft()
        if [now_row, now_col] == [M - 1, N - 1]:
            return visited[now_row][now_col]
        for idx in range(4) :
            next_row, next_col = now_row + dR[idx], now_col + dC[idx]
            if not valid_range(next_row, next_col) :
                continue
            if visited[next_row][next_col] == -1 :
                if board[next_row][next_col] == '0' :
                    visited[next_row][next_col] = visited[now_row][now_col]
                    que.appendleft([next_row,next_col])
                elif board[next_row][next_col] == '1' :
                    visited[next_row][next_col] = visited[now_row][now_col] + 1
                    que.append([next_row, next_col])

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

N, M = map(int, input().split())
board = [list(input()) for _ in range(M)]
print(bfs(0, 0))

import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def valid_range(row, col) :
    return 0 <= row < R and 0 <= col < C

def bfs(start_pos) :
    visited = [[0] * C for _ in range(R)]
    que = deque()
    que.append(start_pos)
    visited[start_pos[0]][start_pos[1]] = 1
    minutes = 0
    while que :
        size = len(que)
        minutes += 1
        # 물 먼저 이동
        water_size = len(water_pos)
        for _ in range(water_size) :
            now_row, now_col = water_pos.popleft()
            for idx in range(4) :
                next_row, next_col = now_row + dR[idx], now_col + dC[idx]
                if not valid_range(next_row, next_col) :
                    continue
                if board[next_row][next_col] == '.' :
                    board[next_row][next_col] = '*'
                    water_pos.append([next_row, next_col])
        # 고슴도치 이동
        for _ in range(size) :
            now_row, now_col = que.popleft()
            for idx in range(4) :
                next_row, next_col = now_row + dR[idx], now_col + dC[idx]
                if not valid_range(next_row, next_col) :
                    continue
                if not visited[next_row][next_col] :
                    if board[next_row][next_col] == '.' :
                        visited[next_row][next_col] = 1
                        que.append([next_row, next_col])
                    elif board[next_row][next_col] == 'D' :
                        return minutes
    return -1




dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

start_pos = []
water_pos = deque()
for row in range(R) :
    for col in range(C) :
        if board[row][col] == "S" :
            start_pos = [row, col]
            board[row][col] = '.'
        if board[row][col] == "*" :
            water_pos.append([row, col])

answer = bfs(start_pos)
if answer == -1 :
    print("KAKTUS")
else :
    print(answer)
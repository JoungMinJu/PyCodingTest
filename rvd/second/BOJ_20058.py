from collections import deque
from copy import deepcopy

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

def bfs(row, col) :
    global total
    cnt = 0
    que = deque()
    que.append([row, col])
    visited[row][col] = 0
    while que :
        cnt += 1
        now_row, now_col = que.popleft()
        total += board[now_row][now_col]
        for idx in range(4) :
            next_row, next_col = now_row + dR[idx], now_col + dC[idx]
            if not valid_range(next_row, next_col) :
                continue
            if visited[next_row][next_col] == -1 :
                if board[next_row][next_col] :
                    que.append([next_row, next_col])
                    visited[next_row][next_col] = visited[now_row][now_col] +1
    return cnt



def valid_range(row, col):
    return 0 <= row < len_board and 0 <= col < len_board

def rotate_and_melting(board, len_board, L):
    new_board = [[0] * len_board for _ in range(len_board)]
    r_size = 2 ** L  # 격자 사이즈
    for row in range(0, len_board, r_size):  # 격자 시작!!! 좌표
        for col in range(0, len_board, r_size):  # 마찬가지로 격자 시작좌푤
            for i in range(r_size):  # 열!! 인덱스
                for j in range(r_size):  # 행 인덱스
                    new_board[row + j][col + i] = board[row + (r_size - 1 - i)][col + j]
    board = deepcopy(new_board)
    for row in range(len_board):
        for col in range(len_board):
            if board[row][col] > 0 :
                cnt = 0
                for idx in range(4):
                    next_row, next_col = row + dR[idx], col + dC[idx]
                    if not valid_range(next_row, next_col):
                        continue
                    elif board[next_row][next_col]:
                        cnt += 1
                if cnt < 3:
                    new_board[row][col] -= 1
    return new_board


N, Q = map(int, input().split())
len_board = 2 ** N
board = [list(map(int, input().split())) for _ in range(len_board)]
L_list = list(map(int, input().split()))

for L in L_list:
    tmp = rotate_and_melting(board, len_board, L)
    board = tmp



# 개수 세기
# 하나씩 번갈아가면서 bfs하고 또 visited 한 부분은 더하기
total = 0
max_cnt = -1
visited = [[-1] * len_board for _ in range(len_board)]
for row in range(len_board):
    for col in range(len_board):
        if board[row][col] and visited[row][col] == -1:
            tmp_cnt = bfs(row, col)
            max_cnt = max(max_cnt, tmp_cnt)
print(total)
if max_cnt <= 1 :
    print(0)
else :
    print(max_cnt)
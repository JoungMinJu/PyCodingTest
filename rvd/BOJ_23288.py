# 동 남 서 북
from collections import deque

dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]

def valid_range(row, col):
    return 0 <= row < N and 0 <= col < M

def get_score(row, col) :
    num = board[row][col]
    visited = [[0] * M for _ in range(N)]
    visited[row][col] = 1
    que = deque()
    que.append([row, col])
    count = 1
    while que :
        now_row, now_col = que.popleft()
        for idx in range(4) :
            next_row, next_col = now_row + dR[idx], now_col + dC[idx]
            if valid_range(next_row, next_col) and board[next_row][next_col] == num and not visited[next_row][next_col] :
                count += 1
                visited[next_row][next_col] = 1
                que.append([next_row, next_col])
    return count * num

def move_dice(idx) :
    if idx == 0 : # 동쪽
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    elif idx == 1 : # 남쪽
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]
    elif idx == 2 : # 서쪽
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    else : # 북쪽
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dice = [[0] * 3 for _ in range(6)] # 맨 아래 = 3행 1열

dice[0][1], dice[1][0], dice[1][1], dice[1][2], dice[2][1], dice[3][1] = 2, 4, 1, 3, 5, 6

score = 0
row = col = 0
move_idx = 0
for turn in range(K):
    move_idx %= 4
    next_row, next_col = row + dR[move_idx], col + dC[move_idx]
    if not valid_range(next_row, next_col) :
        if move_idx >= 2 :
            move_idx -= 2
        else :
            move_idx += 2
        next_row, next_col = row + dR[move_idx], col + dC[move_idx]
    move_dice(move_idx)
    board_num = board[next_row][next_col]
    dice_num = dice[3][1]
    if dice_num > board_num :
        move_idx += 1
    elif dice_num < board_num :
        if move_idx == 0 :
            move_idx = 3
        else :
            move_idx -= 1
    row, col = next_row, next_col
    score += get_score(row, col)
print(score)

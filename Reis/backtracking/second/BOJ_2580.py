import sys

input = lambda : sys.stdin.readline().rstrip()

board = [[0] * 9 for _ in range(9)]
zeros = []

def check_row(now_row, value) :
    for col in range(9) :
        if board[now_row][col] == value :
            return False
    return True

def check_col(now_col, value) :
    for row in range(9) :
        if board[row][now_col] == value :
            return False
    return True

def check_rect(now_row, now_col, value) :
    now_row = now_row//3 * 3
    now_col = now_col // 3 * 3
    for i in range(3) :
        for j in range(3) :
            if board[now_row+i][now_col+j] == value :
                return False
    return True

def dfs(idx) :
    if idx == len(zeros) :
        for i in range(9):
            print(*board[i])
        exit(0)

    for i in range(1, 10) :
        row, col = zeros[idx]

        if check_row(row, i) and check_col(col, i) and check_rect(row, col, i) :
            board[row][col] = i
            dfs(idx+1)
            board[row][col] = 0


for row in range(9) :
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for col in range(9) :
        if tmp[col] == 0 :
            zeros.append([row, col])
        board[row][col] = tmp[col]

dfs(0)
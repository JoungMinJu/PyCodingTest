import sys

def check_row(row, number):
    for col in range(9) :
        if board[row][col] == number:
            return False
    return True

def check_col(col, number) :
    for row in range(9) :
        if board[row][col] == number:
            return False
    return True

def check_rect(row, col, number) :
    next_row = row // 3 * 3
    next_col = col // 3 * 3
    for row in range(3) :
        for col in range(3) :
            if board[next_row+row][next_col+col] == number:
                return False
    return True

def dfs(idx):
    if idx == len(blank): # 마지막 빈 칸까지 다 채웠다면
        for i in range(9):
            print(*board[i])
        exit(0)

    for i in range(1, 10):
        row = blank[idx][0]
        col = blank[idx][1]
        if check_row(row, i) and check_col(col, i) and check_rect(row, col, i):
            board[row][col] = i
            dfs(idx+1)
            board[row][col] = 0


board = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(9)]

blank = []
for row in range(9):
    for col in range(9) :
        if board[row][col] == 0 :
            blank.append((row, col))

dfs(0)
import copy
from copy import deepcopy

def dfs(shark_row, shark_col, score, board) :
    global max_score
    score += board[shark_row][shark_col][0] # 번호
    max_score = max(max_score, score) # 갱신
    board[shark_row][shark_col][0] = 0 # 먹음

    for num in range(1, 17) :
        fish_row, fish_col = -1, -1
        # 하나 하나 찾기
        for row in range(4) :
            for col in range(4) :
                if board[row][col][0] == num :
                    fish_row, fish_col = row, col
                    break
        if (fish_row, fish_col) == (-1, -1) :
            continue # 없는 애는 넘어가
        fish_direction = board[fish_row][fish_col][1]

        for idx in range(8) :
            next_direction = (fish_direction + idx) % 8
            next_row, next_col = fish_row + dR[next_direction], fish_col + dC[next_direction]
            if not (0 <= next_row < 4 and 0 <= next_col < 4) or (next_row == shark_row and next_col == shark_col) :
                continue
            board[fish_row][fish_col][1] = next_direction
            board[fish_row][fish_col], board[next_row][next_col] = board[next_row][next_col], board[fish_row][fish_col]
            break
    # 상어가 먹음
    shark_direction = board[shark_row][shark_col][1]
    for i in range(1, 5) :
        next_row, next_col = shark_row + dR[shark_direction] * i, shark_col + dC[shark_direction] * i
        if (0 <= next_row < 4 and 0 <= next_col < 4) and board[next_row][next_col][0] > 0 :
            dfs(next_row, next_col, score, copy.deepcopy(board))


board = [[] for _ in range(4)]
dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, -1, -1, -1, 0, 1, 1, 1]

for row in range(4) :
    data = list(map(int, input().split()))
    fish = []
    for col in range(4) :
        fish.append([data[2*col], data[2*col+1]-1]) # [번호, 방향]
    board[row] = fish

max_score = 0
dfs(0, 0, 0, board)
print(max_score)
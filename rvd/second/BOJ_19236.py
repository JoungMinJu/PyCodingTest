from copy import deepcopy

def valid_range(row, col) :
    return 0 <= row < 4 and 0 <= col < 4

def dfs(shark, fish, board, count) :
    global answer
    shark_r, shark_c, shark_d = shark
    # 상어가 먹음
    shark_d = fish[board[shark_r][shark_c]][2]
    count += board[shark_r][shark_c]
    fish[board[shark_r][shark_c]] = [-1, -1, -1]
    board[shark_r][shark_c] = 0
    # 물고기 이동
    for f in fish :
        f_row, f_col, f_d = f
        if [f_row, f_col] == [-1, -1] :
            continue
        next_f_row, next_f_col, next_f_d = fish_move(shark_r, shark_c, f_row, f_col, f_d)
        if [next_f_row, next_f_col] == [-1, -1] :
            continue
        # 바꾸기
        origin_fish = board[next_f_row][next_f_col]
        now_fish = board[f_row][f_col]
        board[f_row][f_col], board[next_f_row][next_f_col] = board[next_f_row][next_f_col], board[f_row][f_col]
        # 각자 위치 바꿔주기
        if origin_fish != 0 :
            fish[origin_fish][0], fish[origin_fish][1] = f_row, f_col
        fish[now_fish][0], fish[now_fish][1] = next_f_row, next_f_col
        # 방향도 바꾸기
        fish[now_fish][2] = next_f_d
    # 상어 이동
    flag = 0
    for length in range(1, 5) :
        next_shark_r, next_shark_c = shark_r + dR[shark_d] * length, shark_c + dC[shark_d] * length
        if not valid_range(next_shark_r, next_shark_c) :
            break
        if not board[next_shark_r][next_shark_c] :
            continue
        next_board= deepcopy(board)
        next_fish = deepcopy(fish)
        dfs([next_shark_r, next_shark_c, shark_d], next_fish, next_board, count)
        flag = 1
    if not flag: # 상어가 밖으로 나갔다면
        answer = max(answer, count)
        return


def fish_move(shark_row, shark_col, row, col, d) :
    flag = 0
    for _ in range(8) :
        next_row, next_col = row + dR[d % 8], col + dC[d % 8]
        if not valid_range(next_row, next_col) :
            d += 1
            continue
        elif [shark_row, shark_col] == [next_row, next_col] :
            d += 1
            continue
        else :
            return next_row, next_col, d % 8
    return -1, -1, -1 # 실패면


dR = [-1, -1, 0, 1, 1, 1, 0, -1]
dC = [0, -1, -1, -1, 0, 1, 1, 1]

shark = [] # 위치, 방향
fish = [[-1, -1,-1] for _ in range(17)] # 위치, 방향
board = [[0] * 4 for _ in range(4)] # 물고기 번호
for row in range(4) :
    tmp = list(map(int, input().split()))
    for col in range(4) :
        num, direction = tmp[col*2],tmp[col*2+1]
        board[row][col] = num
        fish[num] = [row, col, direction-1]

# 상어가 처음 위치
answer = 0
shark = [0, 0, fish[board[0][0]][2]] # 위치, 방향
dfs(shark, fish, board, 0)
print(answer)

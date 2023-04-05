from copy import deepcopy

def move(type, red, blue) :
    answer_red = answer_blue = []
    if type == 0 :
        if red[0] <= blue[0]:
            answer_red = real_move(red, [], type)
            answer_blue = real_move(blue, answer_red, type)
        else:
            answer_blue = real_move(blue, [], type)
            answer_red = real_move(red, answer_blue, type)
    elif type == 1 :
        if red[1] >= blue[1]:
            answer_red = real_move(red, [], type)
            answer_blue = real_move(blue, answer_red, type)
        else:
            answer_blue = real_move(blue, [], type)
            answer_red = real_move(red, answer_blue, type)
    elif type == 2 :
        if red[0] >= blue[0]:
            answer_red = real_move(red, [], type)
            answer_blue = real_move(blue, answer_red, type)
        else:
            answer_blue = real_move(blue, [], type)
            answer_red = real_move(red, answer_blue, type)
    elif type == 3 :
        if red[1] <= blue[1]:
            answer_red = real_move(red, [], type)
            answer_blue = real_move(blue, answer_red, type)
        else:
            answer_blue = real_move(blue, [], type)
            answer_red = real_move(red, answer_blue, type)
    return answer_red + answer_blue

def real_move(target_pos, except_pos, idx) :
    now_row, now_col = target_pos[0], target_pos[1]
    while True :
        next_row, next_col = now_row + dR[idx], now_col + dC[idx]
        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M :
            break
        if board[next_row][next_col] == '#' or (next_row, next_col) == except_pos :
            return now_row, now_col
        elif board[next_row][next_col] == "O" :
            return -1, -1 # 현재 구슬 위치를 줄 수도 있음
        now_row, now_col = next_row, next_col

def dfs(red, blue, cnt) :
    global answer
    if cnt > answer :
        return
    if cnt > 10 :
        return
    flag = 0
    for idx in range(4) :
        red_blue_info = move(idx, red, blue)
        now_red = red_blue_info[:2]
        now_blue = red_blue_info[2:]
        if now_blue == blue and now_red == red :
            continue
        else :
            flag = 1
            if [now_blue[0], now_blue[1]] == [-1, -1]:
                continue
            elif [now_red[0], now_red[1]] == [-1, -1]:
                answer = min(answer, cnt)
                continue
            dfs(now_red, now_blue, cnt+1)

# 상 우 하 좌
dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

N, M = map(int, input().split())
board = []
red = []
blue = []
for row in range(N) :
    tmp = list(input())
    board.append(tmp)
    for col in range(M) :
        if tmp[col] == 'R':
            red = (row, col)
            tmp[col] = '.'
        elif tmp[col] == 'B' :
            blue = (row, col)
            tmp[col]= '.'

# bfs 진행
answer = float('inf')

dfs(red, blue, 1)
if answer == float('inf') :
    print(-1)
else :
    print(answer)
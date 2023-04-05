red = [[0]*4 for _ in range(4)]
blue = [[0] * 6 for _ in range(4)]
green = [[0] * 4 for _ in range(6)]

# 하 우
dR = [1, 0]
dC = [0, 1]

REMOVE_GREEN = [0] * 4

def move_one_block(row, col, idx, board) :
    now_row, now_col = row, col
    while True :
        next_row, next_col = now_row + dR[idx], now_col + dC[idx]
        if next_row >= 6 or next_col >= 6 or board[next_row][next_col] :
            return now_row, now_col
        now_row, now_col = next_row, next_col

def move_green(t, row, col) :
    next_row, next_col = move_one_block(-1, col, 0, green)
    if t == 1 :
        green[next_row][next_col] = 1
    elif t == 2 :
        next_row2, next_col2 = move_one_block(-1, col+1, 0, green)
        next_row = min(next_row, next_row2)
        green[next_row][next_col] = 1
        green[next_row][next_col+1] = 1
    elif t == 3 :
        green[next_row][next_col] = 1
        green[next_row-1][next_col] = 1


def move_blue(t, row, col) :
    next_row, next_col = move_one_block(row, -1, 1, blue)
    if t == 1 :
        blue[next_row][next_col] = 1
    elif t == 2 :
        blue[next_row][next_col] = 1
        blue[next_row][next_col-1] = 1
    elif t == 3 :
        next_row2, next_col2 = move_one_block(row+1, -1, 1, blue)
        next_col = min(next_col, next_col2)
        blue[next_row][next_col] = 1
        blue[next_row+1][next_col] = 1

def update_green(remove_row):
    if len(remove_row) == 0 :
        return green
    new_green = [[0] * 4 for _ in range(6)]
    new_row, now_row = 5, 5
    while now_row >= 0 :
        if not now_row in remove_row :
            for col in range(4) :
                new_green[new_row][col] = green[now_row][col]
            new_row -=1
            now_row -=1
        else :
            now_row -= 1
    return new_green

def update_blue(remove_col) :
    if len(remove_col) == 0 :
        return blue
    new_blue = [[0] * 6 for _ in range(4)]
    new_col, now_col = 5, 5
    while now_col >= 0 :
        if not now_col in remove_col:
            for row in range(4) :
                new_blue[row][new_col] = blue[row][now_col]
            new_col -= 1
            now_col -= 1
        else :
            now_col -= 1
    return new_blue

def removed_green() :
    global score
    removed_row = []
    for row in range(6) :
        tmp = sum(green[row])
        if tmp == 4 :
            removed_row.append(row)
            score +=1
    return removed_row

def removed_blue() :
    global score
    removed_col = []
    for col in range(6) :
        tmp = 0
        for row in range(4) :
            tmp += blue[row][col]
        if tmp == 4 :
            removed_col.append(col)
            score +=1
    return removed_col

def check_special_green() :
    removed_row = 0
    for row in range(2) :
        for col in range(4) :
            if green[row][col] :
                removed_row +=1
                break
    return removed_row

def check_special_blue() :
    removed_col = 0
    for col in range(2) :
        for row in range(4) :
            if blue[row][col] :
                removed_col += 1
                break
    return removed_col

def update_special_green() :
    lst = [5, 4]
    cnt = check_special_green()
    return update_green(lst[:cnt])

def update_special_blue() :
    lst = [5, 4]
    cnt = check_special_blue()
    return update_blue(lst[:cnt])


# 내꺼
def print_status() :
    print("** GREEN **")
    for row in range(6) :
        print(*green[row])
    print()
    print("**BLUE**")
    for row in range(4) :
        print(*blue[row])
    print()

N = int(input())

score = 0
for _ in range(N):
    # 블록 위치 주어짐
    t, row, col = map(int, input().split())
    move_green(t, row, col)
    move_blue(t, row, col)
    # 초록 보드 -> 가득 찬 행 체크
    removed_row = removed_green()
    removed_col = removed_blue()
    green = update_green(removed_row)
    blue = update_blue(removed_col)
    # 연한 부분 체크
    green = update_special_green()
    blue = update_special_blue()


print(score)
answer = 0
for row in range(6) :
    answer += sum(green[row])
for row in range(4) :
    answer += sum(blue[row])
print(answer)
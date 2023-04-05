valid_range = lambda row, col : 0 <= row < R and 0 <= col < C

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

up = down = -1

# 공기청정기 위치
for row in range(R) :
    if arr[row][0] == -1 :
        up = row
        down = row +1
        break

# 확산
def spread() :
    dR = [-1, 0, 0, 1]
    dC = [0, -1, 1, 0]

    tmp_arr = [[0] * C for _ in range(R)]
    for row in  range(R) :
        for col in range(C) :
            if arr[row][col] != 0 and arr[row][col] != -1 : # 숫자가 있는 칸이면
                tmp = 0
                for idx in range(4) :
                    next_row, next_col = row + dR[idx], col + dC[idx]
                    if valid_range(next_row, next_col) and arr[next_row][next_col] != -1 :
                        tmp_arr[next_row][next_col] += arr[row][col] // 5
                        tmp += arr[row][col] // 5
                arr[row][col] -= tmp
    for row in range(R) :
        for col in range(C) :
            arr[row][col] += tmp_arr[row][col]

# 위쪽으로 이동
def air_up() :
    dR = [0, -1, 0, 1]
    dC = [1, 0, -1, 0]
    direct = before = 0
    row, col = up, 1 # 공기청정기 바로 옆!
    while True :
        next_row, next_col = row + dR[direct], col + dC[direct]
        if row == up and col == 0 : # 현재 위치가 공기 청정기면
            break
        if not valid_range(next_row, next_col) :
            direct += 1
            continue
        arr[row][col], before = before, arr[row][col]
        row, col = next_row, next_col

def air_down() :
    dR = [0, 1, 0, -1]
    dC = [1, 0, -1, 0]
    direct = before = 0
    row, col = down , 1
    while True :
        next_row, next_col = row + dR[direct], col + dC[direct]
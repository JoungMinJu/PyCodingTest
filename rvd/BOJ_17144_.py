from collections import deque

valid_range = lambda row, col : 0 <= row < R and 0 <= col < C

def swap(row, col, value) :
    tmp = graph[row][col]
    graph[row][col] = value
    return tmp

def move_up() :
    dR = [0, -1, 0, 1] # 오 위 왼 아
    dC = [1, 0, -1, 0]
    row, col = up
    before = 0
    idx = 0
    while True :
        row, col = row + dR[idx], col + dC[idx]
        if not valid_range(row, col) :
            row, col = row - dR[idx], col - dC[idx]
            idx += 1
            continue
        if [row, col] == up :
            break
        before = swap(row, col, before)

def move_down() :
    dR = [0, 1, 0, -1]# 오 아 왼 위
    dC = [1, 0, -1, 0]
    row, col = down
    before = 0
    idx = 0
    while True :
        row, col = row + dR[idx], col + dC[idx]
        if not valid_range(row, col) :
            row, col = row - dR[idx], col - dC[idx]
            idx += 1
            continue
        if [row, col] == down :
            break
        before = swap(row, col, before)


R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]
up = []
down = []

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

for _ in range(T) :
    # 모으기
    que = deque()
    for row in range(R) :
        for col in range(C) :
            if graph[row][col] == -1 :
                if len(up) == 0 :
                    up.append(row)
                    up.append(col)
                elif len(down) == 0 :
                    down.append(row)
                    down.append(col)
            elif graph[row][col] > 0 :
                que.append([row, col, graph[row][col]])
    # 확산하기
    while que :
        now_row, now_col, now_value = que.popleft()
        count = 0
        for idx in range(4) :
            next_row, next_col = now_row + dR[idx], now_col + dC[idx]
            if not valid_range(next_row, next_col) or [next_row, next_col] == up or [next_row, next_col] == down :
                continue
            else :
                count += 1
                graph[next_row][next_col] += (now_value//5)
        graph[now_row][now_col] -= (now_value//5)*count
    move_up()
    move_down()
    # 아래꺼
# 계산하기
sum = 0
for row in range(R) :
    for col in range(C) :
        if [row, col] == up or [row, col] == down :
            continue
        sum += graph[row][col]

print(sum)
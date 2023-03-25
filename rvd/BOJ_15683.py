from copy import deepcopy

valid_range = lambda row, col : 0 <= row < N and 0 <= col < M

def dfs(depth, arr) :
    global min_value
    if depth == len(cctv) :
        count = 0
        for i in range(N) :
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return
    tmp = deepcopy(arr)
    cctv_num, row, col = cctv[depth]
    for i in mode[cctv_num] : # i 는 [0] or [0, 2] ..
        fill(tmp, i, row, col)
        dfs(depth+1, tmp)
        tmp = deepcopy(arr) # 복구

def fill(board, moves, row, col) :
    for move in moves :
        next_row, next_col = row, col
        while True :
            next_row += dR[move]
            next_col += dC[move]
            if not valid_range(next_row, next_col) or board[next_row][next_col] == 6 :
                break
            elif board[next_row][next_col] == 0 :
                board[next_row][next_col] = -1

N, M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)] # 0 빈칸 1~5 씨씨티비 6 벽
cctv_nums = range(1, 6)
cctv = []

# 회전 할 때 바라보는 방향 넣어줌
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]],
]

# 북 0 동 1 남 2 서 3
dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]


for row in range(N) :
    for col in range(M) :
        if graph[row][col] in cctv_nums :
            cctv.append([graph[row][col], row, col])


min_value = int(1e9)
dfs(0, graph)
print(min_value)
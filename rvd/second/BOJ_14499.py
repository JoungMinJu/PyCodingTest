def valid_range(row, col) :
    return 0 <= row < N and 0 <= col < M

def move(type) :
    if type == 1 : # 동쪽
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[3][1], dice[1][0], dice[1][1], dice[1][2]
    elif type == 2 : # 서쪽
        dice[1][0], dice[1][1], dice[1][2], dice[3][1] = dice[1][1], dice[1][2], dice[3][1], dice[1][0]
    elif type == 3 : # 북쪽
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[1][1], dice[2][1], dice[3][1], dice[0][1]
    elif type == 4 : # 남쪽
        dice[0][1], dice[1][1], dice[2][1], dice[3][1] = dice[3][1], dice[0][1], dice[1][1], dice[2][1]


N, M, row, col, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

commands = list(map(int, input().split()))

dR = [0, 0, 0, -1, 1]
dC = [0, 1, -1, 0, 0]

dice = [[0, 0, 0], [0, 0, 0],[0,0,0],[0,0,0]]
for command in commands:
    next_row, next_col = row + dR[command], col + dC[command]
    if not valid_range(next_row, next_col) :
        continue
    move(command)
    if board[next_row][next_col] :
        dice[3][1] = board[next_row][next_col]
        board[next_row][next_col] = 0
    else :
        board[next_row][next_col] = dice[3][1]
    print(dice[1][1])
    row, col = next_row, next_col
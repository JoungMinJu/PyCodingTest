# 북 서 남 동
dR = [-1, 0, 1, 0]
dC = [0, -1, 0, 1]


def get_idx(idx):
    if idx == 0:
        return idx
    if idx == 1:
        return 3
    if idx == 2:
        return 2
    return 1

def check(row, col) :
    for idx in range(4) :
        next_row, next_col = row + dR[idx], col + dC[idx]
        if not valid_range(next_row, next_col) :
            continue
        if board[next_row][next_col] == 0 :
            return True
    return False

def move(row, col):
    global answer, move_idx
    while True :
        #  일단 지금 내 칸을 변형
        if not visited[row][col] :
            answer += 1
            board[row][col] = 2
            visited[row][col] = True
        # 주변에 빈칸이 없으면
        if not check(row, col) :
            next_row, next_col = row - dR[move_idx], col - dC[move_idx]
            if not valid_range(next_row, next_col) :
                break
            else :
                row, col = next_row, next_col
        # 빈 칸이 있으면
        else :
            move_idx = (move_idx+1) % 4
            next_row, next_col = row + dR[move_idx], col + dC[move_idx]
            if not valid_range(next_row, next_col) :
                continue
            elif board[next_row][next_col] == 0 :
                row, col = next_row, next_col


valid_range = lambda row, col: 0 <= row < N and 0 <= col < M and board[row][col] != 1
N, M = map(int, input().split())
now_row, now_col, move_idx = map(int, input().split())
move_idx = get_idx(move_idx)

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
answer = 0

move(now_row, now_col)
print(answer)
from collections import deque


def valid_range(row, col):
    return 0 <= row < N and 0 <= col < N


def bfs(row, col, color):
    que = deque()
    que.append([row, col])

    block_cnt, rainbow_cnt = 1, 0
    blocks, rainbows = [[row, col]], []

    while que:
        row, col = que.popleft()
        for d in range(4):
            next_row, next_col = row + dR[d], col + dC[d]
            if valid_range(next_row, next_col):
                if not visited[next_row][next_col] and board[next_row][next_col] == color:
                    visited[next_row][next_col] = 1
                    que.append([next_row, next_col])
                    block_cnt += 1
                    blocks.append([next_row, next_col])
                elif not visited[next_row][next_col] and board[next_row][next_col] == 0:
                    visited[next_row][next_col] = 1
                    que.append([next_row, next_col])
                    block_cnt += 1
                    rainbow_cnt += 1
                    rainbows.append([next_row, next_col])
    for row, col in rainbows:
        visited[row][col] = 0
    return [block_cnt, rainbow_cnt, blocks + rainbows]


def remove(block):
    for row, col in block:
        board[row][col] = -2


def gravity(a):
    for i in range(N - 2, -1, -1):  # 밑에서 부터 체크
        for j in range(N):
            if a[i][j] > -1:  # -1이 아니면 아래로 다운
                r = i
                while True:
                    if 0 <= r + 1 < N and a[r + 1][j] == -2:  # 다음행이 인덱스 범위 안이면서 -2이면 아래로 다운
                        a[r + 1][j] = a[r][j]
                        a[r][j] = -2
                        r += 1
                    else:
                        break

def rotate(a) : # 이거 방식 기억!
    new_a = [[0]*N for _ in range(N)]
    for row in range(N) :
        for col in range(N) :
            new_a[N-1-col][row] = a[row][col]
    return new_a


dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
score = 0

while True :
    visited = [[0] * N for _ in range(N)]
    blocks = []
    for row in range(N) :
        for col in range(N) :
            if board[row][col] > 0 and not visited[row][col] :
                visited[row][col] = 1
                block_info = bfs(row, col, board[row][col])
                if block_info[0] >= 2 :
                    blocks.append(block_info)
    blocks.sort(reverse=True)

    if not blocks :
        break
    remove(blocks[0][2])
    score += blocks[0][0]**2

    gravity(board)
    board = rotate(board)
    gravity(board)
print(score)
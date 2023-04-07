from collections import deque

# 무지개 = 0 # 빈칸 = -2
dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]


def valid_range(row, col):
    return 0 <= row < N and 0 <= col < N


def bfs(row, col, visited):
    que = deque()
    que.append([row, col])
    rainbows = []  # 무지개블록들
    others = [[row, col]]  # 나머지 애들
    now_color = board[row][col]
    while que:
        now_row, now_col = que.popleft()
        for idx in range(4):
            next_row, next_col = now_row + dR[idx], now_col + dC[idx]
            if not valid_range(next_row, next_col):
                continue
            if not visited[next_row][next_col]:
                if board[next_row][next_col] == now_color:
                    others.append([next_row, next_col])
                    visited[next_row][next_col] = 1
                    que.append([next_row, next_col])
                elif board[next_row][next_col] == 0:
                    rainbows.append([next_row, next_col])
                    visited[next_row][next_col] = 1
                    que.append([next_row, next_col])
    # 총 개수, 무지개블록 개수, 기준블록, 모든 좌표
    # 블록이 한 개 밖에 없으면
    other_cnt = len(others)
    rainbow_cnt = len(rainbows)
    if other_cnt == 1 and rainbow_cnt == 0:
        return -1, -1, [], [], []
    # 기준 블록 구하기
    others.sort()
    return (other_cnt + rainbow_cnt), rainbow_cnt, others[0], others + rainbows, rainbows


def find_group():
    visited = [[0] * N for _ in range(N)]
    groups = []  # 총 개수, 무지개 블록 개수, 기준 블록정보, 총 pos
    for row in range(N):
        for col in range(N):
            if not visited[row][col] and board[row][col] >= 1:
                visited[row][col] = 1
                total_cnt, rainbow_cnt, basic_pos, pos, rainbow_pos = bfs(row, col, visited)
                # 무지개는 visited원상복구
                for r_row, r_col in rainbow_pos:
                    visited[r_row][r_col] = 0
                if total_cnt == -1:
                    continue
                groups.append([total_cnt, rainbow_cnt, basic_pos, pos])
    # 그룹 정렬
    if len(groups) == 0:
        return -1, -1, [], []
    groups.sort(key=lambda x: (-x[0], -x[1], -x[2][0], -x[2][1]))
    return groups.pop(0)


def gravity():
    for col in range(N):
        now_row = N - 1
        next_row = now_row - 1
        while now_row >= 0 and next_row >= 0 and now_row > next_row:
            next_num = board[next_row][col]
            if next_num == -1:  # 무지개 블록이면
                now_row = next_row
            elif next_num >= 0:
                board[next_row][col] = -2
                if board[now_row][col] == -2 :
                    board[now_row][col] = next_num
                elif board[now_row][col] != -2 :
                    board[now_row - 1][col] = next_num
                    now_row -= 1
            next_row -= 1


def rotate():
    new_board = [[-2] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            new_board[row][col] = board[col][N - 1 - row]
    return new_board


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
score = 0

while True:
    group = find_group()
    total_cnt = group[0]
    if total_cnt == -1:
        break
    pos = group[3]
    score += (total_cnt ** 2)
    for row, col in pos:
        board[row][col] = -2
    gravity()
    board = rotate()
    gravity()
print(score)

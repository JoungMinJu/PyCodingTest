# 알파 => 55%
valid_range = lambda row, col: 0 <= row < N and 0 <= col < N

moved_info = [[[3, 2]],
              [[0, 1], [3, 1]],
              [[3, 1]],
              [[2, 1], [3, 1]],
              [[0, 2]],
              [[0, 1], [1, 1]],
              [[1, 1]],
              [[1, 1], [2, 1]],
              [[1, 2]]]  # n만큼 더하고 m만큼 곱함

percent = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]


def move(row, col, now_idx):
    global answer
    y = board[row][col]
    if y != 0:
        moved_sand = 0
        for moved_idx in range(9):
            moved = moved_info[moved_idx]
            next_row, next_col = row, col
            for m in moved:
                next_idx = (now_idx + m[0]) % 4
                next_row += dR[next_idx] * m[1]
                next_col += dC[next_idx] * m[1]
            now_moved_sand = int(y * percent[moved_idx])
            moved_sand += now_moved_sand
            if not valid_range(next_row, next_col) :
                answer += now_moved_sand
                continue
            board[next_row][next_col] += now_moved_sand
        # 알파 칸 이동
        next_row, next_col = row + dR[now_idx], col + dC[now_idx]
        if not valid_range(next_row, next_col) :
            answer += (y - moved_sand)
        else :
            board[next_row][next_col] += (y - moved_sand)


def solve():
    global answer, length, idx
    cnt = 0
    row = col = N // 2
    while True:
        cnt += 1
        for l in range(length):
            # 이동하는 위치 찾기
            next_row, next_col = row + dR[idx], col + dC[idx]
            move(next_row, next_col, idx)
            # 이동하기
            row, col = next_row, next_col
            if [row, col] == [0, 0]:
                return
        # 방향 바꿔
        idx = (idx + 1) % 4
        if cnt % 2 == 0:
            length += 1


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# 우 상 좌 하 (우 넘어갈 때 늘리기)
dR = [0, -1, 0, 1]
dC = [1, 0, -1, 0]
idx = 2
length = 1
answer = 0

solve()
print(answer)

delta = (
    (0, 1),  # 0 동
    (1, 0),  # 1 남
    (0, -1),  # 2 서
    (-1, 0)  # 3 북
)

change = (
    (2, 0, 3, 1),
    (2, 3, 1, 0),
    (1, 3, 0, 2),
    (3, 2, 0, 1),
    (2, 3, 0, 1)
)

def shoot(row, col, dir):
    startr = row
    startc = col
    score = 0
    while True:
        dr, dc = delta[dir]
        row += dr
        col += dc
        if not (0 <= row < N and 0 <= col < N):
            dir = (dir + 2) % 4
            score += 1
        else:
            if (row, col) == (startr, startc) or board[row][col] == -1:
                break
            elif 1 <= board[row][col] <= 5:
                dir = change[board[row][col] - 1][dir]
                score += 1
            elif 6 <= board[row][col] <= 10:
                row, col = gate[(row, col)]
    global maxScore
    if score > maxScore:
        maxScore = score


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    tmp = {}
    gate = {}
    board = [list(map(int, input().split())) for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if 6 <= board[r][c] <= 10:
                if board[r][c] in tmp:
                    gate[tmp[board[r][c]]] = (r, c)
                    gate[(r, c)] = tmp[board[r][c]]
                else:
                    tmp[board[r][c]] = (r, c)

    maxScore = -1
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                for dir in range(4):
                    shoot(r, c, dir)

    print('#%d' % test_case, end=' ')
    if maxScore == -1:
        print(0)
    else:
        print(maxScore)

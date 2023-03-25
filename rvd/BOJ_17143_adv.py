def fish(col) :
    for row in range(R) :
        if board[row][col] :
            x = board[row][col][2]
            board[row][col] = 0
            return x
    return 0

def move() :
    global board
    new_board = [[0 for _ in range(C)] for _ in range(R)]
    for row in range(R) :
        for col in range(C) :
            if board[row][col] :
                next_row, next_col, next_direction = get_next_loc(row, col, board[row][col][0], boar[row][col][1])
                if new_board[next_row][next_col] :
                    new_board[next_row][next_col] = max (
                        new_board[next_row][next_col],
                        (board[row][col][0], next_direction, board[row][col][2]),
                        key = lambda x : x[2]
                    )
                else :
                    new_board[next_row][next_col] = (board[row][col][0], next_direction, board[row][col][2])
    board = new_board


## 여기 진짜 진짜 진짜 진짜 이해하기
def get_next_loc(i, j, speed, dir):

    if dir == UP or dir == DOWN:  # i
        cycle = R * 2 - 2
        if dir == UP:
            speed += 2 * (R - 1) - i
        else:
            speed += i

        speed %= cycle
        if speed >= R:
            return (2 * R - 2 - speed, j, UP)
        return (speed, j, DOWN)

    else:  # j
        cycle = C * 2 - 2
        if dir == LEFT:
            speed += 2 * (C - 1) - j
        else:
            speed += j

        speed %= cycle
        if speed >= C:
            return (i, 2 * C - 2 - speed, LEFT)
        return (i, speed, RIGHT)


UP, DOWN, RIGHT, LEFT = 1, 2, 3, 4
R, C, M = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]

for i in range(M):
    r, c, s, d, z = map(int, input().split())
    board[r-1][c-1] = (s, d, z)

ans = 0
for j in range(C) :
    ans += fish(j)
    move()
print(ans)


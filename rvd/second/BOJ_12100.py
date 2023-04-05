import copy


def valid_range(row, col):
    return 0 <= row < N and 0 <= col < N

def dfs(board, cnt):
    global answer
    now_max = get_max(board)
    answer = max(answer, now_max)
    if cnt > 5:
        return
    for idx in range(4):
        next_board = move(board, idx)
        if next_board != board:
            dfs(next_board, cnt + 1)


def get_max(board):
    answer = -1
    for row in range(N):
        answer = max(answer, max(board[row]))
    return answer


def move(board, idx):
    now_board = copy.deepcopy(board)
    if idx == 0:
        move_up(now_board)
    elif idx == 1:
        move_right(now_board)
    elif idx == 2:
        move_down(now_board)
    else:
        move_left(now_board)
    return now_board


def move_up(board):
    for col in range(N):
        now_row_idx = 0
        while True:
            if now_row_idx == N - 1:
                break
            now_num = board[now_row_idx][col]
            flag = 0
            for next_row_idx in range(now_row_idx + 1, N):
                now_num = board[now_row_idx][col]
                next_num = board[next_row_idx][col]
                if next_num != 0:
                    # 지금이 0이면 걍 그 자리 채우고 now_num 유지
                    if now_num == 0:
                        flag = 1
                        board[now_row_idx][col] = next_num
                        board[next_row_idx][col] = 0
                        break
                    elif now_num == next_num:
                        flag = 1
                        board[now_row_idx][col] *= 2
                        board[next_row_idx][col] = 0
                        now_row_idx += 1
                        break
                    elif board[now_row_idx + 1][col] == 0:
                        flag = 1
                        board[now_row_idx + 1][col] = next_num
                        board[next_row_idx][col] = 0
                        now_row_idx += 1
                        break
                    else:
                        now_row_idx += 1
            if not flag:  # 바꿀게 없었으면
                break


def move_down(board):
    for col in range(N):
        now_row_idx = N - 1
        while True:
            if now_row_idx == 0:
                break
            flag = 0
            for next_row_idx in range(now_row_idx - 1, -1, -1):
                now_num = board[now_row_idx][col]
                next_num = board[next_row_idx][col]
                if next_num != 0:
                    if now_num == 0:
                        flag = 1
                        board[now_row_idx][col] = next_num
                        board[next_row_idx][col] = 0
                        break
                    elif now_num == next_num:
                        flag = 1
                        board[now_row_idx][col] *= 2
                        board[next_row_idx][col] = 0
                        now_row_idx -= 1
                        break
                    elif board[now_row_idx - 1][col] == 0:
                        flag = 1
                        board[now_row_idx - 1][col] = next_num
                        board[next_row_idx][col] = 0
                        now_row_idx -= 1
                        break
                    else :
                        now_row_idx -= 1
            if not flag:  # 바꿀게 없었으면
                break


def move_left(board):
    for row in range(N):
        now_col_idx = 0
        while True:
            if now_col_idx == N - 1:
                break
            flag = 0
            for next_col_idx in range(now_col_idx + 1, N):
                now_num = board[row][now_col_idx]
                next_num = board[row][next_col_idx]
                if next_num != 0:
                    if now_num == 0:
                        flag = 1
                        board[row][now_col_idx] = next_num
                        board[row][next_col_idx] = 0
                        break
                    elif now_num == next_num:
                        flag = 1
                        board[row][now_col_idx] *= 2
                        board[row][next_col_idx] = 0
                        now_col_idx += 1
                        break
                    elif board[row][now_col_idx + 1] == 0:
                        flag = 1
                        board[row][now_col_idx + 1] = next_num
                        board[row][next_col_idx] = 0
                        now_col_idx += 1
                        break
                    else :
                        now_col_idx += 1
            if not flag:  # 바꿀게 없었으면
                break


def move_right(board):
    for row in range(N):
        now_col_idx = N - 1
        while True:
            if now_col_idx == 0:
                break
            flag = 0
            for next_col_idx in range(now_col_idx - 1, -1, -1):
                now_num = board[row][now_col_idx]
                next_num = board[row][next_col_idx]
                if next_num != 0:
                    if now_num == 0:
                        flag = 1
                        board[row][now_col_idx] = next_num
                        board[row][next_col_idx] = 0
                        break
                    elif now_num == next_num:
                        flag = 1
                        board[row][now_col_idx] *= 2
                        board[row][next_col_idx] = 0
                        now_col_idx -= 1
                        break
                    elif board[row][now_col_idx - 1] == 0:
                        flag = 1
                        board[row][now_col_idx - 1] = next_num
                        board[row][next_col_idx] = 0
                        now_col_idx -= 1
                        break
                    else :
                        now_col_idx -=1
            if not flag:  # 바꿀게 없었으면
                break


dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = -1
dfs(board, 1)
print(answer)

def print_b(board) :
    for row in range(N) :
        print(*board[row])
    print()




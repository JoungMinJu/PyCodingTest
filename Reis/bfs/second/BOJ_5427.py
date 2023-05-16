from collections import deque

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

w = h = 0

def valid_range(row, col) :
    return 0 <= row < h and 0 <= col < w

def move(board, start, fires) :
    visited = [[0] * len(board[0]) for _ in range(len(board))]
    visited[start[0]][start[1]] = 1
    que = deque()
    que.append(start)
    move_count = 0
    while que :
        size = len(que)
        move_count += 1
        # 불 움직임
        fire_size= len(fires)
        for _ in range(fire_size) :
            now_row, now_col = fires.popleft()
            for idx in range(4) :
                next_row, next_col = now_row + dR[idx], now_col + dC[idx]
                if not valid_range(next_row, next_col) :
                    continue
                if board[next_row][next_col] != "#" and board[next_row][next_col] != "*" :
                    board[next_row][next_col] = '*'
                    fires.append([next_row, next_col])
        # 이동!
        for _ in range(size) :
            now_row, now_col = que.popleft()
            for idx in range(4) :
                next_row, next_col = now_row + dR[idx], now_col + dC[idx]
                if not valid_range(next_row, next_col) :
                    return move_count
                if not visited[next_row][next_col] and board[next_row][next_col] != "#" and board[next_row][next_col] != "*" :
                    visited[next_row][next_col] = 1
                    que.append([next_row, next_col])
    return -1

T = int(input())
for test in range(T) :
    w, h = map(int, input().split())
    start = []
    fires = deque()
    board = [['.'] * w for _ in range(h)]
    for row in range(h) :
        tmp = list(input())
        for col in range(w) :
            if tmp[col] == "@" :
                start = [row, col]
            elif tmp[col] == "*" :
                fires.append([row, col])
            board[row][col] = tmp[col]
    answer = move(board, start, fires)
    if answer == -1 :
        print("IMPOSSIBLE")
    else :
        print(answer)


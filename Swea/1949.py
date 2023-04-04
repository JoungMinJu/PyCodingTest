dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

def valid_range(row, col) :
    return 0 <= row < N and 0 <= col < N

def dfs(row, col, cnt, is_construction, visited) :
    global answer
    success = 0
    for idx in range(4) :
        next_row, next_col = row + dR[idx], col + dC[idx]
        if not valid_range(next_row, next_col) or [next_row, next_col] in visited:
            continue
        if board[next_row][next_col] < board[row][col] :
            success = 1
            visited.append([next_row, next_col])
            dfs(next_row, next_col, cnt + 1, is_construction, visited)
            visited.pop()
        elif board[next_row][next_col] - board[row][col] + 1 <= K and not is_construction :
            success = 1
            tmp = board[next_row][next_col]
            visited.append([next_row, next_col])
            board[next_row][next_col] = board[row][col] - 1
            dfs(next_row, next_col, cnt + 1, 1, visited)
            visited.pop()
            board[next_row][next_col] = tmp
    if not success :
        answer = max(answer, cnt)
        return


test_size = int(input())
for test in range(1, test_size+1) :
    N, K  = map(int, input().split())
    max_number = -float('inf')
    board = []
    for row in range(N) :
         tmp = list(map(int, input().split()))
         max_number = max(max_number, max(tmp))
         board.append(tmp)
    max_pos = []
    for row in range(N) :
        for col in range(N) :
            if board[row][col] == max_number :
                max_pos.append([row, col])

    answer = -float('inf')
    for row, col in max_pos :
        dfs(row, col, 1, 0, [[row, col]])
    print("#{} {}".format(test, answer))
def check() :
    for col in range(N) : # 세로열을 하나씩 검증
        now_col = col
        for row in range(H) :
            if board[row][now_col] :
                now_col += 1
            elif now_col > 0 and board[row][now_col -1] : # 선이 왼쪽에 존재
                now_col -= 1
        if now_col != col :
            return False
    return True

def dfs(cnt, row, col):
    global ans
    if check() :
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt :
        return
    for i in range(row, H):
        # 가로선을 우선으로 탐색하므로
        if i == row:
            k = col # 행이 변경되기 전에는 가로선을 계속해서 탐색
        else:
            k = 0 # 행이 변경될 경우 가로선 처음부터 탐색
        for j in range(k, N - 1): # 세로선(열)
            if not board[i][j] and not board[i][j + 1]: # 가로선을 놨을 때 오른쪽에 -가 존재하지 않는 경우
                if j > 0 and board[i][j - 1]:
                    continue # 가로선을 놨을 때 왼쪽에 -가 존재할 경우 continue (--가 되면 안되기 때문)
                board[i][j] = True # 가로선 놓기
                dfs(cnt + 1, i, j + 2) # cnt 1 증가, 세로선 그대로, -- 이 되면 안되므로 가로선은 2증가
                board[i][j] = False # 가로선 없애기


N, M, H = map(int, input().split())
board = [[False] * N for _ in range(H)]
if M == 0 :
    print(0)
    exit(0)
for _ in range(M) :
    a, b = map(int, input().split())
    board[a-1][b-1] = True
ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)
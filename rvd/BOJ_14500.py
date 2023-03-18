valid_range = lambda row, col : 0 <= row < N and 0 <= col < M

# 상우하좌
dR = [-1, 0, 0, 1]
dC = [0, 1, -1, 0]
# ㅗ 이동 시키기 # ㅗ, ㅏ, ㅜ, ㅓ
one_move_idxes = [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]]

N, M = map(int, input().split())  # row col
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

answer = 0


# ㅗ,ㅏ,ㅓ,ㅜ 빼고 나머지
def dfs(row, col, dsum, cnt):
    global answer
    if cnt == 4:
        answer = max(answer, dsum)
        return
    for idx in range(4):
        next_row, next_col = row + dR[idx], col + dC[idx]
        if valid_range(next_row, next_col) and not visited[next_row][next_col]:
           visited[next_row][next_col] = True
           dfs(next_row, next_col, dsum + graph[next_row][next_col], cnt + 1)
           visited[next_row][next_col] = False

def exec(row, col) :
    global answer
    for idx in range(4) : # 상우하좌 0123
        tmp = graph[row][col]
        move_idx = one_move_idxes[idx]
        for midx in move_idx :
            next_row, next_col = row + dR[midx], col + dC[midx]
            if not valid_range(next_row, next_col) :
                tmp = 0
                break
            tmp += graph[next_row][next_col]
        answer = max(answer, tmp)

for row in range(N) :
    for col in range(M) :
        visited[row][col] = True
        dfs(row, col, graph[row], 1)
        visited[row][col] = False
        exec (row, col)

print(answer)
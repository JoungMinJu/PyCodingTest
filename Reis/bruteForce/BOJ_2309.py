def count(graph) :
    global answer
    for row in range(N) :
        tmp = 1
        before = graph[row][0]
        for col in range(1, N) :
            now = graph[row][col]
            if now == before :
                tmp += 1
            else :
                answer = max(answer, tmp)
                tmp = 1
                before = now
        answer = max(answer, tmp)
    for col in range(N) :
        tmp = 1
        before = graph[0][col]
        for row in range(1, N) :
            now = graph[row][col]
            if now == before :
                tmp += 1
            else :
                answer = max(answer, tmp)
                tmp = 1
                before = now
        answer = max(answer, tmp)

def dfs(now_row, now_col) :
    visited[now_row][now_col] = True
    color = graph[now_row][now_col]
    for idx in range(4) :
        next_row = now_row + dR[idx]
        next_col = now_col + dC[idx]
        if not valid_range(next_row, next_col) :
            continue
        if not visited[next_row][next_col] and graph[next_row][next_col] != color :
            graph[now_row][now_col] = graph[next_row][next_col]
            graph[next_row][next_col] = color
            count(graph)
            graph[next_row][next_col] = graph[now_row][now_col]
            graph[now_row][now_col] = color

valid_range = lambda row, col : 0 <= row < N and 0 <= col < N

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

N = int(input())
graph = [list(input()) for _ in range(N)]
answer = 0

visited = [[False] * N for _ in range(N)]
for row in range(N) :
    for col in range(N) :
        dfs(row, col)
print(answer)
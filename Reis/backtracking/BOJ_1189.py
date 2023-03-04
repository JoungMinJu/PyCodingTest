import sys
input = sys.stdin.readline

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

def dfs(row, col, count) :
    global end_row, end_col, K, answer
    if (row, col) == (end_row, end_col) :
        if count == K :
            answer += 1
        return
    for idx in range(4) :
        next_row = row + dR[idx]
        next_col = col + dC[idx]
        if next_row not in range(R) or next_col not in range(C) :
            continue
        if not visited[next_row][next_col] and graph[next_row][next_col] != 'T':
            visited[next_row][next_col] = True
            dfs(next_row, next_col, count+1)
            visited[next_row][next_col] = False


R, C, K = map(int, input().split())
graph = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

start_row, start_col = R-1, 0
end_row, end_col = 0, C-1

answer = 0

visited[start_row][start_col] = True
dfs(start_row, start_col, 1)
print(answer)

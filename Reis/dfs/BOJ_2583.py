import sys
sys.setrecursionlimit(100000) # 없으면 recursion error 발생

def dfs(row, col) :
    global cnt
    visited[row][col] = True
    for i in range(4) :
        next_row = row + dR[i]
        next_col = col + dC[i]

        if (0 <= next_row < M) and (0 <= next_col < N) and (not visited[next_row][next_col]) :
            cnt += 1
            dfs(next_row, next_col)


M, N, K = map(int, input().split(" "))
visited = [[False] * N for _ in range(M)]
# MxN

# 처리
for _ in range(K) :
    start_col, start_row, end_col, end_row = map(int, input().split())
    for row in range(start_row, end_row):
        for col in range(start_col, end_col) :
            visited[row][col] = True

dR = [-1, 0, 1, 0]
dC = [0, 1, 0, -1]
cnt = 1
area = 0
ans = []

for i in range(M):
    for j in range(N) :
        if not visited[i][j] :
            area += 1
            dfs(i, j)
            ans.append(cnt)
            cnt = 1

ans.sort()
print(area)
print(' '.join(map(str, ans)))
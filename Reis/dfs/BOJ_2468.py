import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

def dfs(row, col, heigth):
    visited[row][col] = True
    for idx in range(4):
        next_row = row + dR[idx]
        next_col = col + dC[idx]
        if next_row < 0 or next_row >= N or next_col < 0 or next_col >=N :
            continue
        if graph[next_row][next_col] > height and not visited[next_row][next_col] :
            dfs(next_row, next_col, heigth)

N = int(input()) # 2차원 배열의 행과 열의 개수
graph = []
max_num = -1

for i in range(N) :
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    max_num = max(max_num, max(tmp))

result = 0
visited = []

for height in range(max_num) :
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    for row in range(N):
        for col in range(N) :
            if graph[row][col] > height and not visited[row][col] :
                dfs(row, col, height)
                cnt += 1
    result = max(result, cnt)

print(result)

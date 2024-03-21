import sys
sys.setrecursionlimit(10**6)

def dfs(x, y) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    visited[x][y] = True
    for i in range(4) :
        ax = x + dx[i]
        ay = y + dy[i]
        if 0 <= ax < n and 0 <= ay < n and not visited[ax][ay] :
            if graph[ax][ay] == graph[x][y] :
                dfs(ax, ay)

if __name__ == "__main__" :
    n = int(input())
    graph = [list(input().rstrip()) for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]

    cnt = 0
    blind_cnt = 0

    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                dfs(i, j)
                cnt += 1
    for i in range(n) :
        for j in range(n) :
            if graph[i][j] == 'R':
                graph[i][j] = 'G'
    visited = [[False] * n for _ in range(n)]

    for i in range(n) :
        for j in range(n) :
            if not visited[i][j] :
                dfs(i, j)
                blind_cnt += 1
    print(cnt, blind_cnt)

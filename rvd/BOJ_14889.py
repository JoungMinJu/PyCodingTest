
def dfs(depth, idx) :
    global min_diff
    if depth == N /2 :
        power1, power2 = 0, 0
        for i in range(N) :
            for j in range(N) :
                if visited[i] and visited[j] :
                    power1 += board[i][j]
                elif not visited[i] and not visited[j] :
                    power2 += board[i][j]
        min_diff = min(min_diff, abs(power1-power2))
        return
    for i in range(idx, N) :
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [False for _ in range(N)]
min_diff = float('inf')

dfs(0, 0)
print(min_diff)
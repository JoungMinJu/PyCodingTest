R, C = map(int, input().split())
maps = []
for _ in range(R) :
    maps.append(list(input()))
ans = 0
alphas = set()
dR = [-1, 1, 0, 0]
dC = [0, 0, 1, -1]

def dfs(row, col, count) :
    global ans
    ans = max(ans, count)
    for idx in range(4):
        nR = row + dR[idx]
        nC = col + dC[idx]
        if 0 <= nR < R and 0 <= nC < C and not maps[nR][nC] in alphas :
            alphas.add(maps[nR][nC])
            dfs(nR, nC, count+1)
            alphas.pop()

alphas.add(maps[0][0])
dfs(0, 0, 1)
print(ans)
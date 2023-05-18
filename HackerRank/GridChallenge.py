def gridChallenge(grid, n) :
    for i in range(n) :
        grid[i] = sorted(grid[i])
    for i in range(n-1) :
        for j in range(n) :
            if grid[i][j] > grid[i+1][j]:
                return "NO"
    return "YES"


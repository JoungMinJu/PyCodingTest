import copy

INF = float('inf')

def  solve(x, y, d1, d2) :
    tmp = [[0] * (N+1) for _ in range(N+1)]
    tmp[x][y] = 5
    for i in range(1, d1 + 1):
        tmp[x + i][y - i] = 5
    for i in range(1, d2 + 1):
        tmp[x + i][y + i] = 5
    for i in range(1, d2 + 1):
        tmp[x + d1 + i][y - d1 + i] = 5
    for i in range(1, d1 + 1):
        tmp[x + d2 + i][y + d2 - i] = 5

    people = [0] * 5
    for r in range(1, x + d1):
        for c in range(1, y + 1):
            if tmp[r][c] == 5:
                break
            else:
                people[0] += maps[r][c]

    for r in range(1, x + d2 + 1):
        for c in range(N, y, -1):
            if tmp[r][c] == 5:
                break
            else:
                people[1] += maps[r][c]

    for r in range(x + d1, N + 1):
        for c in range(1, y - d1 + d2):
            if tmp[r][c] == 5:
                break
            else:
                people[2] += maps[r][c]

    for r in range(x + d2 + 1, N + 1):
        for c in range(N, y - d1 + d2 - 1, -1):
            if tmp[r][c] == 5:
                break
            else:
                people[3] += maps[r][c]

    people[4] = total - sum(people)
    return max(people) - min(people)



N = int(input())
maps = [[0] * (N+1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

total = 0
for row in range(1, N+1) :
    total += sum(maps[row])

answer = INF
for row in range(1, N+1) :
    for col in range(1, N+1) :
        for d1 in range(1, N+1) :
            for d2 in range(1, N+1) :
                if row + d1 + d2 > N or col - d1 < 1 or col + d2 > N :
                    continue
                answer = min(answer, solve(row, col, d1, d2))
print(answer)
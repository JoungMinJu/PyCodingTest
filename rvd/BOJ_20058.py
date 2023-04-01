import sys
from collections import deque

input = sys.stdin.readline

def devide_rotate(L):
    p = 2 ** L
    for i in range(0, (2 ** n) - 1, p):
        for j in range(0, (2 ** n) - 1, p):
            new = [maps[r][j:j + p] for r in range(i, i + p)]
            for k, col in enumerate(zip(*new[::-1])): #뭐지 천잰가
                maps[i + k][j:j + p] = col


def reduce_ice():
    new_map = [maps[i][:] for i in range(2 ** n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    for i in range(2 ** n):
        for j in range(2 ** n):
            if maps[i][j] > 0:
                count = 0
                for x, y in zip(dx, dy):
                    mx, my = i + x, j + y
                    if 0 <= mx < (2 ** n) and 0 <= my < (2 ** n):
                        if maps[mx][my] > 0:
                            count += 1
                if count < 3:
                    new_map[i][j] -= 1

    for i in range(2 ** n):
        maps[i] = new_map[i][:]


def bfs(row, col):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    count, total = 0, 0
    queue = deque([(row, col)])
    while queue:
        r, c = queue.popleft()
        for x, y in zip(dx, dy):
            mx, my = r + x, c + y
            if 0 <= mx < (2 ** n) and 0 <= my < (2 ** n) and not visited[mx][my] and maps[mx][my] != 0:
                queue.append((mx, my))
                visited[mx][my] = True
        count += 1
        total += maps[r][c]
    return count, total


n, q = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(2 ** n)]
Ls = list(map(int, input().split()))

for L in Ls:
    devide_rotate(L)
    reduce_ice()

count, total = 0, 0
visited = [[False] * (2 ** n) for _ in range(2 ** n)]
for i in range(2 ** n):
    for j in range(2 ** n):
        if maps[i][j] > 0 and not visited[i][j]:
            visited[i][j] = True
            dunguri_cnt, dunguri_sum = bfs(i, j)
            if dunguri_cnt > 1:
                count = max(count, dunguri_cnt)
            total += dunguri_sum
print(total, count, sep='\n')


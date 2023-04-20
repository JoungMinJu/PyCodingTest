import sys
input = sys.stdin.readline

h, w = map(int, input().split())

check = [[0 for i in range(w)] for j in range(h)]

mat = []
ans = [] # x, y, s

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def checks(y, x):
    for s in range(1, w):
        flag = True
        for i in range(4):
            ny = y + dy[i] * s
            nx = x + dx[i] * s
            if 0 <= nx < w and 0 <= ny < h and mat[ny][nx] == '*':
                pass
            else:
                # exit
                flag = False
                break
        if flag:
            ans.append([y + 1, x + 1, s])
            for i in range(4):
                ny = y + dy[i] * s
                nx = x + dx[i] * s
                check[ny][nx] = 0
            check[y][x] = 0
        else:
            break

for i in range(h):
    mat.append(input().strip())

for i in range(h):
    for j in range(w):
        if mat[i][j] == '*':
            check[i][j] = 1

for i in range(h):
    for j in range(w):
        if mat[i][j] == '*':
            checks(i, j)

total = 0
for i in range(h):
    for j in range(w):
        total += check[i][j]

if total == 0:
    print(len(ans))
    for ss in ans:
        print(*ss)
else:
    print(-1)
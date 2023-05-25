import sys

input = lambda: sys.stdin.readline().rstrip()

h, w = map(int, input().split())
check = [[0] * w for _ in range(h)]

mat = []
answer = []

dR = [1, -1, 0, 0]
dC = [0, 0, 1, -1]


def check(row, col):
    for s in range(1, w):
        flag = 1
        for i in range(4):
            next_row, next_col = row + dR[i] * s, col + dC[i] * s
            if 0 <= next_row < w and 0 <= next_col < h and mat[next_row][next_col] == '*' :
                pass
            else :
                flag = 0
                break
        if flag :
            answer.append([row+1, col+1, s]) # 사이즈 체크
            for idx in range(4) :
                next_row, next_col = row + dR[i] * s, col + dC[i] * s
                check[next_row][next_col] = 0
            check[row][col] = 0
        else :
            break

for row in range(h) :
    mat.append(input())

for row in range(h) :
    for col in range(w) :
        if mat[row][col] == '*' :
            check(row, col)
total = 0
for row in range(h) :
    for col in range(w) :
        total += check[row][col]

if total == 0 :
    for j in range(w) :
        total += check[row][col]
if total == 0 :
    print(len(answer))
    for ss in answer :
        print(*ss)
else :
    print(-1)
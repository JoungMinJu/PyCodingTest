import sys

input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
board = [[0] * (N+1)]
for row in range(N) :
    board.append([0] + list(map(int, input().split())))
csum = [[0] * (N+1) for _ in range(N+1)]
# 누적합 구하기
for row in range(1, N+1) :
    for col in range(1, N+1) :
        csum[row][col] = csum[row-1][col] + csum[row][col-1] - csum[row-1][col-1] + board[row][col]

for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().split())
    print(csum[x2][y2] - csum[x1-1][y2] - csum[x2][y1-1] + csum[x1-1][y1-1])

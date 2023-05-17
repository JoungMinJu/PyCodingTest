import sys

input = lambda: sys.stdin.readline().rstrip()

# 배열을 한사이즈 크게 만들어서 빼기 해도 문제 없도록 구성

N, M = map(int, input().split())
board = []
for row in range(N):
    board.append(list(map(int, input().split())))

dp = [[0] * (M+1) for _ in range(N+1)]
for row in range(1, N+1) :
    for col in range(1, M+1) :
        dp[row][col] = board[row-1][col-1] + dp[row][col-1] + dp[row-1][col] - dp[row-1][col-1]
k = int(input())
for _ in range(k) :
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])

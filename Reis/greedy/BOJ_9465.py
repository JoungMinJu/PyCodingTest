import sys

input = lambda : sys.stdin.readline().rstrip()

T = int(input())
for test in range(T) :
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * N for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]
    for col in range(1, N) :
        dp[0][col] = max(stickers[0][col] + dp[1][col-1], dp[0][col-1])
        dp[1][col] = max(stickers[1][col] + dp[0][col-1], dp[1][col-1])
    print(max(dp[0][N-1], dp[1][N-1]))
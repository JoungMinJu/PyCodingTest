import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

test_size = int(input())
for test in range(test_size) :
    N = int(input())
    dp = [list(map(int, input())) for _ in range(2)]
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]
    for col in range(2, N) :
        dp[0][col] += max(dp[1][col-1], dp[1][col-2])
        dp[1][col] += max(dp[0][col-1], dp[0][col-2])
    print(max(dp[0][N-1], dp[1][N-1]))
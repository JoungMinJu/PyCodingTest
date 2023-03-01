N = int(input())

dp = [[0] * (N+1) for _ in range(2)]

dp[0][1] = 0
dp[1][1] = 1

for digit in range(2, N+1) :
    dp[0][digit] = dp[0][digit-1] + dp[1][digit-1]
    dp[1][digit] = dp[0][digit-1]

answer = dp[0][N] + dp[1][N]
print(answer)

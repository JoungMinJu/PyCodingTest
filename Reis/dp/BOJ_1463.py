

N = int(input())
dp = [0] * (N+1)
for i in range(2, N+1) :
    answer = float('inf')
    if i % 2 == 0 :
        answer = min(answer, dp[i//2] +1)
    if i % 3 == 0 :
        answer = min(answer, dp[i//3] +1)
    answer =  min(answer, dp[i-1] + 1)
    dp[i] = answer
print(dp[N])
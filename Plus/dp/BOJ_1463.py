N = int(input())

dp = [0] * (N+1)

for num in range(N+1) :
    if num in (0,1) :
        answer = 0
    else:
        answer = dp[num-1] + 1
        if (num % 3 == 0) :
            answer = min(answer, dp[num//3] + 1)
        if (num % 2 == 0) :
            answer = min(answer, dp[num//2] + 1)
    dp[num] = answer

print(dp[N])
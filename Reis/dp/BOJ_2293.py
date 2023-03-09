import sys
input = sys.stdin.readline

N, K = map(int, input().split())
moneys = []
for _ in range(N) :
    moneys.append(int(input()))
moneys.sort()

dp = [[0 for _ in range(len(moneys))] for _ in range(K+1)]

# 초기화
for target in range(K+1) :
    dp[target][0] = 1 if target % (moneys[0]) == 0 else 0

for money_idx in range(1, len(moneys)):
    now_money = moneys[money_idx]
    for target in range(K+1) :
        if target < now_money :
            dp[target][money_idx] = dp[target][money_idx - 1]
        else :
            dp[target][money_idx] = dp[target][money_idx - 1] + dp[target-now_money][money_idx]

print(dp[K][N-1])
# 메모리 사용량 줄이는 코드
# 기존 코드 = 10000 * 10
# 이번 코드 = 1 * 10000

N, K = (map(int, input().split()))
coins = [0] + [int(input()) for _ in range(N)]
coins.sort()

dp = [0] * (K+1)  # target 금액 배열
# 동전의 가치에 따라서 초기 배열 설정
for i in range(coins[1], K+1, coins[1]) :
    dp[i] = 1
dp[0] = 1

for coin_idx in range(2, len(coins)) :
    # 현재 코인의 가치랑 같은 값부터 갱신 시작 -> 이전 것은 볼 필요 없음
    for target in range(coins[coin_idx], K+1) :
        dp[target] += dp[target-coins[coin_idx]]

print(dp[-1])
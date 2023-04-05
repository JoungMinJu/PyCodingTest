import sys
input = lambda :sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

N = int(input())
works = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)] # 0 1 2 3 4 5 6 7

for day in range(N-1, -1, -1) :
    if day + works[day][0] > N :
        # 그 날의 상담 못함
        dp[day] = dp[day+1]
    else :
        dp[day] = max(dp[day+1], works[day][1] + dp[day + works[day][0]])

print(dp[0])
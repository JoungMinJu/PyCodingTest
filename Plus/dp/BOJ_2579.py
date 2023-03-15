import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)
dp[1] = arr[1]
if N >= 2:
    dp[2] = arr[1] + arr[2]

for i in range(3, N+1) :
    dp[i] = max(arr[i] + dp[i-2], arr[i] + arr[i-1] + dp[i-3])
print(dp[N])
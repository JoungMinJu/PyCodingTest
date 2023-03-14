import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
dp = [0] * (N)
dp[0] = arr[0]
for now in range(1, N) :
    dp[now] = max(dp[now-1]+arr[now], arr[now])

print(max(dp))

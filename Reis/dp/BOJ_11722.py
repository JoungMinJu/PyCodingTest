import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))

dp = [1] * (N)

for now in range(1, N) :
    for before in range(now) :
        if arr[before] > arr[now]:
            dp[now] = max(dp[now], dp[before] + 1)
print(max(dp))
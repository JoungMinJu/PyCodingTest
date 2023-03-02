import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N) :
    arr.append(int(input()))
dp = [0] * (N + 1)
dp[0] = arr[0]
dp[1] = arr[0] + arr[1]
dp[2] = max (arr[2] + arr[0], arr[2] + arr[1], dp[1])

for i in range(3, N):
    dp[i] = max(arr[i] + dp[i-2], arr[i]  + arr[i-1] + dp[i-3], dp[i-1])
print(max(dp))

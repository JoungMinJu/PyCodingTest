import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
for start in range(N):
    for before in range(start) :
        if arr[before] < arr[start] :
            dp[start] = max(dp[start], dp[before] + 1)

print(max(dp))
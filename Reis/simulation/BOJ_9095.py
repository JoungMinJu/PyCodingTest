import sys

input = lambda : sys.stdin.readline().rstrip()

'''
정수 1 = 1가지 (1)
정수 2 = 2가지 (1+1, 2)
정수 3 = (1+1+1, 2+1, 1+2, 3) 4가지
정수 4 = (1+1+1, 2+1+1, 1+2+1, 3+1, 1+1+2, 2+2, 1+3) 7가지
'''

T = int(input())

def get(n) :
    if dp[n] :
        return dp[n]
    dp[n] = get(n-1) + get(n-2) + get(n-3)
    return dp[n]

dp = [0, 1, 2, 4]

for test in range(T) :
    N = int(input())
    if len(dp) <= N :
        dp = dp + [0] * (N-len(dp)+1)
    print(get(N))

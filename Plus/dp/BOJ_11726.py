import sys
sys.setrecursionlimit(10**6)

def solution(number) :
    if number in (1, 2) :
        return number
    if dp[number] > 0 :
        return dp[number]
    dp[number] = solution(number-1) + solution(number-2)
    return dp[number]

N = int(input())
dp = [0] * (N+1)

print(solution(N))
import sys
sys.setrecursionlimit(10**6)

N = int(input())
dp = [[0] * (N+1) for _ in range(10)]

for digit in range(1, N+1):
    for end_number in range(10):
        if digit == 1 :
            if end_number == 0 :
                answer = 0
            else :
                answer = 1
        else :
            if end_number == 0 :
                answer = dp[end_number+1][digit-1]
            elif end_number == 9:
                answer = dp[end_number-1][digit-1]
            else :
                answer = dp[end_number-1][digit-1] + dp[end_number+1][digit-1]
        dp[end_number][digit] = answer

sum = 0
for digit in range(0, 10) :
    sum += dp[digit][N]
print(sum % 1000000000)
import sys
sys.setrecursionlimit(10**6)

def solution(number) :
    if number <=  2:
        return number
    if number == 3:
        return 4
    if dp[number] > 0 :
        return dp[number];
    dp[number] = solution(number-1) + solution(number-2) + solution(number-3)
    return dp[number]


input = sys.stdin.readline
test_size = int(input().strip())

for test in range(test_size) :
    number = int(input().strip())
    dp = [0] * (number+1)
    print(solution(number))


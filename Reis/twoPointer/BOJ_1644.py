import sys
import math
input = lambda : sys.stdin.readline().rstrip()

#. 연속된 소수의 합
N = int(input())

A = [False, False] + (True) * (N-1)
prime_nums = []
for i in range(2, N+1) :
    if A[i] :
        prime_nums.append(i)
        for j in range(2*i, N+1, i) :
            A[j] = False

answer = start = end = 0
while end <= len(prime_nums) :
    tmp_sum = sum(prime_nums[start:end])
    if tmp_sum == N :
        answer += 1
        end += 1
    elif tmp_sum < N :
        end += 1
    else :
        start += 1
print(answer)

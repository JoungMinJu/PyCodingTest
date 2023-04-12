import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().strip()

def solve(start, end) :
    if start == end :
        return A[end] ** 2
    mid = (start+end) // 2
    result = max(solve(start, mid), solve(start+1, end))

    low = high = mid
    sum_value = A[mid]
    min_value = A[mid]

    while high - low < end - start :
        if low > start :
            low_value = A[low-1]
        else :
            low_value = -1
        if high < end :
            high_value = A[high+1]
        else :
            high_value = -1

        if low_value > high_value :
            sum_value += low_value
            min_value = min(min_value, low_value)
            low -= 1
        else :
            sum_value += high_value
            min_value = min(min_value, high_value)
            high += 1
        result = max(result, sum_value*min_value)
    return result

N = int(input())
A = list(map(int, input().split()))

print(solve(0, N-1))

'''
[모노톤 스택] - 오름차순
1. 높이 오름차순으로 스택에 담고
2. 더 작은 값이 나오면, pop하면서 계산하고 밑 변은 스택에 남은 값에 물려주기
3. 마지막 스택에 남은 값을 모두 pop 하여 계산
'''


import sys

input = lambda : sys.stdin.readline().rstrip()

N = int(input())
dice = list(map(int, input().split()))

'''
세 면이 다 드러남 => 각 위의 모서리 네 개 (4)
두 면이 다 드러남 => 가로 부분의 중앙 + 맨 밑 부분의 모서리 (n-1)*4 + (n-2)*4
한 면이 다 드러남 => 멘 밑면 중앙 + 중앙*4 + 최상단 가운데 (n-2)*(n-2) + (n-1)*(n-2)*4'''

'''
서로 맞은편 숫자 비교해서 min값 찾고 적절히 n1,n2,n3 하면 된다.
'''

answer = 0
nums = []
if N == 1 :
    print(sum(dice) - max(dice))
else :
    nums.append(min(dice[0], dice[5]))
    nums.append(min(dice[1], dice[4]))
    nums.append(min(dice[2], dice[3]))
    nums.sort()
    n3 = 4
    n2 = (N-2) * 4 + (N-1) * 4
    n1 = (N-2) ** 2 + (N-1) * (N-2) * 4

    print(n1 * nums[0] + n2 *(nums[0] + nums[1]) + n3 * sum(nums))
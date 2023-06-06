import sys

input = lambda: sys.stdin.readline().rstrip()

N = int(input())
board = list(map(int, input().split()))

'''
DP인데 메모리가 작아서 -> 슬라이딩윈도우 기법 활용하기
'''

dp1 = board
dp2 = board

for _ in range(N - 1):
    a, b, c = map(int, input().split())
    # append 아니고 갱신하기
    dp1 = [a + max(dp1[0], dp1[1]), b + max(dp1), c + max(dp1[1], dp1[2])]
    dp2 = [a + min(dp2[0], dp2[1]), b + min(dp2), c + min(dp2[1], dp2[2])]
print(max(dp1), min(dp2))

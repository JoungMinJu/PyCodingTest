import sys

input = lambda: sys.stdin.readline().rstrip()

def dfs(idx, s) :
    global answer
    if idx >= len(nums) :
        if s == S :
            answer += 1
        return
    dfs(idx +1, s + nums[idx])
    dfs(idx+1, s)

N, S = map(int, input().split())
nums = list(map(int, input().split()))

answer = 0
dfs(0, 0)
if S == 0:
    print(answer-1)
else :
    print(answer)
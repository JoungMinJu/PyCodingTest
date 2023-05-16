import sys
input = sys.stdin.readline

N, M= map(int, input().split())
nums = []
for _ in range(N):
    nums.append(int(input()))

nums.sort()

left, right = 0, 0
ans = sys.maxsize

while left < N and right < N:
    tmp = nums[right] - nums[left]
    if tmp == M :
        print(M)
        exit(0)
    if tmp < M :
        right += 1
    else :
        left += 1
        ans = min(ans, tmp)
print(ans)
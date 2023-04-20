import itertools

data = [str(i) for i in range(1, 10)]
nums = list(itertools.permutations(data, 3))

N = int(input())
for _ in range(N) :
    n, s, b = map(int, input().split())
    n = list(str(n))
    remove_cnt = 0
    for i in range(len(nums)) :
        strike = ball = 0
        i -= remove_cnt
        for j in range(3) :
            if nums[i][j] == n[j] :
                strike += 1
            elif n[j] in nums[i]:
                ball += 1
        if strike != s or ball != b :
            nums.remove(nums[i])
            remove_cnt += 1

print(len(num))
test_case = int(input())
for _ in range(test_case) :
    n = int(input())
    nums = list(map, input().split())
    value = 0
    max_value = 0
    for i in range(n-1, -1, -1) :
        if (nums[i] > max) :
            max = nums[i]
        else :
            value += max - nums[i]
    print(value)
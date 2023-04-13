import sys
input = lambda : sys.stdin.readline().strip()

def get_answer(height) :
    answer = 0
    for tree in trees :
        if tree > height :
            answer += (tree - height)
    return answer

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort()

min_val = 1
max_val = trees[-1]
while min_val <= max_val :
    mean_val = (min_val + max_val) // 2
    now_answer = get_answer(mean_val)
    if now_answer >= M :
        min_val = mean_val + 1
    else :
        max_val = mean_val - 1

print(max_val)
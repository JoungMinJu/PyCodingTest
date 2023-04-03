test_size = 10

directions = [-2, -1, 1, 2]

def get_answer(now) :
    now_height = heights[now]
    answer = float('inf')
    for direction in directions :
        other_height = heights[now+direction]
        if other_height >= now_height :
            return -1
        else :
            answer = min(answer, now_height - other_height)
    return answer

for test in range(1, test_size+1) :
    N = int(input())
    heights = list(map(int, input().split()))
    answer = 0
    for now in range(2, len(heights) - 2) :
        tmp_answer = get_answer(now)
        if tmp_answer != -1 :
            answer += tmp_answer
    print(f"#{test} {answer}")
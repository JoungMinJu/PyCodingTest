from collections import deque

def solution(priorities, location) :
    index_list = deque([i for i in range(len(priorities))])
    maximum = max(priorities)
    answer = 0
    while True :
        now_index = index_list.popleft() # 맨처음꺼
        if priorities[now_index] < maximum:
            index_list.append(now_index)
        else :
            answer += 1
            priorities[now_index] = 0
            maximum = max(priorities)
            if now_index == location :
                return answer

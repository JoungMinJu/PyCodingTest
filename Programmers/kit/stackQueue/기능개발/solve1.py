def solution(progresses, speeds):
    answer = []
    days_left = [(100-p) // s + (1 if (100-p) % s > 0 else 0) for p, s in zip(progresses, speeds)]

    stack = [] # (완료까지 남은 일 수, 배포된 기능의 수
    for day in days_left :
        if not stack or stack[-1][0] < day :
            stack.append((day, 1))
        else :
            stack[-1] = (stack[-1][0], stack[-1][1] + 1)
    answer = [count for day, count in stack]
    return answer
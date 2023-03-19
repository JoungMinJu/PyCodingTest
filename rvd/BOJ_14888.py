from collections import deque

N = int(input())
nums = list(map(int, input().split()))

operators = list(map(int, input().split()))
opers = ["+", "-", "*", "%"]

min_answer = float('inf')
max_answer = -float('inf')


def dfs(operators, current_operator):
    global min_answer, max_answer
    # 이미 다 썼으면 계산하기
    if check(operators):
        answer = get_answer(current_operator)
        min_answer = min(min_answer, answer)
        max_answer = max(max_answer, answer)
        return
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            dfs(operators, current_operator + opers[i])
            operators[i] += 1


def check(operators):
    return operators.count(0) == 4


def get_answer(current_operators):
    dq = deque(nums)
    for op in current_operators:
        first = dq.popleft()
        second = dq.popleft()
        tmp = calculate(first, second, op)
        dq.appendleft(tmp)
    return dq.popleft()


def calculate(first, second, op):
    if op == '+':
        return first + second
    if op == '-':
        return first - second
    if op == '*':
        return first * second
    if first < 0:
        first *= -1
        return (first // second) * -1
    elif second < 0:
        second *= -1
        return (first // second) * -1
    return first // second

dfs(operators, "")
print(max_answer)
print(min_answer)
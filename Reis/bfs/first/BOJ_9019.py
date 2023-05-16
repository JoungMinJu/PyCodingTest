import sys
from collections import deque

input = sys.stdin.readline

def bfs(number) :
    que = deque()
    visited = [False for _ in range(10001)]
    que.append([number, ""])
    visited[number] = True

    while que :
        size = len(que)
        for _ in range(size) :
            tmp = que.popleft()
            now_number, now_list = tmp[0], tmp[1]
            if now_number == B :
                return now_list
            nums_and_commands = list(calculator(now_number))
            for num_and_command in nums_and_commands :
                num, command = num_and_command[0], num_and_command[1]
                if not visited[num] :
                    que.append((num, now_list + command))
                    visited[now_number] = True


def calculator(number) :
    return [D(number), "D"], [S(number),"S"],[ L(number), "L"] , [R(number), "R"]

def D(number):
    return (2*number) % 10000

def S(number) :
    return (number-1) if number != 0 else 9999

def L(number) :
    size = get_size(number)
    ten = pow(10, size-1)
    return (int)((number % ten) * 10 + (number// ten))

def R(number) :
    size = get_size(number)
    ten = pow(10, size-1)
    return int((number % 10) * ten + (number // 10))

def get_size(number) :
    ans = 0
    while number:
        number //= 10
        ans += 1
    return ans

test_size = int(input())
for test in range(test_size) :
    A, B = map(int, input().split())
    answer = bfs(A)
    print(answer)

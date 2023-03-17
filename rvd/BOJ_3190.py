from collections import deque

in_range = lambda row, col: 0 <= row < N and 0 <= col < N


def move():
    global answer
    answer += 1
    now_row, now_col = snake_pos[len(snake_pos) - 1]
    next_row, next_col = now_row + dR[(idx % 4)], now_col + dC[(idx % 4)]
    if not in_range(next_row, next_col) or graph[next_row][next_col] == 1:
        return answer
    if graph[next_row][next_col] != 2:
        tail_row, tail_col = snake_pos.popleft()
        graph[tail_row][tail_col] = 0
    graph[next_row][next_col] = 1
    snake_pos.append((next_row, next_col))


def solve():
    global idx
    global answer
    for _ in range(L):
        num, dir = input().split()
        now_answer = answer
        for _ in range(now_answer, int(num)):
            answer += 1
            now_row, now_col = snake_pos[len(snake_pos) - 1]
            next_row, next_col = now_row + dR[(idx % 4)], now_col + dC[(idx % 4)]
            if not in_range(next_row, next_col) or graph[next_row][next_col] == 1:
                return answer
            if graph[next_row][next_col] != 2:
                tail_row, tail_col = snake_pos.popleft()
                graph[tail_row][tail_col] = 0
            graph[next_row][next_col] = 1
            snake_pos.append((next_row, next_col))
        if dir == 'L':
            idx -= 1
        else:
            idx += 1
    while True:
        answer += 1
        now_row, now_col = snake_pos[len(snake_pos) - 1]
        next_row, next_col = now_row + dR[(idx % 4)], now_col + dC[(idx % 4)]
        if not in_range(next_row, next_col) or graph[next_row][next_col] == 1:
            return answer
        if graph[next_row][next_col] != 2:
            tail_row, tail_col = snake_pos.popleft()
            graph[tail_row][tail_col] = 0
        graph[next_row][next_col] = 1
        snake_pos.append((next_row, next_col))
    return answer


N = int(input())
K = int(input())

# 동 남 서 북
dR = [0, 1, 0, -1]
dC = [1, 0, -1, 0]
idx = 0

graph = [[0] * N for _ in range(N)]  # 0 = 빈칸

for _ in range(K):
    row, col = map(int, input().split())
    graph[row - 1][col - 1] = 2  # 사과

L = int(input())
snake_pos = deque()
snake_pos.append((0, 0))  # 초기화
graph[0][0] = 1  # 뱀이 있음.
answer = 0  # 초
print(solve())

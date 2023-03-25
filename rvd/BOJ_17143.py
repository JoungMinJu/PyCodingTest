# 시초
from collections import deque

valid_range = lambda  row, col : 0 <= row < R and 0 <= col < C

dR = [-1, 1, 0, 0]# 위, 아래, 오른쪽, 왼쪽
dC = [0, 0, 1, -1]

R, C, M = map(int, input().split()) # 상어의 수 M

graph = [[[] for _ in range(C)] for _ in range(R)]
# 상어 = 위치 r,c / 속력 s / 이동 방향 d / 크기 z
sharks = []
for _ in range(M) :
    r, c, s, d, z = map(int, input().split())
    graph[r-1][c-1].extend([s,d-1,z])
    sharks.append([r-1, c-1, s, d-1, z])

sharks = deque(sorted(sharks, key = lambda x : x[4], reverse = True))

answer = 0

def get_direction(now_direction):
    if now_direction == 0  :
        return 1
    if now_direction == 1 :
        return 0
    if now_direction == 2 :
        return 3
    if now_direction == 3 :
        return 2


for pos in range(C) :
    # 낚시 한다.
    for row in range(R) :
        if len(graph[row][pos]) != 0 :
            answer += graph[row][pos][2]
            graph[row][pos].clear()
            break
    # 움직인다 -> 해당 위치에 상어가 없으면 그 값 지워버리기
    size = len(sharks)
    tmp_graph = [[[] for _ in range(C)] for _ in range(R)]
    for _ in range(size) :
        now_row, now_col, now_speed, now_direction, now_size = sharks.popleft()
        # 해당 위치에 상어가 없으면 지우기
        if len(graph[now_row][now_col]) == 0 :
            continue
        next_row, next_col = now_row, now_col
        for _ in range(now_speed) :
            next_row = now_row + dR[now_direction]
            next_col = now_col + dC[now_direction]
            # 벽에 부딪히면 방향 바꾸기
            if not valid_range(next_row, next_col) :
                now_direction = get_direction(now_direction)
                next_row = now_row + dR[now_direction]
                next_col = now_col + dC[now_direction]
            now_row, now_col = next_row, next_col
        # 내 원래 자리 비우고
        if len(tmp_graph[next_row][next_col]) == 0 :
            tmp_graph[next_row][next_col] = [now_speed, now_direction, now_size]
            sharks.append([next_row, next_col, now_speed, now_direction, now_size])
    for row in range(R) :
        for col in range(C) :
            graph[row][col] = tmp_graph[row][col]
print(answer)
from collections import deque

check_idx = [[-1, -2, 2], [1, 2, -2]]  # 체크할 톱니바퀴 idx, 비교할 내 톱니 idx, 비교할 상대의 톱니 idx

valid_range = lambda gear_idx: 0 <= gear_idx < 4


def solution(gears_idx, move):
    visited = [False] * 4
    que = deque()
    que.append((gears_idx, move))
    while que:
        now_gear_idx, now_move = que.popleft()
        visited[now_gear_idx] = True
        for i in range(2):
            check_gear_idx, my_gear, other_gear = check_idx[i]
            check_gear_idx += now_gear_idx
            if not valid_range(check_gear_idx):
                continue
            now_start_idx, other_start_idx = start_index[now_gear_idx], start_index[check_gear_idx]
            now_gear = now_start_idx + my_gear
            other_gear = other_start_idx + other_gear
            if not visited[check_gear_idx] and gears[now_gear_idx][now_gear % 8] != gears[check_gear_idx][other_gear % 8]:
                que.append((check_gear_idx, now_move * -1))
        if now_move == -1:
            start_index[now_gear_idx] += 1
        else:
            start_index[now_gear_idx] -= 1


gears = [list(map(int, list(input()))) for _ in range(4)]
start_index = [0] * 4
K = int(input())
moves = [list(map(int, input().split())) for _ in range(K)]

for move in moves:
    solution(move[0] - 1, move[1])

answer = 0
for i in range(4):
    answer += int(pow(2, (i+1) * gears[i][start_index[i]%8] - 1))
print(answer)

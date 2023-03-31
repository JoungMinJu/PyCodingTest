# 1. 벨트가 각 칸 위의 로봇과 함께 한 칸 회전
# 2. 가장 먼저! 벨트에 올라간 로봇부터 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동. (없으면 가만히)
    # -> 이동하려면 그 칸에 로봇에 없음 and 내구도 >=1
# 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 그 위치에 로봇 올림
# 4. 내구도가 0인 칸의 개수가 K개 이상이면 과정 종료. 아니면 1번으로 다시

## 보충 필요
from collections import deque

N, K = map(int, input().split())
strong = list(map(int, input().split()))
robots = deque([])
belt = deque([i for i in range(2*N)])

stage = 0
zero_count = 0
while True :
    stage += 1
    # 1번
    belt.appendleft(belt.pop())
    outside_index = [i % (2*N) for i in range(belt[N], belt[N]+N)]
    # 2번
    size = len(robots)
    for _ in range(size) :
        robot = robots.popleft()
        if robot in outside_index :
            continue
        next_idx = (robot + 1) % (2*N)
        if strong[next_idx] >= 1 and next_idx != belt[N] and not next_idx in robots:
            strong[next_idx] -= 1
            if strong[next_idx] == 0 :
                zero_count += 1
            robots.append(next_idx)
    # 3번
    if strong[belt[0]] != 0 :
        robots.append(belt[0])
        strong[belt[0]] -= 1
        if strong[belt[0]] == 0 :
            zero_count += 1
    if zero_count >= K :
        break
print(stage)

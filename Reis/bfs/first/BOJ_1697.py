from collections import deque
import sys

def get_next_step(now) :
    return {now - 1, now + 1, now * 2}

input = sys.stdin.readline

N, K = map(int, input().split())
que = deque()
visited = [False for _ in range(100001)]
que.append(N)
visited[N] = True
count = -1

while que :
    size = len(que)
    count += 1
    for _ in range(size) :
        now = que.popleft()
        if now == K :
            print(count)
            break
        step_list = get_next_step(now)
        for step in step_list :
            if step not in range(100001) :
                continue
            if not visited[step] :
                visited[step] = True
                que.append(step)

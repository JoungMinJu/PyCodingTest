from collections import deque
import sys
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
# 총 F층. 목적지 G층, 현재 S층, U 층 , D층

visited = [False for _ in range(F+1)]
que = deque()
que.append(S)
visited[S] = True
count = -1
move = [U, -D]
is_success = False

while que :
    count += 1
    size = len(que)
    for _ in range(size) :
        now = que.popleft()
        if now == G :
            print(count)
            is_success = True
            break
        for i in range(2) :
            next = now +  move[i]
            if next in range(1, F+1) and not visited[next]:
                visited[next] = True
                que.append(next)

if not is_success :
    print("use the stairs")
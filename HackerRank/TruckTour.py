from collections import deque

n = int(input().split())
rest = tank = 0
que = deque()
for ind in range(n) :
    petr, dist = [int(arg) for arg in input().strip().split()]
    tank += petr

    if dist <= tank :
        tank -= dist
    else :
        tank = 0
        res= ind + 1
    que.append((petr, dist))

print(res)


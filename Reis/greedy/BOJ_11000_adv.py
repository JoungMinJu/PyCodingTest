from heapq import heappush, heappop
N = int(input())
que = [list(map(int, input().split())) for _ in range(N)]

que.sort(key = lambda x : (x[0], x[1]))

room = []
heappush(room, que[0][1])

for i in range(1, N) :
    if que[i][0] < room[0] :
        heappush(room, que[i][1])
    else :
        heappop(room)
        heappush(room, que[i][1])
print(len(room))
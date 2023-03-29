from heapq import heappop, heappush

N = int(input())
times = [list(map(int, input().split())) for _ in range(N)]
times.sort(key = lambda x : (x[0], x[1]))

classes = []
for time in times :
    if len(classes) == 0 :
        heappush(classes, time[1])
    else :
        if classes[0] <= time[0] :
            heappop(classes)
        heappush(classes, time[1])

print(len(classes))
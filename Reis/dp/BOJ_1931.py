from heapq import heappop, heappush
N = int(input())

pq = []
for _ in range(N) :
    start, end = map(int, input().split())
    heappush(pq, (end, start))

now = 0
answer = 0
while pq :
    now_end, now_start = heappop(pq)
    if now_start >= now :
        now = now_end
        answer += 1
print(answer)
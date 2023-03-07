import sys
from heapq import heappop, heappush
input = sys.stdin.readline

dR = [1, -1, 0, 0]
dC = [0, 0, 1, -1]

def dijkstra() :
    heap = []
    heappush(heap, [0,0,0])
    while heap :
        cnt, row, col = heappop(heap)
        for idx in range(4) :
            next_row, next_col = row + dR[idx], col + dC[idx]
            if (next_row, next_col) == (N-1, M-1):
                print(cnt)
                return
            if 0 <= next_row < N and 0 <= next_col < M and not visited[next_row][next_col] :
                visited[next_row][next_col] = True
                if graph[next_row][next_col] == "1" :
                    heappush(heap, [cnt+1, next_row, next_col])
                else :
                    heappush(heap, [cnt, next_row, next_col])

M, N = map(int, input().split())
graph = [list(str(input())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]


dijkstra()
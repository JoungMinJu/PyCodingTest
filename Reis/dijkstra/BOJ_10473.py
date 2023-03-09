import sys
from heapq import heappush, heappop
import math

input = lambda : sys.stdin.readline().rstrip()

'''
[ 노드 번호 ] => 시작점 0, 대포들 1 ~ N, 도착점 N+1
[i][j] => 노드 i에서 j까지의 최소 시간
시작점부터 -> 다른 노드까지는 "달리기"만 가능하기 때문에 (거리/5)
나머지는 대포를 사용할 수 있으므로
1. (거리/5)
2. 거리가 50 초과일 때 대포 + 앞으로 달려가기 (2 + (거리 - 50)/5)
3. 거리가 50 미만일 때 대포 + 뒤로 달려가기 (2 + (50 - 거리)/5)
3. 거리가 50일 때 (2)
'''

def calculate_distance(src, dst) :
    return math.sqrt((src[0] - dst[0]) ** 2 + (src[1] - dst[1]) ** 2)

my_x, my_y = map(float, input().split())
target_x, target_y = map(float, input().split())
N = int(input())

points = [list(map(float, input().split())) for _ in range(N)]
points = [[my_x, my_y]] + points + [[target_x, target_y]]

time_matrix = [[0] * (N+2) for _ in range(N+2)]

# 걸리는 시간 행렬 다 구하기
for i in range(len(points)) :
    for j in range(i+1, len(points)):
        dist = calculate_distance(points[i], points[j])
        if i == 0 : # 시작점
            time_matrix[i][j] = dist / 5
        else :
            time_matrix[i][j] = dist / 5
            if dist > 50.0 :
                time_matrix[i][j] = min(time_matrix[i][j], 2 + (dist - 50)/5)
            elif dist == 50.0:
                time_matrix[i][j] = 2.0
            else :
                time_matrix[i][j] = min(time_matrix[i][j], 2 + (50-dist)/5)
        time_matrix[j][i] = time_matrix[i][j]

''' 
[다익스트라 진행]
1. 현재 최소거리인 노드를 잡고 -> 이동 가능한 모든 노드를 이동해보면서 거리를 갱신
'''

INT_MAX = int(10e9)
distance = [INT_MAX] * (N+2)
distance[0] = 0
heap = [[0,0]] # 시간, 시작점

while heap :
    time, next_node = heappop(heap)
    if distance[next_node] != time :
        continue # 중복 처리?
    if distance[i] > time + time_matrix[i][next_node] :
        distance[i] = time + time_matrix[i][next_node]
        heappush(heap, [distance[i], i])

print("%.6f"%(distance[N+1]))
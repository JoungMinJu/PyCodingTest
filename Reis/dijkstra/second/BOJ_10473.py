import math
import sys
from heapq import heappop, heappush

input = lambda : sys.stdin.readline.rstrip()

def calculate_distance(src, dest) :
    return math.sqrt((src[0] - dest[0]) ** 2 + (src[1] - dest[1])**2)

'''
1. 시작점, 대포 위치, 도착점을 노드로 잡고 걸리는 시간을 행렬로 구해줌
    : 시작점 -> 0 / 대포들 -> (1~N) / 도착점 -> N+1
    : [i][j] = 노드 i에서 j 까지의 최소 시간
    : 시작점부터 각 노드의 걸리는 시간을 구하는 경우, 달려가는 케이스밖에 없음
        => [0][j] = 시작점~도착점 거리 구하고 5(속력)로 나누기
    : 이외는 대포 사용 가능
        1. 달려가는 케이스 (거리/5)
        2. 거리가 50 초과일 때 대포 + 앞으로 달려가기 (2 + (거리 - 50) / 5)
        3. 거리가 50 미만일 때 대포 + 뒤로 달려가기 (2 + (50 - 거리) / 5)
        4. 거리가 50일 때
2. 시작점을 0으로 두고 다익스트라 활용
    : 현재 최소 거리인 노드를 잡고
    : 이동 가능한 모든 노드를 이동해 보면서 거리를 갱신하는 경우 거리 갱신 및 최소 힙에 거리 저장
3. N+1 노드까지의 최소 거리를 출력
'''

my_x, my_y = map(float, input().split())
target_x, target_y = map(float, input().split())
N = int(input())

points = []
points.append([my_x, my_y])
points += [list(map(float, input().split())) for _ in range(N)]
points.append([target_x, target_y])

time_matrix = [[0] * (N+2) for _ in range(N+2)]

# 최소 시간 구해서 time_matrix에 넣어놓기
for i in range(len(points)) :
    for j in range(i+1, len(points)):
        if i == 0 : # 시작점
            time_matrix[i][j] = calculate_distance(points[i], points[j]) / 5
        else :
            distance = calculate_distance(points[i], points[j])
            time_matrix[i][j] = distance / 5
            if distance > 50.0 :
                time_matrix[i][j] = min(time_matrix[i][j], 2 + (distance - 50) / 5)
            elif distance == 50.0 :
                time_matrix[i][j] = 2.0
            else :
                time_matrix[i][j] = min(time_matrix[i][j], 2 + (50 - distance) / 5)
            time_matrix[j][i] = time_matrix[i][j]

INT_MAX = int(10e9)
distance = [INT_MAX] * (N+2)
distance[0] = 0
heap = [[0, 0]]

while heap :
    time, next_node = heappop(heap)
    if distance[next_node] != time :
        continue
    for i in range(len(points)) :
        if next_node == i :
            continue
        if distance[i] > time + time_matrix[i][next_node] :
            distance[i] = time + time_matrix[i][next_node]
            heappush(heap, [distance[i], i])
print("%.6f"%(distance[N+1]))

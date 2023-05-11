'''
시작 정점에서 출발하여 정점을 하나씩 선택하며 신장트리 집합을 확장해나가는 방법
그리디 알고리즘의 일종
[작동순서]
1. 임의의 시작 장점을 하나 정한다. 시작 정점만 포함된 신장 트리 집한을 만든다
2. N개의 정점이 모두 선택될 때까지
    - 신장 트리 집합에 포함된 정점에 인접했으며 아직 방문하지 않은 정점 중 최소 비용의 간선이 존재하는 정점을 선택한다
    - 선택한 정점은 신장 트리 집합에 포함시킨다.
'''

'''
인접 행렬을 이용한 코드
'''

from math import inf


def prim(start):
    global N, adj_mat
    visited_set = set()
    visited_set.add(start)
    distance = 0
    # N-1개의 간선을 선택할 때까지 반복한다
    for _ in range(N - 1):
       min_dist, next_node = inf, -1
       # 현재까지 방문한모든 정점에 대하여
       for node in visited_set :
           for j in range(1, N + 1):
               if j not in visited_set and 0 < adj_mat[node][j] < min_dist:
                   min_dist = adj_mat[node][j]
                   next_node = j
       distance += min_dist
       visited_set.add(next_node)
    return distance

# N = 정점의 개수
# M = 간선의 개수
# adj_mat =  그래프의 인접 행렬
N, M = map(int, input().split())
adj_mat = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M) :
    x, y, value = map(int, input().split())
    adj_mat[x][y] = value
    adj_mat[y][x] = value

print(prim(1))
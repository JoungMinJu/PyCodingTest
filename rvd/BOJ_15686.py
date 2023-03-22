from copy import deepcopy
from collections import deque

dR = [0, 0, 1, -1]
dC = [1, -1, 0, 0]

valid_range = lambda row, col : 0 <= row < N and 0 <= col < N

def update(now_chickens):
    global answer
    # 현재 치킨집들 리스트 기반으로 board 만든다.
    board = deepcopy(graph)
    for chicken in chickens:
        if not chicken in now_chickens:
            board[chicken[0]][chicken[1]] = 0
    # 각 house에 대한 거리 계산
    now_dist = 0
    for house in houses:
        now_dist += get_dist( house, now_chickens)
    answer = min(now_dist, answer)


def get_dist(house, now_chickens):
    dist = float('inf')
    for chicken in now_chickens :
        tmp = abs(chicken[0] - house[0]) + abs(chicken[1] - house[1])
        dist = min(dist, tmp)
    return dist



def dfs(idx, now_chicken):
    if len(now_chicken) == M:
        update(now_chicken)
        return
    if idx >= len(chickens) :
        return
    now_chicken.append(chickens[idx])
    dfs(idx + 1, now_chicken)
    now_chicken.pop()
    dfs(idx + 1, now_chicken)


N, M = map(int, input().split())

houses = []
chickens = []
graph = []

answer = float('inf')

for row in range(N):
    tmp = list(map(int, input().split()))
    for col in range(N):
        if tmp[col] == 1 :
            houses.append([row, col])
        elif tmp[col] == 2 :
            chickens.append([row, col])
    graph.append(tmp)

dfs(0, deque())
print(answer)
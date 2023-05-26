import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

bridge = deque([0,0])
N, W, L = map(int, input().split()) # 다리를 건너는 트럭의 수 / 다리의 길이 / 다리의 최대 하중
bridge = deque([0]*W)
trucks = deque(list(map(int, input().split())))

now_weight = 0
answer = 0
while trucks :
    answer += 1
    # 이동
    now_weight -= bridge.popleft()
    # 들어갈 수 있는지 확인
    if now_weight + trucks[0] <= L :
        now_weight += trucks[0]
        bridge.append(trucks.popleft())
    else :
        bridge.append(0)
print(answer+W)
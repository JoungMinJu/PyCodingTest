import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input()) # 센서의 개수
K = int(input()) # 집중국의 개수
sensor_pos = list(map(int, input().split()))

answer = 0
if N > K : # 센서가 집중국의 개수보다 많으면
    dist = []
    for i in range(1, N) :
        dist.append(sensor_pos[i] - sensor_pos[i-1])
    dist.sort(reverse=True)
    for _ in range(K-1) :
        dist.pop(0)
    answer = sum(dist)
print(answer)
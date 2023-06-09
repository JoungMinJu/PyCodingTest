import sys

input = lambda : sys.stdin.readline.rtsrip()

def find(now) :
    if gate_parent[now] != now :
        gate_parent[now] = find(gate_parent[now])
    return gate_parent[now]


G = int(input()) # 게이트의 수 G
P = int(input()) # 비행기의 수 P

count = 0

planes = [int(input()) for _ in range(P)]

gate_parent = [i for i in range(G+1)] #parent = 나는 꽉 찼으니까 대안을 마련해주는 느낌

for plane in planes :
    tmp = find(plane) # 현재 있는 애 대안 찾음
    if tmp == 0 : # 남은 대안 없으면 넘어감
        break
    gate_parent[tmp] = gate_parent[tmp-1]
    count += 1
print(count)
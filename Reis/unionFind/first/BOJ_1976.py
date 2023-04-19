import sys
input = sys.stdin.readline

def find(node) :
    if parents[node] == node :
        return node
    p = find(parents[node])
    parents[node] = p
    return p

def union(start, end) :
    start_p = find(start)
    end_p = find(end)
    if start_p != end_p :
        if start_p < end_p :
            parents[end_p] = start_p
        else :
            parents[start_p] = end_p

N = int(input())
M = int(input())
parents = [i for i in range(N)]

for start in range(N) :
    link = list(map(int, input().split()))
    for end in range(N) :
        if link[end] == 1:
            union(start, end)

parents = [-1] + parents

path = list(map(int, input().split())) # 경로 입력 받음
start = parents[path[0]] # 시작점의 부모부터 시작
flag = True
for i in range(1, M) :
    if parents[path[i]] != start :
        print("NO")
        flag = False
        break
if flag :
    print("YES")

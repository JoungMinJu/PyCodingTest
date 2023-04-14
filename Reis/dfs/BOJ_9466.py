# "팀원수" 제한X
# 프로젝트를 함께하고 싶은 학생 선택하기 (단 한 명만 선택 가능)
# 자기 자신 선택도 가능
import sys
sys.setrecursionlimit(10**6)
input = lambda : sys.stdin.readline().strip()

def dfs(x):
    global count
    visited[x] = 1
    cycle.append(x)
    if visited[arr[x]] : # 내 다음 애가 이미 방문한 놈인데
        if arr[x] in cycle : # 사이클 안에 있으면
            count -= len(cycle[cycle.index(arr[x]):])
        return
    else :
        dfs(arr[x])



test_size = int(input())
for test in range(test_size) :
    N = int(input())
    arr = [0]
    arr.extend(list(map(int, input().split())))
    visited = [0] * (N+1)
    count = N
    for i in range(1, N+1) :
        if not visited[i] :
            cycle = []
            dfs(i)
    print(count)
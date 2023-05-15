import sys

input = lambda : sys.stdin.readline()

visited = []
link = []

def dfs(start) :
    visited[start] = 1
    if not visited[link[start]] :
        dfs(link[start])

T = int(input())
for test in range(T) :
    N = int(input())
    arr = list(map(int, input().split()))
    visited = [0] * N
    link = [-1] * N
    for i in range(N) :
        link[i] = arr[i]-1
    count = 0
    for i in range(N) :
        if not visited[i] :
            dfs(i)
            count += 1
    print(count)

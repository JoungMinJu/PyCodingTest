import sys

input = lambda : sys.stdin.readline().rstrip()

def solve(lst) :
    global answer
    if len(lst) == N :
        total = 0
        for i in range(N-1) :
            total += abs(lst[i] - lst[i+1])
        answer = max(answer, total)
        return
    for i in range(N) :
        if not visited[i] :
            visited[i] = 1
            lst.append(in_list[i])
            solve(lst)
            lst.pop()
            visited[i] = 0

N = int(input())
in_list = list(map(int, input().split()))
visited = [0] * N

answer = 0



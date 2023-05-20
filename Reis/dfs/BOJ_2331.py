import sys

input = lambda : sys.stdin.readline().rstrip()

def multiple(N, M):
    N = str(N)
    res = 0
    for i in N :
        res += pow(int(i), M)
    return res

def dfs(N, M, iteration, check) :
    if check[N] != 0 : # 이미 한 번 있으면
        return check[N] -1
    check[N] = iteration
    next = multiple(N, M)
    iteration += 1
    return dfs(next, M, iteration, check)

N, M = map(int, input().split())
check = [0] * 236197 # 최대 값
iteration = 1

print(dfs(N, M, iteration, check))
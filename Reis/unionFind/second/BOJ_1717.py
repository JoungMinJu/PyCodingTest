import sys
sys.setrecursionlimit(10**6)

input = lambda : sys.stdin.readline().rstrip()

def union(a, b) :
    p_a = find(a)
    p_b = find(b)
    if p_a == p_b :
        return
    if p_a <= p_b :
        parents[p_b] = p_a
    else :
        parents[p_a] = p_b

def find(a) :
    if parents[a] != a :
        parents[a] = find(parents[a])
    return parents[a]

N, M = map(int, input().split())
parents = [i for i in range(N+1)]
for _ in range(M) :
    number, a, b = map(int, input().split())
    if number == 0 :
        union(a, b)
    elif number == 1:
        p_a = find(a)
        p_b = find(b)
        if p_a == p_b :
            print("yes")
        else :
            print("no")

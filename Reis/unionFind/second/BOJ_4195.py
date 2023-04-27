import sys
input = lambda : sys.stdin.readline().rstrip()

def find(X) :
    if X == parent[X] :
        return X
    else :
        parent[X] = find(parent[X])
        return parent[X]

def union(X, Y) :
    root_X = find(X)
    root_Y = find(Y)
    if root_X != root_Y :
        parent[root_Y] = root_X
        number[root_X] += number[root_Y]

test_case = int(input())
for test in range(test_case) :
    parent = dict()
    number = dict()
    F = int(input())
    for _ in range(F) :
        X, Y = input().split()
        if X not in parent :
            parent[X] = X
            number[X] = 1
        if Y not in parent :
            parent[Y] = Y
            number[Y] = 1
        union(X, Y)
        print(number[find(X)])

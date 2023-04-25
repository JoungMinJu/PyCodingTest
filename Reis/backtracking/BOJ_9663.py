N = int(input())

ans = 0
row = [0] * N

def is_valid(x) :
    for i in range(x) :
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i) :
            return False
    return True

def n_queens(x):
    global ans
    if x == N:
        ans += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if is_valid(x):
                n_queens(x + 1)

n_queens(0)
print(ans)

import sys

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

mtr = [input() for _ in range(N)]
cnt = []

for a in range(N-7) :
    for b in range(M-7) :
        w_index = 0
        b_index = 0
        for i in range(a, a+8) :
            for j in range(b, b+8) :
                if (i+j) % 2 == 0 :
                    if mtr[i][j] != "W" :
                        w_index += 1
                    else :
                        b_index += 1
                else :
                    if mtr[i][j] != 'W' :
                        b_index += 1
                    else :
                        w_index += 1
        cnt.append(w_index)
        cnt.append(b_index)
print(min(cnt))
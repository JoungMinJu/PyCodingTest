import sys
from collections import deque

input = lambda : sys.stdin.readline().rstrip()

N, K = input().split()
size = len(N)
K = int(K)

def solve() :
    answer = 0
    visited = list()

    que = deque([(N, 0)])
    while que :
        now_str, cnt = que.popleft()
        if cnt == K :
            answer = max(answer, int(now_str))
            continue
        for one in range(size - 1):
            for two in range(one+1, size) :
                if one == 0 and now_str[two] == "0" :
                    continue
                tmp = now_str[0:one] + now_str[two] + now_str[one+1:two] +now_str[one] +  now_str[two+1:]
                if (tmp, cnt+1) not in visited :
                    que.append((tmp, cnt+1))
                    visited.append((tmp, cnt+1))
    print(answer if answer > 0 else -1)

solve()
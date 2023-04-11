import sys
from collections import defaultdict
input = lambda : sys.stdin.readline().strip()

N, K = map(int, input().split())
use = list(map(int, input().split()))
plugs = []
result = 0
for i in range(K) :
    if use[i] in plugs :
        continue
    if len(plugs) != N :
        plugs.append(use[i])
        continue
    # 가장 멀리 있는 플러그의 인덱스
    far_one = 0
    tmp = 0
    for plug in plugs :
        if plug not in use[i:] :
            tmp = plug
            break
        elif use[i:].index(plug) > far_one :
            far_one = use[i:].index(plug)
            tmp = plug
    plugs[plugs.index(tmp)] = use[i]
    result += 1

print(result)
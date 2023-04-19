import sys

input = lambda : sys.stdin.readline().rstrip()

# 지구 E, 태양 S, 달 M
# 1년이 지날때마다 세 수는 모두 1씩 증가, 어떤 수가 범위를 넘어가는 경우에는 1이 됨.
E, S, M = map(int, input().split())
now_E = now_S = now_M = cnt =1
days = 1
while True:
    if (now_E == E and now_S == S and now_M == M) :
        break
    now_E += 1
    now_S += 1
    now_M += 1
    cnt += 1
    if now_E >= 16 :
        now_E -= 15
    if now_S >= 29 :
        now_S -= 28
    if now_M >= 20 :
        now_M -= 19
print(cnt)
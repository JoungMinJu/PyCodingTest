import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split()) # 접시 수, 가짓 수, 연속 접시 수, 쿠폰 번호
lst = []
for _ in range(N) :
    lst.append(int(input()))

lst = lst + lst[:K-1]
answer = -1

for start in range(N):
    now = lst[start:start+K]
    now.append(C)
    now = set(now)
    if answer < len(now) :
        answer = len(now)


print(answer)


import sys; input = sys.stdin.readline

# 0 입력
N, K, Q, M = map(int, input().split())
sleep = set(map(int, input().split()))
students = set(map(int, input().split()))
attend = [False for _ in range(N + 3)]

# 1 출석 체크
for s in (students - sleep):
    for i in range(s, N + 3, s):
        if i not in sleep:
            attend[i] = True
# 2 미출석자 누적합 구하기
memo = [0 for _ in range(N + 3)]
for i in range(3, N + 3):
    if not attend[i]:
        memo[i] = memo[i - 1] + 1
    else:
        memo[i] = memo[i - 1]

# 3 출력
answer = ''
for _ in range(M):
    s, e = map(int, input().split())
    ans = memo[e] - memo[s - 1]
    answer += '{}\n'.format(ans)
print(answer)
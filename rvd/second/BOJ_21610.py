from collections import deque

dR = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dC = [0, -1, -1, 0, 1, 1, 1, 0, -1]

N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

# 구름 생성
cloud = deque()
cloud.append([N-1, 0])
cloud.append([N-1,1])
cloud.append([N-2, 0])
cloud.append([N-2, 1])


for _ in range(M) :
    visited = [[0] * N for _ in range(N)]
    d, s = map(int, input().split())
    size = len(cloud)
    for _ in range(size) :
        now_row, now_col = cloud.popleft()
        next_row = (now_row + dR[d]*s) % N
        next_col = (now_col + dC[d] * s) % N
        cloud.append([next_row, next_col])
    size = len(cloud)
    for idx in range(size) :
        now_row, now_col = cloud[idx]
        A[now_row][now_col] += 1
    for idx in range(size) :
        now_row, now_col = cloud.popleft()
        visited[now_row][now_col] = 1
        cnt = 0
        for d in [2, 4, 6, 8] :
            next_row, next_col = now_row + dR[d], now_col + dC[d]
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N :
                continue
            if A[next_row][next_col] :
                cnt +=1
        A[now_row][now_col] += cnt
    # 전체 돌며서 저장된 물의 양 2 이상인 애들 조사(구름생김) + 하면서 -2도 해줌
    for row in range(N) :
        for col in range(N) :
            if A[row][col] >= 2 :
                if not visited[row][col] : # 현재 클라우드에 있는게 아니면
                    A[row][col] = max(0, A[row][col] - 2)
                    cloud.append([row, col])


answer = 0
for row in range(N) :
    answer += sum(A[row])
print(answer)
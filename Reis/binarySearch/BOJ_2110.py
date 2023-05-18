import sys

input = lambda: sys.stdin.readline().rstrip()

N, C = map(int, input().split())  # 집의 개수, 공유기의 개수

arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

end = arr[-1] - arr[0]
start = 1
answer = 0

while start <= end :
    mid = (start + end) // 2
    count = 1
    current_router = arr[0]
    tmp = float('inf')

    for i in range(1, N) :
        if current_router + mid <= arr[i] :
            tmp = min(arr[i] - current_router, tmp)
            count += 1
            current_router = arr[i]
    if count < C : # 공유기 설치를 더 해야함
        end = mid -1
    else :
        start = mid +1
        answer = max(answer, tmp)
print(answer)

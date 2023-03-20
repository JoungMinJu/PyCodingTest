N, L = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def find(arr):
    slope = [False]*N
    for i in range(1, N) :
        if abs(arr[i] - arr[i-1]) > 1 :
            return False
        if arr[i] < arr[i-1] : # 내림차순
            for j in range(L) :
                if i + j >= N or arr[i] != arr[i+j] or slope[i+j]  :
                    return False
            for j in range(L) :
                slope[i+j] = True
        if arr[i] > arr[i-1] : # 오름차순
            for j in range(L) :
                if i - j - 1< 0 or arr[i-1] != arr[i-j-1] or slope[i-j-1]:
                    return False
            for j in range(L) :
                slope[i-j-1] = True
    return True

answer = 0
for row in range(N) :
    if find(arr[row]) :
        answer += 1

for col in range(N) :
    tmp_arr = []
    for row in range(N):
        tmp_arr.append(arr[row][col])
    if find(tmp_arr) :
        answer += 1

print(answer)
def dfs(depth, sum):
    global answer
    if depth == N:
        if sum == S:
            answer += 1
        return
    else :
        dfs(depth + 1, sum)
        dfs(depth + 1, sum + arr[depth])

N, S = map(int, input().split())  # 정수의 개수, 정수 S
arr = list(map(int, input().split()))

answer = 0
dfs(0, 0)

if S == 0:
    print(answer - 1)  # 공집합은 조건에 포함되지 않음
else:
    print(answer)

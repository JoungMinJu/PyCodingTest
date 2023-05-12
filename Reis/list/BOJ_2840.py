import sys

input = lambda : sys.stdin.readline()

N, K = map(int, input().split()) # 바퀴 칸의 수, 바퀴 돌리는 횟수


def solution() :
    numbers = ["?"] * N
    idx = 0
    for _ in range(K) :
        S, C = input().split()
        idx = (idx + int(S)) % N
        if numbers[idx] == "?" :
            numbers[idx] = C
        elif numbers[idx] != C :
            return "!"
    answer = ""
    char_set = set()
    for _ in range(N) :
        answer += numbers[idx]
        if numbers[idx] != "?" :
            if numbers[idx] in char_set :
                return "!"
            else :
                char_set.add(numbers[idx])
        idx = idx -1
        if idx < 0 :
            idx = N-1
    return answer

print(solution())
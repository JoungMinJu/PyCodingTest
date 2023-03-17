import math

N = int(input())
rooms = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for room in rooms :
    if room <= B :
        answer += 1
    else :
        answer += 1
        room -= B
        answer += math.ceil(room/C)

print(answer)
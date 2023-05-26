import sys

input = lambda: sys.stdin.readline().rstrip()
n, atk = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(N)]
left, right, answer = 0, sys.maxsize, 0


def binary_search(atk, hp, maxHP):
    for t, a, h in rooms:
        if t == 1:
            if h % atk == 0:
                hp = hp - ((h // atk - 1) * a)
            else:
                hp = hp - (h // atk * a)
        else :
            hp = min(maxHP, hp+h)
            atk += a
        if hp <= 0 :
            return False
    return True

while left <= right :
    mid = (left + right) // 2
    if binary_search(atk, mid, mid) :
        right = mid -1
        answer = mid
    else :
        left = mid + 1

print(answer)
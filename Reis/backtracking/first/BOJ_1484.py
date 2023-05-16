import sys
input = sys.stdin.readline

def calc(x, y) :
    return x**2 - y**2

G = int(input())
left, right = 1, 1
not_answer = True

while left + right <= G : # 경계 조건
    if calc(left, right) == G :
        print(left)
        left += 1
        not_answer = False
    elif calc(left, right) > G :
        right += 1
    elif calc(left, right) < G :
        left += 1

if not_answer :
    print(-1)
import sys

input = lambda: sys.stdin.readline().rstrip()

N, atk = map(int, input())
rooms = [list(map(int, input().split())) for _ in range(N)]  # t, a, h

'''
용사가 n번 때려서 몬스터가 죽는다면
그동안 몬스터에게 n-1 번의 데미지를 입는다.
'''

maxHP, curHP, damage = 0, 0, 0

for t, a, h in rooms:
    if t == 1:  # 몬스터
        tmp = h % atk
        if tmp == 0:
            damage = -(a * (h // atk - 1))
        else :
            damage = -(a*(h//atk))
    else : # 포션
        atk += a
        damage = h
    curHP += damage
    if curHP > 0 : #curHP > 0이라는 것은 maxHP보다 더 많이 ! 있다는 것을 의미
        curHP = 0
    maxHP = max(maxHP, abs(curHP))
print(maxHP+1)


import sys

input = lambda: sys.stdin.readline().rstrip()


def calc(a, b):
    return a ** 2 - b ** 2


'''
G = (성원이의 현재 몸무게)^2 - (성원이 기억 몸무게)^2
'''
G = int(input())  # 100,000 이하의 자연수
a, b = 1, 1
not_answer = True
while a + b <= G :
    if calc(a,b)== G :
        print(a)
        not_answer = False
    elif calc(a,b) > G :
        b += 1
    else :
        a+= 1
if not_answer :
    print(-1)
'''
1. 첫 번째 숫자를 -1 => 맨 뒤로 보냄
2. 다음엔 -2 => 맨 뒤로 보내고
...
(+) 0보다 작아지면 0으로 유지되고 프로그램 종료됨. 이때의 8자리의 숫자 값이 암호가 된다.
'''

def password(lst) :
    while 1 :
        for i in range(1, 6) :
            num = lst.pop(0)
            lst.append(num-i)

            if lst[-1] <= 0 :
                lst[-1] = 0
                return lst

for test in range(10):
    tc = int(input())
    numbers = list(map(int, input().split()))

    result = password(numbers)
    print(f"#{tc} {result}")
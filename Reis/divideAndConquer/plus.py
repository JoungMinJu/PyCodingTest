'''
분할정복으로 자연수 제곱
-> C^n을 C^(n/2) 두 개로 "분할"하고 "서로 곱함"

[방법 1 = 재귀]
1. C^n을 C^(N/2) 두 개로 분할 후 서로 곱함
2. n이 홀수였다면 추가로 C를 곱하고 return
3. n == 0 인 경우 1을 return

[방법 2 = 반복문]
1. base = 1, tmp = C로 시작
2. n > 0 까지 반복
3. n이 홀수라면 base에 tmp 곱함
4. tmp는 모든 반복마다 제곱
5. n은 모든 반복마다 2로 나눔
'''

def pow(a, b) : # a^b
    if b == 0 :
        return 1
    n = pow(a, b//2)
    tmp = n*n
    if b % 2 == 0 :
        return tmp
    return a * tmp
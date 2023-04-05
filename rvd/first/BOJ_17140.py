# 이차원 배열과 연산
import sys


# 연산함수
# A : NxN 배열, L : 행의 길이 (칼럼 개수)
def operation(A, L):
    for idx, row in enumerate(A):
        temp = []
        for n in set(row):  # 행의 중복을 제거한 후
            if n:  # 0이 아닌 숫자면
                temp.append((n, row.count(n)))  # 해당 숫자에 대한 값을 세어줌
        temp = sorted(temp, key=lambda x: (x[1], x[0]))  # 개수, 숫자 순서로 정렬
        templen = len(temp)
        if templen > 50: templen = 50  # 숫자의 개수는 100을 넘어가면 안됨
        L = max(L, templen * 2)  # 행의 길이를 최대로 바꿔줌
        A[idx] = []  # A의 idx행 초기화
        for i in range(templen):  # A의 idx행 재구성
            A[idx].append(temp[i][0])
            A[idx].append(temp[i][1])

    # 최대 길이만큼 0 채우기
    for idx, row in enumerate(A):
        for _ in range(L - len(row)):
            A[idx].append(0)

    return A, L


if __name__ == '__main__':
    r, c, k = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(3)]
    success = 0
    rlen, clen = 3, 3
    for time in range(101):
        if r <= rlen and c <= clen and A[r - 1][c - 1] == k:
            print(time)
            success = 1
            break
        if rlen >= clen:  # R연산
            A, clen = operation(A, clen)
        else:  # C연산
            A, rlen = operation(list(zip(*A)), rlen)  # 행과 열을 전치시켜 함수를 실행한다.
            A = list(zip(*A))  # 행과 열을 원상태로 바꾼다.
    if not success :
        print(-1)
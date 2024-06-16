def solution(numbers):
    # numbers.sort(key = lambda x : str(x), reverse=True) 이러면 3, 30이 있을 때 303이 되어버림
    numbers = list(map(str, numbers))
    print(numbers)
    numbers.sort(key=lambda x: x * 3, reverse=True)  # x*3을 통해 '330' > '303' 순으로 비교
    # 함수를 사용하여 정렬 기준을 설정합니다. x*3을 통해 각 숫자를 세 번 반복하여 비교합니다. 이는 주어진 숫자가 최대 1000 이하의 숫자이기 때문에, 예를 들어 6, 10, 2를 비교할 때, 666, 101010, 222를 비교하여 정렬합니다.

    # 모두 0으로 이루어진 경우 예외 처리
    if numbers[0] == '0':
        return '0'

    return ''.join(numbers)



# 연속 부분 수열 합의 개수
# "원형 수열의 연속하는 부분 수열의 합"으로 만들 수 있는 수가 "모두 몇 개"
tmp_answer = set()

def solution(elements):
    size = len(elements)
    for start_idx in range(len(elements)) :
        sum_num = 0
        for length in range(size) :
            sum_num += elements[(start_idx+length) % size]
            tmp_answer.add(sum_num)
    return len(tmp_answer)

print(solution([7, 9, 1, 1,4]))
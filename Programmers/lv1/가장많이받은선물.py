from collections import defaultdict
#https://velog.io/@daoh98/2024-%EC%B9%B4%EC%B9%B4%EC%98%A4-%EC%9C%88%ED%84%B0-%EC%9D%B8%ED%84%B4%EC%8B%AD-%EB%B3%B5%EC%88%98%EC%A0%84-%ED%8C%8C%EC%9D%B4%EC%8D%AC
def solution(friends, gifts) :
    friends_size = len(friends)
    answer_list = [0 for _ in range(friends_size)]

    gift_rate = defaultdict(int) # 선물 지수

    idx_record = dict()
    value_record = dict()

    chart = [[0] * friends_size for _ in range(friends_size)]

    for row in range(friends_size) :
        for col in range(friends_size) :
            if row == col :
                chart[row][col] = -1

    for idx, value in enumerate(friends) :
        idx_record[value] = idx
        value_record[idx] = value

    for gift in gifts :
        giver, receiver = gift.split()
        # 선물지수
        gift_rate[giver] += 1
        gift_rate[receiver] -= 1
        # 표
        idx_giver, idx_receiver = idx_record[giver], idx_record[receiver]

        # 받은게 많으면 음수, 준게 많으면 양수
        chart[idx_giver][idx_receiver] += 1
        chart[idx_receiver][idx_giver] -= 1

    for c in range(friends_size) :
        for i in range(friends_size) :
            if chart[c][i] > 0 : # 준게 많으면
                answer_list[c] += 1
            elif chart[c][i] == 0 :
                a = value_record[c]
                b = value_record[i]
                if gift_rate[a] > gift_rate[b] :
                    answer_list[c] += 1
    return max(answer_list)


    answer = 0
    return answer
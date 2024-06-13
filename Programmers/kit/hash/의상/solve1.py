from collections import defaultdict

def solution(clothes) :
    closet = defaultdict(int)
    for cloth, category in clothes :
        closet[category] += 1
    answer = 1
    for count in closet.values() :
        answer *= (count + 1)
    return answer - 1
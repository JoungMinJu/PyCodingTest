import heapq

def solution(scoville, K) :
    heapq.heapify(scoville) #최소힙
    answer = 0

    while len(scoville) > 1:
        first = heapq.heappop(scoville) # 가장 작은 스코빌지수)
        if first >= K :
            return answer
        second = heapq.heappop(scoville)
        new_scoville = first + (second * 2)
        heapq.heappush(scoville, new_scoville)
        answer += 1
    if scoville[0] >= K:
        return answer
    return -1
from collections import Counter

def solution(participants, completion) :
    participant_counter = Counter(participants)
    completion_counter = Counter(completion)

    answer = participant_counter - completion_counter

    return list(answer.keys())[0]
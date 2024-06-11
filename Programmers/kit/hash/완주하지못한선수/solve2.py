def solution(participants, completion) :
    dic = {}
    for participant in participants:
        dic[hash(participant)] = participants
    for c in completion :
        dic[hash(c)] = None
    for key in dic.keys() :
        if dic[key] :
            return dic[key]

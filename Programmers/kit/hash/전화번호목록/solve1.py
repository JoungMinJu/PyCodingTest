def solution(phone_book) :
    hash_dict = {}
    for number in phone_book :
        hash_dict[number] = True

    for number in phone_book:
        for i in range(1, len(number)) :
            prefix = number[:i]
            if prefix in hash_dict :
                return False
    return True
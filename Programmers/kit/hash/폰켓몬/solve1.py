def fun(names) :
    count_of_mon = len(set(names))
    count_of_select = len(names) // 2
    if count_of_mon <= count_of_select :
        return count_of_mon
    return count_of_select
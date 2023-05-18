def superDigit(n, k):
    if k == len(n) == 1:
        return int(n)

    res = 0
    for num in n:
        res += int(num)

    return superDigit(str(res*k),1)

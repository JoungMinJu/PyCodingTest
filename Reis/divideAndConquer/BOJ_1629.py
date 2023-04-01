A, B, C = map(int, input().split())


def dac(A, B, C):
    if B == 1:
        return A % C
    elif B % 2 == 0:
        return (dac(A, B // 2, C) ** 2) % C
    else:
        return ((dac(A, B // 2, C) ** 2) * A) % C

'''
2^32 == (2^16)^2 (연산 17번) 
== ((2^8)^2)^2 (연산 10번)
'''

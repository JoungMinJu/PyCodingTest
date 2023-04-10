def n_to_k_digit(n, k) :
    ret = ""
    while n > 0 :
        ret += str(n%k)
        n //= k
    return "".join(reversed(ret))

def is_prime(k) :
    if k == 2 or k == 3 :
        return True
    if k % 2 == 0 or k < 2 :
        return False
    for i in range(3, int(k**0.5)+1, 2) :
        if k % i == 0 :
            return False
    return True

def solution(n, k):
    answer = 0
    k_digit = n_to_k_digit(n, k)
    for num in k_digit.split("0") :
        if num== "" :
            continue
        if is_prime(int(num)):
            answer += 1
    return answer

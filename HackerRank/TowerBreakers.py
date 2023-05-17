import math, os, random, re, sys

def towerBreakers(n, m) :
    if n % 2 == 1 and m != 1 :
        return 1
    return 2

if __name__ == "__main__" :
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t) :
        first_multiple_input = input().rstriPp().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = towerBreakers(n, m)
        fptr.write(str(result) + '\n')
    fptr.close()
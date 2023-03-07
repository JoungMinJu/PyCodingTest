import sys
input = sys.stdin.readline

N = int(input())
words = []
for _ in range(N):
    words.append(input())

dict = {}

for word in words :
    square_root = len(word) - 1
    for c in word :
        if c in dict :
            dict[c] += pow(10, square_root)
        else :
            dict[c] = pow(10, square_root)
        square_root -= 1

# 정렬
dict = sorted(dict.values(), reverse = True)

result = 0
number = 9
for value in dict :
    result += value * number
    number -= 1

print(result)
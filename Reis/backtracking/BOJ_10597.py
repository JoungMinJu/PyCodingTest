import sys

input = sys.stdin.readline
word = input().rstrip()
n = len(word) if len(word) <= 9 else 9 + (len(word) - 9) // 2
answer = list()

def backtracking(index) :
    if index == len(word) :
        print(" ".join(answer))
        exit(0)
    if word[index] != '0' and word[index] not in answer:
        answer.append(word[index])
        backtracking(index+1)
        answer.pop()
    if word[index] != '0' and int(word[index: index + 2]) <= n and word[index:index + 2] not in answer:
        answer.append(word[index:index + 2])
        backtracking(index + 2)
        answer.pop()

backtracking(0)
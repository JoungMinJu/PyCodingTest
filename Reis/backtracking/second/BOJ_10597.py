import sys
input = lambda : sys.stdin.readline().rstip()

def backtracking(index) :
    if index == len(sentence) :
        print(" ".join(answer))
        exit(0)
    if sentence[index] != '0' and sentence[index] not in answer :
        answer.append(sentence[index])
        backtracking(index+1)
        answer.pop()
    if sentence[index] != '0' and int(sentence[index:index+2]) <= N and sentence[index:index+2] not in answer :
        answer.append(sentence[index:index+2])
        backtracking(index+2)
        answer.pop()

sentence = input()

if len(sentence) <= 9 :
    N = len(sentence)
else :
    # 최대 50개의 수
    N = (len(sentence)-9)//2 + 9

'''
[한자리수]
1. 0이 아니어야 한다
2. 리스트에서 중복되지 않아야 한다
[두 자리 수]
1. 해당 숫자가 N보다 작거나 같아야 한다.
2. 리스트에서 중복되지 않아야 한다.
3. 10의 자리수가 0이 아니어야 한다.
'''

answer = list()
backtracking(0)

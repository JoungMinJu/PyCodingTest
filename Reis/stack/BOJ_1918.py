# 중위 -> 후위
# [핵심] = 스택은 우선순위가 낮은 연산자부터 큰 연산자 순으로 쌓아야 한다.
from collections import deque

def get_seq(ch) :
    if ch in ["+", "-"] :
        return 0
    else :
        return 1

input_chars = list(input())
stack = deque()
answer = ""
for ch in input_chars :
    if ord('A') <= ord(ch)  <= ord("Z"):
        answer += ch
    else :
        if ch == '(' :
            stack.appendleft(ch)
        elif ch == ')' :
            while True :
                pop_ch = stack.popleft()
                if pop_ch == '(' :
                    break
                else :
                    answer += pop_ch
        else :
            while True :
                if len(stack) == 0:
                    stack.appendleft(ch)
                    break
                if stack[0] == '('  :
                    stack.appendleft(ch)
                    break
                else :
                    top_ch_seq = get_seq(stack[0])
                    now_ch_seq = get_seq(ch)
                    if top_ch_seq < now_ch_seq:
                        stack.appendleft(ch)
                        break
                    else :
                        answer += stack.popleft()

while stack:
    answer += stack.popleft()
print(answer)

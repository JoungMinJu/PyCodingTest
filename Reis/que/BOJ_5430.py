from collections import deque

testSize = int(input())

for test in range(testSize) :
    commands = input()
    n = int(input())
    arr = input()[1:-1].split(",")

    dq = deque(arr)
    flag = False

    if n == 0:
        dq = []
    for command in commands :
        if command == "R" :
            flag = not flag
        elif command == "D":
            if len(dq) == 0 :
                print("error")
                break
            else :
                if flag :
                    dq.pop()
                else :
                    dq.popleft()
    else:
        if not flag :
            print("[" + ",".join(dq) + "]")
        else :
            dq.reverse()
            print("[" + ",".join(dq) + "]")

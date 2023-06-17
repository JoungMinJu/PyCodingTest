import sys

input = lambda : sys.stdin.readline.rstrip()

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse= True)
boxes.sort(reverse = True)

time = 0

if cranes[0] < boxes[0] :
    print(-1)
else :
    while len(boxes) > 0 :
        for crane in cranes :
            for box in boxes :
                if crane >= box :
                    boxes.remove(box)
                    break
        time += 1
    print(time)
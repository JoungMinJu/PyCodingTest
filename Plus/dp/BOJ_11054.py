import sys
input = lambda : sys.stdin.readline().rstrip()

x = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

increase = [1] * x
decrease = [1] * x

for start in range(x) :
    for before in range(start) :
        if case[start] > case[before] :
            increase[start] = max(increase[start], increase[before] + 1)
        if reverse_case[start] > reverse_case[before] :
            decrease[start] = max(decrease[start], decrease[before] + 1)

result = [0] * x
for i in range(x) :
    result[i] =  increase[i] + decrease[x-i-1] -1
print(max(result))

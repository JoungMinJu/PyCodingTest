testSize = int(input())

for test in range(testSize):
    a, b = map(int, input().split(" "))
    print(f"Case #{test+1}: {a+b}")

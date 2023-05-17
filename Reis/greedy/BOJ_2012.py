N = int(input())
expected = []
for _ in range(N) :
    expected.append(int(input()))

expected.sort()

result = 0
for i in range(1, N) :
    result += abs(i-expected[i])
print(result)
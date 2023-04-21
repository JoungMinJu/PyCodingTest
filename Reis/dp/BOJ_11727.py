N = int(input())
s = [0, 1, 3]
for i in range(3, 1001) :
    s.append(s[i-2]*2 + s[i-1])
print(s[N] % 10007)
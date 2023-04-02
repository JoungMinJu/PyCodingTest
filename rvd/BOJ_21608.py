dR = [-1, 1, 0, 0]
dC = [0, 0, -1, 1]

N = int(input())
arr = [[0] * N for _ in range(N)]
students = [list(map(int, input().split())) for _ in range(N**2)]

for order in range(N**2) :
    student = students[order]
    candidates = []
    for row in range(N) :
        for col in range(N) :
            if not arr[row][col] :
                like = blank = 0
                for idx in range(4) :
                    next_row, next_col = row + dR[idx], col + dC[idx]
                    if 0 <= next_row < N and 0 <= next_col < N :
                        if arr[next_row][next_col] in student[1:]:
                            like += 1
                        if arr[next_row][next_col] == 0 :
                            blank += 1
                candidates.append([like, blank, row, col])
    candidates.sort(key = lambda x : (-x[0], -x[1], x[2],x[3]))
    arr[candidates[0][2]][candidates[0][3]] = student[0]

result = 0
students.sort()

for row in range(N):
    for col in range(N) :
        answer = 0
        for idx in range(4) :
            next_row, next_col = row + dR[idx], col + dC[idx]
            if 0 <= next_row < N and 0 <= next_col <  N :
                if arr[next_row][next_col] in students[arr[row][col]-1]:
                    answer +=1
        if answer != 0 :
            result += (10) ** (answer-1)
print(result)
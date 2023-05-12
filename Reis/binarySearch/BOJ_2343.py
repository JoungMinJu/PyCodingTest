import sys
input = lambda: sys.stdin.readline()

def get_count(mid) :
    count = sum = 0
    for lecture in lectures :
        if (sum + lecture > mid) :
            sum = 0
            count += 1
        sum += lecture
    if (sum > 0) :
        count += 1
    return count


N, M = map(int, input().split())
lectures = list(map(int, input().split()))
# M개의 블루레이에 모든 기타 강의 동영상
# 녹화 가능한 길이 최소로 할 것
low = min(lectures)
high = sum(lectures)

while (low <= high) :
    mid = (low + high) // 2
    count = get_count(mid)
    if (count <= M) :
        high = mid - 1
    else :
        low = mid + 1
print(low)
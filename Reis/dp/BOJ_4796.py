case = 0
while True :
    case += 1
    L, P, V = map(int, input().split()) # 연속하는 P일 중, L일 동안만 사용할 수 있다. 이제 막 V일짜리 휴가를 시작
    if (L, P, V) == (0, 0, 0) :
        break
    answer = L * (V//P) + min(V%P, L)
    print(f"Case {case}: {answer}")
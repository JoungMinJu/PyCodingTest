import sys

input = lambda: sys.stdin.readline().rstrip()

'''
"전위 순회"에서 발견한 "루트 값"을 기준으로 "중위 순회"를 보면 그 루트 값을 기준으로 왼쪽 서브트리, 오른쪽 서브 트리로 분리됨.
-> 이를 재귀로 응용!

1. "전위 순회"의 "루트"와 "중위 순회"의 값 중 일치하는 값의 인덱스 찾기
2. 인덱스를 기준으로 왼쪽 서브트리, 오른쪽 서브트리를 탐색
3. 후위 순회이기 때문에 서브 트리 탐색이 끝난 후 루트를 출력
'''


def solve(root, start, end):
    for i in range(start, end):
        if inorder[i] == preorder[root]:  # 찾았으면
            solve(root + 1, start, i)
            solve(root + i + 1 - start, i+1, end)
            print(preorder[root], end =' ')


T = int(input().split())
for test in range(T):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    solve(0, 0, N)
    print()

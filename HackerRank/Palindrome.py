def palindrome(s) :
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            # 왼쪽 문자를 제거한 경우 팰린드롬인지 확인
            if s[left+1:right+1] == s[left+1:right+1][::-1]:
                return left
            # 오른쪽 문자를 제거한 경우 팰린드롬인지 확인
            if s[left:right] == s[left:right][::-1]:
                return right
        left += 1
        right -= 1
    return -1

print(palindrome("racecar"))
print(palindrome("aaab"))
print(palindrome("aaa"))
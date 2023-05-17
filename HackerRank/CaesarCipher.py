
def caesarCipher(s, k):
    k %= 26
    result = ""
    tmp = ""
    for i in s :
        tmp = chr(ord(i) + k)
        if 'A' <= i <= 'Z' :
            if tmp > 'Z' :
                result += chr(ord(tmp)-26)
            else :
                result += tmp
        elif 'a' <= i <= 'z' :
            if tmp > 'z' :
                result += chr(ord(tmp)-26)
            else :
                result += tmp
        else :
            result += i
            continue
    return result

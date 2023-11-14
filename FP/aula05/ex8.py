def evenThenOdd(s):
    even = s[::2]
    odd = s[1::2]
    return even + odd

def noDouble(s):
    new_s = ""
    for c in range(len(s)):
        if s[c] != s[c-1]:
            new_s += s[c]

    return new_s

def repeatnum(num):
    for c in range(1, num+1):
        print(c)

repeatnum(5)



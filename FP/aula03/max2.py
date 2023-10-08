def max2(a, b):
    if a > b:
        return a
    return b

def max3(a, b, c):
    if max2(a, b) > c:
        return max2(a, b)
    return c

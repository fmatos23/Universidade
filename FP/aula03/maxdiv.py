def mdc(a,b):
    r = a % b
    if r == 0:
        return b
    if r > 0:
        return mdc(b,r)



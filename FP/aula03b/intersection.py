def intersects(a1,b1,a2,b2):
    assert a1 <= b1
    assert a2 <= b2
    if a1 <= b2 and a2 <= b1:
        return True
    return False

def intersection(a, b, c, d):
    """Return the intersection of intervals [a, b[ and [c, d[."""
    assert a <= b
    assert c <= d
    if intersects(a, b, c, d):
        e = max(a, c)
        f = min(b, d)
    return e, f


def testIntersection(a, b, c, d, x, y):
    """Call intersection, print result and check against expected result."""
    print(f"intersection({a}, {b}, {c}, {d})", end=" ")
    (e, f) = intersection(a, b, c, d)
    if (e, f) == (x, y):
        check = "OK"
    else:
        check = "FAIL"
    print(f"--> ({e}, {f})", check)


def main():
    testIntersection(1, 6, 4, 8,  4, 6)
    testIntersection(1, 6, 3, 5,  3, 5)
    # Acrescente mais casos de teste...
    ...


main()


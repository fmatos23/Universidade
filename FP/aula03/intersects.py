def intersects(a1,b1,a2,b2):
    assert a1 <= b1
    assert a2 <= b2
    if a1 <= b2 and a2 <= b1:
        return True
    return False

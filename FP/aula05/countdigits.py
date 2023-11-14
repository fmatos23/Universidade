def countDigits(str):
    count = 0
    for c in str:
        if c.isdigit():
            count += 1

    return count


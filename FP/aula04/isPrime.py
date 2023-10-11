def isPrime(n):
    for c in range(2, n):
        if n % c == 0:
            return False
    return True

def main():
    for c in range(2, 101):
        if isPrime(c):
            print(c)

main()

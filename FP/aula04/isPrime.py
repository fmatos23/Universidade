def isPrime(n):
    for c in range(2, n):
        if n % c == 0:
            return False
    return True

def main():
    for c in range(2, 101): # teoricamente devia de começar no 1 mas o numero 1 aparentemente não é primo (reparámos
        # nisto quando fomos pesquisar porque não tinhamos a certeza se era primo ou não)
        if isPrime(c):
            print(c)

main()

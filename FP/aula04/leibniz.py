def leibnizPi4(n):
    pi = 0
    for i in range(0, n):
        pi += (-1)**i / (2*i + 1)
    return pi * 4

def main():
    n = int(input("valor de n: "))
    print(f"A soma dos {n} primeiros termos é de {leibnizPi4(n)}")

main()
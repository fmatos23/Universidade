segundos = int(input("segundos que durou a chamada: "))

if segundos <= 60:
    custo = 0.12
else:
    custo = segundos *  (0.12/60)
    print("vai ter que pagar {}".format(custo))
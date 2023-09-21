PF = 20
PC = 24.95
IMP = 0.23
SPA = 0.2

lucro = ((PC - SPA) / (1 + IMP)) - PF
imposto = IMP * PC

numero = int(input('Number of sold books: '))
print("Lucro total: {}".format(lucro*numero))
print("Total de impostos: {}".format(imposto*numero))
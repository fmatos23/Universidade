# Complete o programa!

# a)

def loadFile(fname, lst):
    with open(fname, 'r') as file:
        file.readline()
        for line in file:
            data = line.strip('\n').split('\t')
            dataTuple = (int(data[0]), data[1], float(data[5]), float(data[6]), float(data[7]))
            lst.append(dataTuple)


# b) Crie a função notaFinal aqui...
def notaFinal(reg):
    return sum(reg[2:]) / 3
# c) Crie a função printPauta aqui...
def printPauta(lst, filename=""):
    text = f'{"Numero":>6} {"Nome":^50} {"Nota":>4}\n'
    for aluno in lst:
        text += f'{aluno[0]:>6} {aluno[1]:^50} {notaFinal(aluno):>4.1f}\n'

    print(text)


# d)
def main():
    lst = []
    # ler os ficheiros
    loadFile("school1.csv", lst)
    loadFile("school2.csv", lst)
    loadFile("school3.csv", lst)

    # ordenar a lista
    lst.sort(key=lambda reg: reg[0])

    # mostrar a pauta
    printPauta(lst)


# Call main function
if __name__ == "__main__":
    main()



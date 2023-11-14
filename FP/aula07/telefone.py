# Complete este programa como pedido no guião da aula.

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^35s} : {:<12s}".format("Numero", "Nome", "Morada"))
    for num in dic:
        print("{:>12s} : {:^35s} : {:<12s}".format(num, dic[num][0], dic[num][1]))

def addContact(dic):
    number = input("number: ")
    name = input("name: ")
    address = input("address: ")
    dic[number] = name, address


def removeContact(dic):
    number = input("number: ")
    del dic[number]

def findNumber(dic):
    number = input("number: ")
    if number in dic:
        print(dic[number])
    else:
        print(number)


def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    newdict = {}
    for num in contacts:
        if partName in contacts[num]:
            newdict[num] = contacts[num]
    return newdict


def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)istar contactos")
    print("(A)dicionar contacto")
    print("(R)emover contacto")
    print("Procurar (N)úmero")
    print("Procurar (P)arte do nome")
    print("(T)erminar")
    op = input("opção? ").upper()   # converts to uppercase...
    return op


def main():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": ("Universidade de Aveiro", "Santiago, Aveiro"),
        "727392822": ("Cristiano Aveiro","Lisboa"),
        "387719992": ("Maria Matos", "Leiria"),
        "887555987": ("Marta Maia", "Coimbra"),
        "876111333": ("Carlos Martins", "Porto"),
        "433162999": ("Ana Bacalhau", "Chelas")
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contactos:")
            listContacts(contactos)
        elif op == "A":
            print("Adicionar contacto")
            addContact(contactos)
        elif op == "R":
            print("Remover contacto: ")
            removeContact(contactos)
        elif op == "P":
            partName = input("Parte do nome: ")
            newDict = filterPartName(contactos, partName)
            listContacts(newDict)

        else:
            print("Não implementado!")
    

# O programa começa aqui
main()


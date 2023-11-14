def remove_duplicates(lst):
	newLst = []
	for num in lst:
		if num not in newLst:
			newLst.append(num)
	return newLst




num = input("Dá me um número: ")
lista = []
while num != "STOP":
	lista.append(int(num))
	num = input("Dá me um número: ")
print(lista)

print(remove_duplicates(lista))

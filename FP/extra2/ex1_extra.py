def isValidnum(num):
	validchar = ["+","0","1","2","3","4","5","6","7","8","9"]
	for c in num:
		if num[0] == "+":
			if len(num) >= 4:
				return True
			else:
				return False
		elif c not in validchar :
			return False
		elif len(num) < 3 or len(num) > 9:
			return False
		else:
			return True

'''	if num[0] == "+":
		if len(num) < 4:
			return False
		elif len(num) >= 4 and len(num) <= 10:
			return True
		else:
			return False
	else:
	elif num[0] == "0" or :
		if len(num) < 3:
			return False
		elif len(num) >= 3 and len(num) <=9
'''

def registercall():
	lstOrigem = []
	lstDest = []
	nO = input("Telefone origem: ")
	nD = input("Telefone destino:")
	while len(nO) < 3 or len(nD) < 3:
		print("numero inválido")
		nO = input("Telefone origem: ")
		nD = input("Telefone destino: ")
	lst.append(n)
	print(lst)


def main():

	while True:
		print("1) Registar chamada")
		print("2) Ler ficheiro")
		print("3) Listar cliente")
		print("4) Fatura")
		print("5) Terminar")
		print("6) Ni*")
		option = int(input("Opção? "))
		if option == 5:
			break

		elif option == 1:
			print(f"opção escolhida: {option}")
		
		elif option == 2:
			print(f"opção escolhida: {option}")
		elif option == 3:
			print(f"opção escolhida: {option}")
		elif option == 4:
			print(f"opção escolhida {option}")
		else:
			print("numero inválido")
	


from unidecode import unidecode

def count_letters(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        count = 0
        newdict = {}
        for char in file.read():
            char = char.lower()
            char = unidecode(char)
            if char.isalpha():
                if char not in newdict:
                    newdict[char] = 1
                else:
                    newdict[char] += 1
                sorted_dict = dict(sorted(newdict.items()))
    return sorted_dict

dicionario = count_letters('pg3333.txt')

for c in dicionario:
    print(c, dicionario[c])